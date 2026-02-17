import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from constants import groq_key
import os

# page configuration
st.set_page_config(page_title="PDF QA App")
st.title("📄 Chat with your PDF (RAG)")

os.environ["GROQ_API_KEY"] = groq_key

## upoad pdf file
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    # Read PDF
    pdf_reader = PdfReader(uploaded_file)
    raw_text = ""

    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content

    # Split text
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200
    )

    texts = splitter.split_text(raw_text)

    st.success(f"PDF processed into {len(texts)} chunks")

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector store
    db = FAISS.from_texts(texts, embeddings)

    # LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )
    # User Query

    query = st.text_input("Ask a question about the document")

    if query:

        docs = db.similarity_search(query)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer using ONLY the provided context.

        Context:
        {context}

        Question:
        {query}
        """

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)