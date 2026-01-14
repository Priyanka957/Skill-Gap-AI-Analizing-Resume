import streamlit as st
import pdfplumber
from docx import Document
import re
import matplotlib.pyplot as plt


TECHNICAL_SKILLS = [
    "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
    "Keras", "Data Analysis", "SQL", "Power BI", "Excel", "NLP",
    "scikit-learn", "Tableau", "Regression Analysis",
    "Statistics", "Unix"
]

SOFT_SKILLS = [
    "Communication", "Leadership", "Teamwork",
    "Problem Solving", "Time Management", "Critical Thinking"
]


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_text(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file)
    else:
        return file.read().decode("utf-8")


def extract_name(text):
    for line in text.split("\n")[:5]:
        if 1 < len(line.split()) <= 4:
            return line.strip()
    return "Candidate"

def extract_professional_summary(text):
    clean_text = re.sub(r"\n{2,}", "\n", text)
    match = re.search(
        r"(summary|professional summary|profile|about me|career objective)(.*?)(skills|experience|education|projects)",
        clean_text, re.IGNORECASE | re.DOTALL
    )
    if match:
        return match.group(2).strip()

    lines = [l.strip() for l in clean_text.split("\n") if len(l.strip()) > 40]
    return " ".join(lines[:3]) if lines else "Experienced professional with diverse skills."

def extract_skills(text):
    skills = []

    for skill in TECHNICAL_SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            skills.append({
                "name": skill,
                "type": "Technical",
                "confidence": 85
            })

    for skill in SOFT_SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            skills.append({
                "name": skill,
                "type": "Soft",
                "confidence": 75
            })

    return skills


def skill_distribution_chart(tech, soft):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(
        [tech, soft],
        labels=["Technical Skills", "Soft Skills"],
        startangle=90,
        wedgeprops=dict(width=0.4)
    )
    ax.axis("equal")
    return fig


def main():
    st.set_page_config(layout="wide")

    
    st.markdown("""
    <style>
    .header {
        background:#4caf50;
        padding:14px;
        color:white;
        font-size:22px;
        font-weight:600;
        border-radius:6px;
        margin-bottom:12px;
    }
    .box {
        background:white;
        border-radius:8px;
        padding:18px;
        box-shadow:0 4px 10px rgba(0,0,0,0.08);
        margin-bottom:14px;
    }
    .tag {
        background:#e0f2f1;
        color:#00796b;
        padding:6px 14px;
        border-radius:20px;
        margin:4px;
        display:inline-block;
        font-size:13px;
        font-weight:500;
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown(
        '<div class="header">Milestone 2: Skill Extraction using NLP Module</div>',
        unsafe_allow_html=True
    )

    
    resume_file = st.file_uploader("Upload Resume", ["pdf", "docx", "txt"])
    jd_file = st.file_uploader("Upload Job Description", ["pdf", "docx", "txt"])

    if not resume_file or not jd_file:
        st.info("Please upload both Resume and Job Description.")
        return

    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    
    selected_source = st.radio(
        "Select Skill Source",
        ["Resume Skills", "Job Description Skills"],
        horizontal=True
    )

    if selected_source == "Resume Skills":
        active_text = resume_text
        active_skills = resume_skills
    else:
        active_text = jd_text
        active_skills = jd_skills

    tech_skills = [s for s in active_skills if s["type"] == "Technical"]
    soft_skills = [s for s in active_skills if s["type"] == "Soft"]

    total_skills = len(active_skills)
    avg_conf = (
        round(sum(s["confidence"] for s in active_skills) / total_skills, 1)
        if total_skills else 0
    )

    col1, col2 = st.columns([2.5, 1])

    
    with col1:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader(selected_source)
        for s in active_skills:
            st.markdown(f"<span class='tag'>{s['name']}</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("Highlighted Text")
        st.markdown(f"**👤 Name:** {extract_name(active_text)}")
        st.markdown("**🧑‍💼 Professional Summary:**")
        st.write(extract_professional_summary(active_text))

        st.markdown("**🛠 Skills:**")
        for s in active_skills:
            st.markdown(f"- {s['name']} ({s['type']})")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("Skill Distribution")

        fig = skill_distribution_chart(len(tech_skills), len(soft_skills))
        st.pyplot(fig)

        st.metric("Technical Skills", len(tech_skills))
        st.metric("Soft Skills", len(soft_skills))
        st.metric("Total Skills", total_skills)
        st.metric("Avg Confidence", f"{avg_conf}%")

        # 🔽 DETAILED SKILLS BELOW PIE CHART
        st.markdown("### 🔍 Detailed Skills")
        for skill in active_skills:
            st.markdown(f"**{skill['name']} ({skill['type']})**")
            st.progress(skill["confidence"] / 100)

        st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
