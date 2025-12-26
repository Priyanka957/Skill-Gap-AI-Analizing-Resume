from PyPDF2 import PdfReader
headings = []
pdf = PdfReader("resume.pdf")
for page in pdf.pages :
    lines = page.extract_text().split('\n')
    for line in lines :
        clean = line.strip()
        if clean.isupper() :
            headings.append(clean)
print("Headings :")
for heading in headings :
    print(heading)
