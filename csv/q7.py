import csv

total = 0
with open("D:/Skill-Gap-AI-Analizing-Resume/csv/q7sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += int(row["price"]) * int(row["quantity"])
print("Total Sales:", total)