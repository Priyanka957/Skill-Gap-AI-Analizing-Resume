import pdfplumber
with pdfplumber.open("sample.pdf") as pdf:
    words = pdf.pages[0].extract_words()
    for word in words[:5]:
        print(word)