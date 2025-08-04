import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.storage import StorageContext
import faiss
import os

# Step 1: Load documents
@st.cache_resource
def load_documents(_folder_path):
    return SimpleDirectoryReader(_folder_path).load_data()

# Step 2: Set up index (FAISS + HuggingFace)
@st.cache_resource
def setup_index(_documents):
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    service_context = ServiceContext.from_defaults(embed_model=embed_model)

    # Set up FAISS index
    faiss_index = faiss.IndexFlatL2(384)
    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        _documents,
        service_context=service_context,
        storage_context=storage_context
    )
    return index.as_chat_engine(chat_mode="condense_question", verbose=True)

# Streamlit UI
st.set_page_config(page_title="📄 Document GPT with LlamaIndex")
st.title("📄 Chat with Your Document")

uploaded_folder = "docs"

# Upload PDF/DOC
uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])
if uploaded_file:
    os.makedirs(uploaded_folder, exist_ok=True)
    filepath = os.path.join(uploaded_folder, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Uploaded {uploaded_file.name}")

    # Load documents and set up index
    docs = load_documents(uploaded_folder)
    chat_engine = setup_index(docs)

    # Chat interface
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_prompt = st.text_input("Ask a question about the document:")
    if user_prompt:
        response = chat_engine.chat(user_prompt)
        st.session_state.chat_history.append((user_prompt, response.response))

    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**📄 DocBot:** {a}")
        st.markdown("---")
