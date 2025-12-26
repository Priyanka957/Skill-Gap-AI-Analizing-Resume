import json

with open("D:/Skill-Gap-AI-Analizing-Resume/JSON/q3data.json content", "r") as file:
    data = json.load(file)
    for key, value in data.items():
        print(key, ":", value)