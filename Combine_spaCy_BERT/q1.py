


import spacy
from spacy.matcher import PhraseMatcher

resume_text = """
I have experience in Python, Machine Learning, SQL, HTML,
and teamwork and communication.
"""

nlp = spacy.load("en_core_web_sm")
doc = nlp(resume_text)

skills = ["python", "machine learning", "sql", "html"]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp(skil) for skil in skills]
matcher.add("SKILLS", patterns)

matches = [doc[start:end].text for _, start, end in matcher(doc)]
print(matches)