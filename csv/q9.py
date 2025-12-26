import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/q9people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["age"]) > 30:
            print(row)