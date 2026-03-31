import requests
from sentence_transformers import SentenceTransformer
import chromadb
import sys
import gradio as gr

# -----------------------------
# 1. LOAD EMBEDDING MODEL
# -----------------------------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# 2. CREATE VECTOR DATABASE
# -----------------------------
client = chromadb.Client()
collection = client.create_collection("rag_data21")

# Load data
with open("data.txt") as f:
    lines = f.readlines()
# Store embeddings
for i, line in enumerate(lines):
    emb = embed_model.encode(line)
    collection.add(
        ids=[str(i)],
        embeddings=[emb.tolist()],
        documents=[line]
    )
# -----------------------------
# 5. RETRIEVE FUNCTION
# -----------------------------
def retrieve(query):
    q_emb = embed_model.encode(query)

    results = collection.query(
        query_embeddings=[q_emb.tolist()],
        n_results=5
    )

    return " ".join(results["documents"][0])


# -----------------------------
# 6. OLLAMA API CALL
# -----------------------------
def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral:latest",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.0,
                "num_predict": 500,
                "stop": ["Question:", "User query:","Context","QUESTION: "]
            }
        }
    )
    answer = response.json()["response"].strip()
    # remove unwanted phrases
    bad_phrases = [
        "here's", "here is", "updated version",
        "based on","revised version ", "context", "rules"
    ]
    for word in bad_phrases:
        if word in answer.lower():
            answer = answer.split("\n")[0]

    return answer


# -----------------------------
# 7. RAG PIPELINE
# -----------------------------
def rag_chat(question, history):
    context = retrieve(question)
    prompt = f"""
        You are a Retainuser CRM assistant.

        Answer ONLY using the context below.
        Do NOT use your own knowledge.
        Each benefit must be on a new line.
        Each features must be on a new line.

        If answer is not present in context, reply exactly:
        Not available


        Context: {context}

        Question: {question}

        Answer:
        """
    return ask_ollama(prompt)


# -----------------------------
# 8. CHAT LOOP
# -----------------------------
if __name__ == "__main__":
        default_history = [
            {"role": "assistant", "content": "Hi i am an AI assistant for Retainuser CRM Software Pvt Ltd, a SaaS company providing CRM software for lead management, follow-up automation, and sales tracking.\nYour role: - Answer customer questions about Retainuser CRM - Explain features in simple language - Help users understand benefits - Encourage demo booking when appropriateAbout Retainuser CRM: Retainuser CRM is a cloud-based software designed to help businesses: - Capture leads from multiple sources - Manage follow-ups automatically - Track sales pipeline - Automate WhatsApp communication - Improve team productivity \n Communication Rules: - Speak in friendly and simple language - Keep answers short and clear - Be helpful and polite - Suggest demo when user shows interest and share number +919643880542"}
        ]
        gr.ChatInterface(
            fn=rag_chat,
            chatbot=gr.Chatbot(
                value=default_history
            )
        ).launch(share=True)
        