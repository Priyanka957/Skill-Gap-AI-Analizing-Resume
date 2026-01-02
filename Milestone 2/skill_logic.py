import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from cleaner import clean_text

nlp = spacy.load("en_core_web_sm")
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

TECHNICAL_SKILLS = [
    "python", "machine learning", "deep learning", "sql",
    "tensorflow", "pandas", "numpy", "cloud computing"
]

SOFT_SKILLS = [
    "communication", "teamwork", "leadership",
    "problem solving", "time management"
]

ALL_SKILLS = TECHNICAL_SKILLS + SOFT_SKILLS


def extract_spacy_skills(text):
    doc = nlp(text)
    skills = set()
    for chunk in doc.noun_chunks:
        for skill in ALL_SKILLS:
            if skill in chunk.text.lower():
                skills.add(skill)
    return list(skills)


def extract_bert_skills(text, threshold=0.6):
    sentences = text.split(".")
    sent_emb = bert_model.encode(sentences)
    skill_emb = bert_model.encode(ALL_SKILLS)

    similarity = cosine_similarity(sent_emb, skill_emb)
    skills = set()

    for i in range(len(sentences)):
        for j in range(len(ALL_SKILLS)):
            if similarity[i][j] > threshold:
                skills.add(ALL_SKILLS[j])
    return list(skills)


def extract_skills(text):
    text = clean_text(text)
    skills = set(extract_spacy_skills(text) + extract_bert_skills(text))
    return {
        "all": list(skills),
        "technical": [s for s in skills if s in TECHNICAL_SKILLS],
        "soft": [s for s in skills if s in SOFT_SKILLS]
    }


def compare_skills(resume_text, jd_text):
    resume = extract_skills(resume_text)
    jd = extract_skills(jd_text)

    return {
        "resume": resume,
        "jd": jd,
        "matched": list(set(resume["all"]) & set(jd["all"])),
        "missing": list(set(jd["all"]) - set(resume["all"])),
        "extra": list(set(resume["all"]) - set(jd["all"]))
    }