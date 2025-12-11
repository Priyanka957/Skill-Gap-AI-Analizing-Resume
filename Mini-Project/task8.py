
programming_languages = {"python", "java", "c++", "c#", "javascript"}
databases = {"sql", "postgresql", "sqlite", "mongodb" }
frameworks = {"django", "flask", "react", "angular", "vue", "spring", "laravel", "fastapi"}


user_input = input("Enter a list of tools/technologies: ")

tools = [t.strip().lower() for t in user_input.split(",")]

lang_count = 0
db_count = 0
fw_count = 0

for tool in tools:
    if tool in programming_languages:
        lang_count += 1
    elif tool in databases:
        db_count += 1
    elif tool in frameworks:
        fw_count += 1
        
print("Programming Languages:", lang_count)
print("Databases:", db_count)
print("Frameworks:", fw_count)
