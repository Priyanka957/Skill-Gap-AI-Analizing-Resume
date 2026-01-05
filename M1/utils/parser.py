
import pdfplumber
import docx

def parse_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text(layout=True)
        if page_text:
            text += page_text + "\n"

    return text

def parse_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_txt(file):
    return file.read().decode("utf-8")

def parse_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return parse_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return parse_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        return parse_txt(uploaded_file)
    else:
        return "Unsupported file format"
