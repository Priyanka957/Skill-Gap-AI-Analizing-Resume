job_title = input("Enter job title: ")
clean_title = ""
for ch in job_title:
    if ch.isalnum() or ch.isspace():
        clean_title += ch
normalized = clean_title.title()

print("Normalized Job Title:", normalized)