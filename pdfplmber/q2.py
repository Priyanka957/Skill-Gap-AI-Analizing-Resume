import pdfplumber

with pdfplumber.open("sample.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n--- Page {i+1} ---")
        print(page.extract_text())