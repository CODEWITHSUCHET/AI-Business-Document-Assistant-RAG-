# 🤖 AI Google Docs Assistant (RAG)

An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to connect a public Google Document and interact with it using natural language. The system retrieves relevant information using semantic search with FAISS and generates context-aware responses using Google's Gemini LLM.

---

# 🚀 Project Overview

Organizations frequently share reports, policies, documentation, meeting notes, research papers, and knowledge bases through Google Docs. Locating specific information within lengthy documents can be time-consuming and inefficient.

This project solves that problem by allowing users to provide a public Google Docs link and ask questions in natural language. The application retrieves relevant content using semantic search and generates accurate, context-aware answers using Google's Gemini LLM.

Instead of relying solely on the LLM's internal knowledge, responses are grounded in the actual document content through a Retrieval-Augmented Generation (RAG) pipeline.

---

# ✨ Key Features

- Load public Google Docs
- Automatic document parsing
- Semantic search using FAISS
- Retrieval-Augmented Generation (RAG)
- Context-aware responses using Google Gemini
- LangChain-powered pipeline
- Interactive Streamlit interface
- Fast document retrieval

---

# 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- FAISS
- Google Docs API
- Sentence Transformers

---

# ⚙️ Architecture

```
          Google Docs URL
                 │
                 ▼
        Document Extraction
                 │
                 ▼
          Text Chunking
                 │
                 ▼
      Embedding Generation
                 │
                 ▼
        FAISS Vector Store
                 │
        User Question
                 │
                 ▼
      Semantic Retrieval
                 │
                 ▼
      Google Gemini LLM
                 │
                 ▼
      Context-Aware Answer
```

---

# 📌 Workflow

1. Enter a public Google Docs URL.
2. Load the document.
3. Extract and split the content into chunks.
4. Generate vector embeddings.
5. Store embeddings in FAISS.
6. Ask questions in natural language.
7. Retrieve the most relevant document context.
8. Generate accurate answers using Google Gemini.

---

# 💼 Business Applications

- Enterprise Knowledge Assistant
- Internal Documentation Search
- Company Policy Assistant
- Research Documentation
- Knowledge Base Search
- Project Documentation Assistant

---

# 📷 Application Preview

(Add screenshots here)

---

# 📦 Installation

```bash
git clone https://github.com/CODEWITHSUCHET/ai-rag-chatbot.git

cd ai-rag-chatbot

pip install -r requirements.txt

streamlit run app.py
```

---

# 🔮 Future Improvements

- Support multiple Google Docs
- PDF & DOCX support
- Authentication
- Source citations
- Docker deployment
- Cloud deployment

---

# 👨‍💻 Author

**Suchet Mahajan**

MBA | IIT Mandi (Minor in Computer Science)

Business Growth • Strategy • Analytics • AI
