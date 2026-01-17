import streamlit as st
import requests
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

# --- Page Config ---
st.set_page_config(page_title="Free RAG Bot", layout="wide")
st.title("🤖 Free Google Doc Chatbot")

# --- API KEY HANDLING (Secret + Sidebar Fallback) ---
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    with st.sidebar:
        st.header("Settings")
        groq_api_key = st.text_input("Groq API Key", type="password")

# --- Functions ---

def get_google_doc_text(url):
    try:
        if "/d/" not in url:
            return None, "Invalid URL format."
        doc_id = url.split("/d/")[1].split("/")[0]
        export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
        response = requests.get(export_url)
        if response.status_code == 200:
            return response.text, None
        else:
            return None, f"Failed to fetch. Status: {response.status_code}"
    except Exception as e:
        return None, str(e)

def process_text(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# --- Main Logic ---

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

doc_url = st.text_input("Paste Public Google Doc URL:")

if st.button("Load Document"):
    if not groq_api_key:
        st.error("API Key missing.")
    elif not doc_url:
        st.error("Please enter a URL.")
    else:
        with st.spinner("Processing..."):
            raw_text, error = get_google_doc_text(doc_url)
            if raw_text:
                st.session_state.vectorstore = process_text(raw_text)
                st.success("Knowledge Base Ready!")
            else:
                st.error(error)

if prompt := st.chat_input("Ask a question..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.vectorstore:
        with st.chat_message("assistant"):
            if not groq_api_key:
                 st.error("API Key is missing.")
                 st.stop()
                 
            # Model
            llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")
            
            retriever = st.session_state.vectorstore.as_retriever()
            
            # Simple RAG Chain (The Safe Way)
            template = """Answer the question based only on the following context:
            {context}
            
            Question: {question}
            """
            prompt_template = ChatPromptTemplate.from_template(template)
            
            def format_docs(docs):
                return "\n\n".join([d.page_content for d in docs])

            chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt_template
                | llm
                | StrOutputParser()
            )
            
            response = chain.invoke(prompt)
            st.markdown(response)
    else:
        st.warning("Please load a document first.")