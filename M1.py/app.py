
import streamlit as st
from utils.parser import parse_file
from utils.cleaner import clean_text

st.set_page_config(
    page_title="Milestone 1: Data Ingestion & Parsing",
    layout="wide"
)

st.markdown(
    """
    <div style="background-color:#3f51b5;padding:15px;border-radius:6px">
        <h2 style="color:white;">Milestone 1: Data Ingestion and Parsing Module (Weeks 1–2)</h2>
        <p style="color:white;">
        Resume and Job Description upload system · File parsing and text extraction · Clean normalized input data
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Documents")

    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"]
    )

    jd_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx", "txt"]
    )

with col2:
    st.subheader("Document Preview")

    if resume_file:
        resume_text = parse_file(resume_file)
        resume_text = clean_text(resume_text)

        st.markdown("**Resume Preview**")
        st.text_area("", resume_text, height=300)

    if jd_file:
        jd_text = parse_file(jd_file)
        jd_text = clean_text(jd_text)

        st.markdown("**Job Description Preview**")
        st.text_area(" ", jd_text, height=300)
