import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["Priyanka", 22, "A"])
    writer.writerow(["Rahul", 23, "B"])
    writer.writerow(["Anita", 21, "A"])

print("students.csv created")