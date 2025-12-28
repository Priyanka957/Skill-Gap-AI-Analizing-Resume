skills = set()

sentences = ["I know Python", "I use SQL"]
for s in sentences:
    if "Python" in s:
        skills.add("python")
    if "SQL" in s:
        skills.add("sql")

print(list(skills))