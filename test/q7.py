jd_text = "I have a good communication and team work skills"
soft_skills=["communication","problem solving","team work skills"]
found_soft_skills=[]

for skills in soft_skills:
    if skills.lower() in jd_text.lower():
        found_soft_skills.append(skills)
print(found_soft_skills)
        