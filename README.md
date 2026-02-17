# 📄 Chat with Your PDF — RAG App

An AI-powered web application that allows users to upload a PDF document and ask questions about its content using **Retrieval-Augmented Generation (RAG)**.

Built with **Streamlit, LangChain, FAISS, HuggingFace Embeddings, and Groq LLM (LLaMA 3.1)**.

---

## 🌐 Live Demo

🚀 **Try the App Here:**  
👉 https://ai-document-app-system-wggkmig7xhynefhmnmgkww.streamlit.app/

Upload any PDF → Ask questions → Get context-grounded answers instantly.

---

## ✨ Features

- 📂 Upload any PDF document
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast inference using Groq LLaMA-3.1
- 📚 Context-aware answers (minimized hallucinations)
- 🌐 Clean web interface with Streamlit
- 🔒 Secure API key handling via environment variables

---

## 🏗️ Tech Stack

- **Frontend/UI:** Streamlit  
- **PDF Processing:** PyPDF2  
- **Text Splitting:** LangChain Text Splitters  
- **Embeddings:** HuggingFace (MiniLM-L6-v2)  
- **Vector Database:** FAISS  
- **LLM:** Groq — LLaMA 3.1 8B Instant  
- **Language:** Python  

---

## 🧠 How It Works (RAG Pipeline)

1. User uploads a PDF  
2. Text is extracted from the document  
3. Text is split into chunks  
4. Each chunk is converted into vector embeddings  
5. Embeddings are stored in FAISS  
6. User asks a question  
7. Relevant chunks are retrieved  
8. LLM generates answer using ONLY retrieved context  

---

