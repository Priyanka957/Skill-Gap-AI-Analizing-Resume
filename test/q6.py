resume_text = "I learnt Python,SQL,JAVA"
skill_list = ["Python","JAVA","Data Analyst","SQL"]
found_skills = []

for skill in skill_list:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)
        
print(found_skills)