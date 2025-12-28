import pdfplumber
with pdfplumber.open("sample.pdf") as pdf:
    pages = pdf.pages[0]
    tables = pages.extract_tables()
    print(tables[0])