from PyPDF2 import PdfReader
pdf = PdfReader("resume.pdf") 
metaData = pdf.metadata
for key, value in metaData.items() :
    print(f"{key} : {value}")