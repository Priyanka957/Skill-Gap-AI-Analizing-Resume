import pdfplumber
import pandas as pd

with pdfplumber.open("sample.pdf") as pdf:
    table = pdf.pages[0].extract_tables()[0]
    df = pd.DataFrame(table[1:],columns=table[0])
    df.to_csv("output.csv",index = False)
    
    print("table saved as output.csv")