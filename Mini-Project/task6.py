
resume_text = input("Enter the resume paragraph:\n")

skill = input("Enter the skill to check: ").lower()

resume_lower = resume_text.lower()

count = resume_lower.count(skill)

print(f"'{skill}' appears {count} times.")
