from PyPDF2 import PdfReader

reader = PdfReader("resume.pdf")
text_found = False

for page in reader.pages:
    if page.extract_text():
        text_found = True

if text_found:
    print("Text-based PDF")
else:
    print("Scanned PDF")