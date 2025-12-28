resume_skills = ["Python", "SQL"]
jd_skills = ["Python", "SQL", "Git", "Machine Learning"]

missing_skills = set(jd_skills) - set(resume_skills)
print(list(missing_skills))