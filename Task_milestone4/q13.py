import streamlit as st

file = st.file_uploader("Upload TXT only", type=["txt"])

if file is None:
    st.warning("No file uploaded")
