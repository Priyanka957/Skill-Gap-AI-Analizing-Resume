from PyPDF2 import PdfReader

reader = PdfReader("resume.pdf")
print(reader.pages[0].extract_text())