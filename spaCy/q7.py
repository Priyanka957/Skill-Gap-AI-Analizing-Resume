import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Good communication and teamwork skills")
soft_skills = ["communication","teamwork"]
found = [t.text for t in doc if t.text.lower() in soft_skills]
print(found)
