import pdfplumber

with pdfplumber.open("sample.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    if text is None:
        print("scanned PDF(no extractable text)")
    else:
        print("text-based PDF")