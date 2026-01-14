import streamlit as st
import plotly.graph_objects as go
import re
from PyPDF2 import PdfReader
from docx import Document

# ================= PAGE CONFIG =================
st.set_page_config(layout="wide")

# ================= FILE READERS =================
def read_txt(file):
    return file.read().decode("utf-8").lower()

def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

def read_docx(file):
    doc = Document(file)
    return " ".join(p.text for p in doc.paragraphs).lower()

def extract_text(uploaded_file):
    # ✅ SAFETY CHECK (FIX)
    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        return read_txt(uploaded_file)
    elif filename.endswith(".pdf"):
        return read_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return read_docx(uploaded_file)
    return ""

# ================= HEADER =================
st.markdown("""
<div style="background-color:#5932EA;padding:16px;border-radius:6px">
<h3 style="color:white;">Milestone 3: Skill Gap Analysis & Similarity Matching (Weeks 5–6)</h3>
<p style="color:white;font-size:14px;">
Dynamic similarity • Skill gap detection • Resume vs JD
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Skill Gap Analysis Interface")

# ================= FILE UPLOAD =================
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload Resume (PDF / DOCX / TXT)",
        type=["pdf", "docx", "txt"]
    )

with col2:
    jd_file = st.file_uploader(
        "Upload Job Description (PDF / DOCX / TXT)",
        type=["pdf", "docx", "txt"]
    )

# ✅ STOP EXECUTION EARLY (FIX)
if resume_file is None or jd_file is None:
    st.warning("Please upload both Resume and Job Description.")
    st.stop()

# ================= TEXT EXTRACTION =================
resume_text = extract_text(resume_file)
jd_text = extract_text(jd_file)

# ================= SKILL LIST =================
SKILLS = [
    "java", "spring boot", "mysql", "sql", "rest",
    "python", "react", "node", "mongodb",
    "communication", "leadership"
]

def extract_skills(text):
    found = set()
    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.add(skill)
    return found

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matched = resume_skills & jd_skills
missing = jd_skills - resume_skills
partial = resume_skills - jd_skills

overall_match = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0

# ================= LAYOUT =================
left, right = st.columns([3, 2])

# ==================================================
# 🔥 DYNAMIC SIMILARITY MATRIX
# ==================================================
with left:
    st.markdown("### Similarity Matrix")

    resume_list = sorted(resume_skills)
    jd_list = sorted(jd_skills)

    if not resume_list or not jd_list:
        st.info("Not enough skills to generate similarity matrix.")
    else:
        fig = go.Figure()

        for r_skill in resume_list:
            for j_skill in jd_list:

                if r_skill == j_skill:
                    score = 0.9
                elif r_skill in j_skill or j_skill in r_skill:
                    score = 0.65
                else:
                    score = 0.35

                color = "green" if score >= 0.8 else "orange" if score >= 0.5 else "red"

                fig.add_trace(go.Scatter(
                    x=[j_skill],
                    y=[r_skill],
                    mode="markers",
                    marker=dict(
                        size=score * 50,
                        color=color,
                        line=dict(color="black", width=1)
                    ),
                    showlegend=False
                ))

        fig.update_layout(
            height=340,
            plot_bgcolor="white",
            margin=dict(l=40, r=40, t=30, b=30),
            xaxis=dict(title="Job Description Skills"),
            yaxis=dict(title="Resume Skills")
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Missing Skills")
    for skill in missing:
        st.markdown(f"• **{skill.title()}**")

# ==================================================
# 📊 OVERVIEW PANEL
# ==================================================
with right:
    st.markdown("### Skill Match Overview")

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    c1.metric("Overall Match", f"{overall_match}%")
    c2.metric("Matched Skills", len(matched))
    c3.metric("Partial Matches", len(partial))
    c4.metric("Missing Skills", len(missing))

    donut = go.Figure(go.Pie(
        labels=["Matched", "Partial", "Missing"],
        values=[len(matched), len(partial), len(missing)],
        hole=0.65,
        marker_colors=["green", "orange", "red"],
        textinfo="none"
    ))

    donut.update_layout(
        height=240,
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=True,
        legend=dict(orientation="h", x=0.5, xanchor="center")
    )

    st.plotly_chart(donut, use_container_width=True)
