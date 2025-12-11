resume = input("Enter resume skills:")
Job = input("Enter Job required skills:")

resume_list = resume.split(",")
Job_list = Job.split(",")

matched = []
missing = []
for skills in Job_list:
    if skills in resume_list:
        matched.append(skills)
    else:
        missing.append(skills)


print("Mathched Skills:", matched)
print("Missing Skills:",missing)
