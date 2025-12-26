import csv

resume_text = "experienced in python and sql"

with open("D:/Skill-Gap-AI-Analizing-Resume/test/skills.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["skill"].lower() in resume_text.lower():
            print(row["skill"])
