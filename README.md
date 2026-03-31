🤖 LLM RAG Model (Retrieval-Augmented Generation)

An end-to-end Retrieval-Augmented Generation (RAG) system that combines Large Language Models (LLMs) local api with vector search to answer questions from custom data.
---

## 🚀 Features

* 🔍 Semantic search using embeddings
* 🧠 Context-aware responses with LLM
* 📂 Custom dataset support (PDF, text, etc.)
* ⚡ Fast retrieval using vector database (CHROMA DB)
* 🏠 Local LLM inference using Ollama local api
* 💬 Question-answering system

---

## 🏗️ Architecture

```
User Query
    ↓
Convert to Embedding
    ↓
Vector Search (FAISS)
    ↓
Retrieve Relevant Context
    ↓
Pass to LLM (Ollama)
    ↓
Generate Final Answer
```

---

## 🧠 Tech Stack
 
 Language: Python
 LLM: Ollama (Local Models)
 Embeddings:Sentence Transformers
 Vector DB:CHROMO DB
 UI : Gradio

---

## 📦 Installation

### 1. Clone Repository

```bash
git clone https://github.com/surku12/llm-rag-model.git
cd llm-rag-model
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup

### Install Ollama

Download and install from: https://ollama.com

Run model:

```bash
ollama run llama2
```

---

## ▶️ Usage

### 1. Add your documents

Place your files inside:

```
/data
```

### 2. Run embedding script

```bash
python ragsearch.py
```

### 3. Start chatbot

```bash
python ragsearch.py
```

---

## 💡 Example

**Input:**

```
What are office working hours?
```

**Output:**

```
Our office is open Monday to Saturday, 9 AM to 6 PM IST.
```

---

## 📁 Project Structure

```
llm-rag-model/

│── ragsearch.py               # Main chatbot
│── data.txt             #traindatafile
│── README.md
```

---

## 🔥 Key Concepts

* **RAG (Retrieval-Augmented Generation):** Combines retrieval + generation
* **Embeddings:** Convert text into vectors
* **Cosine Similarity:** Finds relevant documents
* **LLM:** Generates human-like responses

---

## 🛠️ Future Improvements

* Add web UI
* Deploy on AWS
* Use better vector DB (Pinecone)
* Add streaming responses

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Suraj Dhingra**
AI Developer | Generative AI Enthusiast

---

