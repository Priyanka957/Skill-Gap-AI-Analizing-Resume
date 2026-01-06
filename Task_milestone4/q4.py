import streamlit as st

file = st.file_uploader("Upload a file", type=["pdf", "docx", "txt"])

if file:
    st.success(f"Uploaded file: {file.name}")
