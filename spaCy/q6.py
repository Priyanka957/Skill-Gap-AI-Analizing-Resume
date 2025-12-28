import spacy
from spacy.matcher import PhraseMatcher
PhraseMatcher
nlp = spacy.load("en_core_web_sm")

doc = nlp("Experience in Python,NLP,and Machine Learning with SQL.")
skills = ["Python","NLP","Machine Learning","SQL"]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add("SKILLS", [nlp(skill) for skill in skills])

found=[doc[start:end].text for _,start,end in matcher(doc)]

print(found)