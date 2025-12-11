text = input("Enter text: ")

words = text.split()
email_found = None

for w in words:
    if "@" in w:         
        email_found = w
        break

if email_found:
    print("Extracted email:", email_found)
else:
    print("No email detected.")
