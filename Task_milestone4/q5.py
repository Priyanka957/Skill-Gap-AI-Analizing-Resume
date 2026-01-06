
import streamlit as st

file = st.file_uploader("Upload TXT file", type=["txt"])

if file:
    text = file.read().decode("utf-8")
    st.text_area("Preview", text[:300])
