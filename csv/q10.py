import csv

with open("D:/Skill-Gap-AI-Analizing-Resume/csv/q10source.csv", "r") as src, open("copy.csv", "w", newline="") as dest:
    reader = csv.reader(src)
    writer = csv.writer(dest)
    for row in reader:
        writer.writerow(row)
print("File copied successfully")