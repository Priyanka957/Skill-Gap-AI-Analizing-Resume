import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/q6data.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)
print("Total rows:", len(rows)-1)