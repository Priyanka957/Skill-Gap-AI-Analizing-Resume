import csv

data = [
    [1, "Priyanka"],
    [2, "Rahul"],
    [3, "Anita"]
]

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/q8list_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name"])
    writer.writerows(data)
print("CSV created from list")