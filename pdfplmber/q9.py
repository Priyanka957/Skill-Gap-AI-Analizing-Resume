import pdfplumber
with pdfplumber.open("sample.pdf") as pdf:
    page = pdf.pages[0]
    print("lines:",page.lines)
    print("rects:",page.rects)