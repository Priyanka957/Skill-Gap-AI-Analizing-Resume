import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/products.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        print(row[0])