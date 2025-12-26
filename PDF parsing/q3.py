from PyPDF2 import PdfReader

reader = PdfReader("resume.pdf")
print("Total pages:", len(reader.pages))