import streamlit as st
import plotly.graph_objects as go
import os
import re

st.set_page_config(layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

RESUME_PATH = os.path.join(DATA_DIR, "resume2.txt")
JD_PATH = os.path.join(DATA_DIR, "job_description2.txt")


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().lower()
    except:
        return ""

resume_text = read_file(RESUME_PATH)
jd_text = read_file(JD_PATH)

if not resume_text or not jd_text:
    st.error("resume2.txt or job_description2.txt not found in /data folder")
    st.stop()


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
        range=[-0.5,len(x_skills)-0.5]
    )

    fig.update_yaxes(
        tickvals=list(range(len(y_skills))),
        ticktext=y_skills,
        range=[-0.5,len(y_skills)-0.5],
        autorange="reversed"
    )

    fig.update_layout(
        height=320,
        plot_bgcolor="white",
        margin=dict(l=30,r=30,t=20,b=20)
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
        labels=["Matched","Partial","Missing"],
        values=[len(matched), len(partial), len(missing)],
        hole=0.65,
        marker_colors=["green","orange","red"],
        textinfo="none"
    ))

    donut.update_layout(
        height=220,
        margin=dict(t=10,b=10,l=10,r=10),
        showlegend=True,
        legend=dict(orientation="h", x=0.5, xanchor="center")
    )

    st.plotly_chart(donut, use_container_width=True)
