import pdfplumber
with pdfplumber.open("sample.pdf") as pdf:
    print("total pages:",len(pdf.pages))