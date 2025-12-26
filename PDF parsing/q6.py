
    
    
import pdfplumber
with pdfplumber.open("resume.pdf") as pdf :
    table = pdf.pages[0].extract_table()
    text = pdf.pages[0].extract_text()
    print(text.split('\n')[0])
    
        
