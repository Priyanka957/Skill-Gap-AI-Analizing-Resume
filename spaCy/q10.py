import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
paragraph = "Python, Python, SQL, NLP, NLP, Machine Learning"
doc3 = nlp(paragraph)
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
skills = ["Python", "SQL", "NLP", "Machine Learning"]
patterns = [nlp(skill) for skill in skills]
matcher.add("SKILLS", patterns)
matches = matcher(doc3)
unique_skills = list(set([doc3[start:end].text.lower() for _, start, end in matches]))
print(unique_skills)