resume_text = "Python and SQL are required. Python is important."
skills = ["Python", "SQL"]

for skill in skills:
    count = resume_text.lower().count(skill.lower())
    print(skill,":",count)