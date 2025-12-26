import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)