import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
doc = nlp("python PYTHON python")
matcher = PhraseMatcher(nlp.vocab,attr="LOWER")
matcher.add("SKILLS",[nlp("Python")])
print([doc[start:end].text for _,start, end in matcher(doc)])