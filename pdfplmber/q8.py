import pdfplumber
with pdfplumber.open("sample.pdf") as pdf:
    page = pdf.pages[0]
    images = page.images
    print("number of images:",len(images))