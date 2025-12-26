from PyPDF2 import PdfReader
reader = PdfReader("resume.pdf")
text = reader.pages[0].extract_text()
print(text)