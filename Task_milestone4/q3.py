import streamlit as st

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["pdf", "docx", "txt"]
)
