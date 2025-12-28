import csv

extracted_skills = ["Python", "SQL", "Git"]

with open("extracted_skills.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Skill"])
    for skill in extracted_skills:
        writer.writerow([skill])

print("Skills saved successfully")
