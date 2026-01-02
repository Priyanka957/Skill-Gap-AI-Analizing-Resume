import spacy
nlp = spacy.load("en_core_web_sm")
resume_text="I worked at InternPe as Intern"

doc = nlp(resume_text)
for ent in doc.ents:
    print(ent.text,ent.label_)