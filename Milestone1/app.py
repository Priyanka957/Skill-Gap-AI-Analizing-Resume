import streamlit as st
import os
from re import sub

def loadTxt(file):
    """
    This function will load the text file and return the content as string
    args : file -> uploaded txt file (Streamlit)
    return-type : string
    """
    content = file.read().decode("utf-8")
    return content


def preview(content, length=200):
    """
    This will return a preview of default length of 200 characters
    args : content -> string
           length -> integer
    return-type : string
    """
    return content[:length]


def cleanText(content):
    """
    This function will clean the content
    args : content -> string
    return-type : string
    """
    clean = content.lower()
    clean = sub(r"[^a-zA-Z0-9/:\s]", "", clean)
    clean = sub(r"\s+", " ", clean)
    return clean.strip()


def saveFile(content="", fileName="output"):
    """
    This will save the content in a text file
    args : fileName -> string
           content -> string
    return-type : void
    """
    os.makedirs("files", exist_ok=True)
    path = os.path.join("files", fileName + ".txt")
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return path

st.title("📄 Text File Cleaner")

st.write(
    "Upload a `.txt` file, clean the content, "
    "and preview the processed output."
)

uploaded_file = st.file_uploader(
    "Drag and drop TXT file here",
    type=["txt"]
)

if uploaded_file:

    st.success("File uploaded successfully!")

    rawContent = loadTxt(uploaded_file)

    st.subheader("Preview for Raw Content")
    st.write(preview(rawContent))

    if st.button("Clean & Process"):

        cleanContent = cleanText(rawContent)

        st.subheader("Preview for Cleaned Content")
        st.write(preview(cleanContent))

        outputPath = saveFile(cleanContent, fileName="output_txt")

        st.success("Output saved successfully")

        st.subheader("Cleaned output")
        st.write(cleanContent)
