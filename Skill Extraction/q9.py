resume_skills = ["Python", "SQL", "Git"]
jd_skills = ["Python", "Java", "Git"]

common_skills = set(resume_skills) & set(jd_skills)
print(list(common_skills))
