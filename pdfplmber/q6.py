import pdfplumber
with pdfplumber.open("sample.pdf") as pdf:
    for page_no,page in enumerate(pdf.pages):
        tables = page.extract_tables()
        print(f"page{page_no+1} tables:",tables)