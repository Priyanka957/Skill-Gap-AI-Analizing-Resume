import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
text = "Skills include: Python, SQL; NLP, and Machine Learning."
doc = nlp(text)
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
skills = ["Python", "SQL", "NLP", "Machine Learning"]
patterns = [nlp(skill) for skill in skills]
matcher.add("SKILLS", patterns)
matches = matcher(doc)
extracted_skills = list(set([doc[start:end].text for _, start, end in matches]))
print(extracted_skills)