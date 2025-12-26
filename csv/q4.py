import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/skills.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)