import streamlit as st

st.file_uploader("Upload file")

if st.button("Process File"):
    st.success("Processing started...")
