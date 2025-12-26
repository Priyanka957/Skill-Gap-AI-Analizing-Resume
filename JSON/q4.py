import json
student = {'name': 'priyanka', 'age': 19, 'grade': 'A'}

with open("D:/Skill-Gap-AI-Analizing-Resume/JSON/q4student.json content", "w") as file:
    json.dump(student, file)