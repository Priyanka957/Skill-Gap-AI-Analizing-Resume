predefined_skills  = ["python","java","sql","html"]

resume_text = """
I have experience in Python, Java, SQL, HTML.
"""
found = [s for s in predefined_skills
if s in resume_text.lower()]
print(found)