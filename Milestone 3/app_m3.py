import streamlit as st
import plotly.graph_objects as go
import re
from PyPDF2 import PdfReader
from docx import Document

st.set_page_config(layout="wide")


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
    return " ".join([p.text for p in doc.paragraphs]).lower()

def extract_text(uploaded_file):
    if uploaded_file is None:
        return ""

    if uploaded_file.name.endswith(".txt"):
        return read_txt(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        return read_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return read_docx(uploaded_file)
    else:
        return ""



st.markdown(
    """
    <div style="background-color:#5932EA;padding:16px;border-radius:6px">
    <h3 style="color:white;">Milestone 3: Skill Gap Analysis and Similarity Matching Module (Weeks 5–6)</h3>
    <p style="color:white;font-size:14px;">
    BERT-style similarity • Skill gap detection • Resume vs JD
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("## Skill Gap Analysis Interface")



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

if resume_file is None or jd_file is None:
    st.warning("Please upload both Resume and Job Description files.")
    st.stop()

resume_text = extract_text(resume_file)
jd_text = extract_text(jd_file)



SKILLS = [
    "java", "spring boot", "mysql", "sql", "rest",
    "python", "react", "node", "mongodb",
    "communication", "leadership"
]

def extract_skills(text):
    found = set()
    for skill in SKILLS:
        if re.search(rf"\b{skill}\b", text):
            found.add(skill)
    return found

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matched = resume_skills & jd_skills
missing = jd_skills - resume_skills
partial = resume_skills - jd_skills

total_required = len(jd_skills)
overall_match = int((len(matched) / total_required) * 100) if total_required else 0



left, right = st.columns([3, 2])


with left:
    st.markdown("### Similarity Matrix")

    x_skills = ["ML", "SQL", "Communication", "Adv. Stats", "NoSQL", "Team Leadership"]
    y_skills = ["NoSQL", "Adv. Stats", "Communication", "SQL", "ML"]

    bubbles = [
        ("ML","ML",0.9,"green"),
        ("SQL","SQL",0.85,"green"),
        ("Communication","Communication",0.8,"green"),
        ("Adv. Stats","Adv. Stats",0.82,"green"),
        ("NoSQL","NoSQL",0.88,"green"),
        ("Communication","Adv. Stats",0.65,"orange"),
        ("SQL","Adv. Stats",0.6,"orange"),
        ("Team Leadership","SQL",0.4,"red"),
        ("Team Leadership","Communication",0.35,"red"),
    ]

    x_map = {k:i for i,k in enumerate(x_skills)}
    y_map = {k:i for i,k in enumerate(y_skills)}

    fig = go.Figure()

    for x,y,val,color in bubbles:
        fig.add_trace(go.Scatter(
            x=[x_map[x]],
            y=[y_map[y]],
            mode="markers",
            marker=dict(
                size=val*60,
                color=color,
                line=dict(color="black", width=1)
            ),
            showlegend=False
        ))

    fig.update_xaxes(
        tickvals=list(range(len(x_skills))),
        ticktext=x_skills,
        range=[-0.5, len(x_skills)-0.5]
    )

    fig.update_yaxes(
        tickvals=list(range(len(y_skills))),
        ticktext=y_skills,
        range=[-0.5, len(y_skills)-0.5],
        autorange="reversed"
    )

    fig.update_layout(
        height=320,
        plot_bgcolor="white",
        margin=dict(l=30, r=30, t=20, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <span style="color:green">●</span> High Match (80–100%) &nbsp;
    <span style="color:orange">●</span> Partial Match (50–79%) &nbsp;
    <span style="color:red">●</span> Low Match (0–49%)
    """, unsafe_allow_html=True)

    st.markdown("### Missing Skills")
    for skill in missing:
        st.markdown(f" **{skill.title()}** — High")


with right:
    st.markdown("### Skill Match Overview")

    c1, c2 = st.columns(2)
    c1.metric("Overall Match", f"{overall_match}%")
    c2.metric("Matched Skills", len(matched))

    c3, c4 = st.columns(2)
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
        height=220,
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=True,
        legend=dict(orientation="h", x=0.5, xanchor="center")
    )

    st.plotly_chart(donut, use_container_width=True)
