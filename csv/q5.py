import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/marks.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Priyanka", "Maths", 95])
print("Row added successfully")