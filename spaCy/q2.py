import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")

doc = nlp("I have experience in Python and SQL.")

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")


patterns = [nlp("Python"),nlp("SQL")]
matcher.add("SKILLS", patterns)
skills=[doc[start:end].text for _,start,end in matcher(doc)]

print(skills)