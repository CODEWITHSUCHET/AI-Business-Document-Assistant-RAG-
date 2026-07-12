# 🤖 AI Business Document Assistant (RAG)

An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them using natural language. The system leverages semantic search with FAISS and Google's Gemini LLM to deliver fast, accurate, and context-aware answers from business documents.

---

# 🚀 Project Overview

Organizations generate thousands of documents such as reports, policies, contracts, manuals, financial statements, and research papers. Extracting relevant information manually is slow, inefficient, and time-consuming.

This project addresses this challenge by building an intelligent document assistant that understands uploaded PDF documents and answers user questions in natural language using Retrieval-Augmented Generation (RAG).

Instead of relying solely on an LLM's pre-trained knowledge, the application retrieves relevant document content through semantic search before generating responses, ensuring answers remain grounded in the uploaded documents.

---

# ✨ Key Features

- Upload PDF documents
- Intelligent document understanding
- Semantic search using FAISS
- Retrieval-Augmented Generation (RAG)
- Context-aware responses using Google Gemini
- LangChain-powered pipeline
- Simple Streamlit web interface
- Fast and scalable document search

---

# 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- FAISS Vector Database
- PyPDF
- Sentence Transformers

---

# ⚙️ Architecture

```
                PDF Documents
                      │
                      ▼
             Text Extraction
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
        User asks a Question
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

1. Upload one or more PDF documents.
2. Extract text from the uploaded files.
3. Split the document into semantic chunks.
4. Generate vector embeddings.
5. Store embeddings inside FAISS.
6. User asks a question.
7. Retrieve the most relevant document chunks.
8. Send retrieved context to Google Gemini.
9. Generate an accurate, document-grounded response.

---

# 💼 Business Applications

- Enterprise Knowledge Assistant
- Internal Policy Search
- Contract & Legal Document Q&A
- HR Documentation Assistant
- Financial Report Analysis
- Research Paper Assistant
- Standard Operating Procedure (SOP) Search
- Customer Support Knowledge Base

---

# 📷 Application Preview

*Add screenshots of the Streamlit application here.*

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

- Multi-document conversations
- Chat history
- Source citation
- Authentication
- Docker deployment
- Cloud deployment
- OCR support for scanned PDFs

---

# 👨‍💻 Author

**Suchet Mahajan**

MBA | IIT Mandi (Minor in Computer Science)

Business Growth • Strategy • Analytics • AI

GitHub: https://github.com/CODEWITHSUCHET
