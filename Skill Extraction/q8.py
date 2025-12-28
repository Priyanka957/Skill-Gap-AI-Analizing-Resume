import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/test/skills.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["category"].strip().lower()
        if category == "technical":
            print(row["skill"])