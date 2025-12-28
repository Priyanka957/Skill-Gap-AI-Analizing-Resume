import pdfplumber

with pdfplumber.open("sample.pdf") as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(text)