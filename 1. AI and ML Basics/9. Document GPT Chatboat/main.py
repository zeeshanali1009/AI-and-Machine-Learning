import streamlit as st
import openai
import os
from PyPDF2 import PdfReader
from docx import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document as LangDoc

#  Set OpenAI key
openai.api_key = st.secrets["OPENAI_API_KEY"]

#  Page settings
st.set_page_config(page_title="📄 Document GPT", layout="centered")
st.title("📄 Ask your Document (GPT)")

#  Upload
uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

# Handle file
if uploaded_file:
    file_text = ""
    if uploaded_file.type == "application/pdf":
        file_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        file_text = extract_text_from_docx(uploaded_file)

    #  Split text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_text(file_text)

    #  Create vectorstore
    embeddings = OpenAIEmbeddings()
    docs = [LangDoc(page_content=t) for t in texts]
    db = FAISS.from_documents(docs, embeddings)

    #  Ask the doc
    query = st.text_input("Ask a question about the document:")
    if query:
        # Search and respond
        matching_docs = db.similarity_search(query)
        llm = ChatOpenAI(temperature=0)
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=matching_docs, question=query)
        st.markdown(f"**Answer:** {response}")
