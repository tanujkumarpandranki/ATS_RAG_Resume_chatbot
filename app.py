import streamlit as st
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader

from nlp import clean_text, extract_skills
from ml import compute_similarity, compute_ats
from rag import build_rag, retrieve_context
from chatbot import get_response

# load key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.title("ATS + RAG Chatbot")

file = st.file_uploader("Upload Resume", type="pdf")
job_desc = st.text_area("Paste Job Description")

if file and job_desc:

    # load pdf
    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    resume_text = " ".join([d.page_content for d in docs])

    # NLP
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_desc)

    resume_skills = extract_skills(clean_resume)
    job_skills = extract_skills(clean_job)

    # ML
    similarity = compute_similarity(clean_resume, clean_job)
    ats = compute_ats(similarity, resume_skills, job_skills)

    missing = list(set(job_skills) - set(resume_skills))

    st.write("ATS Score:", ats)
    st.write("Missing Skills:", missing)

    # RAG
    retriever = build_rag(docs)

    # CHAT
    query = st.text_input("Ask question")

    if query:
        context = retrieve_context(retriever, query)

        answer = get_response(context, ats, missing, query, api_key)

        st.write(answer)