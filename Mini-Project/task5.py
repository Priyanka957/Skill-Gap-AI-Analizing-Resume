skills = input("Enter your skills:")

if "python" in skills or "machine learning" in skills or "data" in skills:
    category = "Data/ML"

elif "Java" in skills or "javascript" in skills or "SQL" in skills :
    category = "Java Developer"

elif "web" in skills:
    category = "web development"

else:
    category = "Other"

print("Predicted Category:", category)