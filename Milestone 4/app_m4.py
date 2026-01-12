import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
import PyPDF2
import docx


def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.type == "text/plain":
        text = file.read().decode("utf-8")
    else:
        doc = docx.Document(file)
        for p in doc.paragraphs:
            text += p.text + " "
    return text.lower()


SKILLS = ["Python", "Machine Learning", "SQL", "AWS"]


st.set_page_config(page_title="Skill Gap Analysis", layout="wide")

st.markdown("""
<div style="background:#1e3a8a;padding:18px;border-radius:8px;color:white;">
    <h3 style="margin:0;">Milestone 4: Dashboard & Report Export Module</h3>
    <p style="margin:0;font-size:14px;">Skill Gap Analysis • Role View • PDF & CSV Reports</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Skill Gap Analysis Dashboard")


st.markdown("### 📄 Upload Resume & Job Description")
u1, u2 = st.columns(2)

with u1:
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "txt", "doc", "docx"])
with u2:
    jd_file = st.file_uploader("Upload Job Description", type=["pdf", "txt", "doc", "docx"])

if resume_file and jd_file:

    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    resume_scores = []
    jd_scores = []
    matched, partial, missing = [], [], []

    for skill in SKILLS:
        r = skill.lower() in resume_text
        j = skill.lower() in jd_text

        if r and j:
            resume_scores.append(85)
            jd_scores.append(90)
            matched.append(skill)
        elif r or j:
            resume_scores.append(55)
            jd_scores.append(80)
            partial.append(skill)
        else:
            resume_scores.append(20)
            jd_scores.append(70)
            missing.append(skill)

    overall_match = int(((len(matched) + 0.5 * len(partial)) / len(SKILLS)) * 100)

    df_skills = pd.DataFrame({
        "Skill": SKILLS,
        "Resume Skill %": resume_scores,
        "Job Requirement %": jd_scores
    })

    skill_comparison = dict(zip(SKILLS, resume_scores))

    
    c1, c2, c3 = st.columns(3)

    c1.markdown(f"""
    <div style="background:#e0ecff;padding:20px;border-radius:10px;text-align:center;">
    <h2 style="color:#1d4ed8;margin:0;">{overall_match}%</h2>
    <p>Overall Match</p>
    </div>
    """, unsafe_allow_html=True)

    c2.markdown(f"""
    <div style="background:#dcfce7;padding:20px;border-radius:10px;text-align:center;">
    <h2 style="color:#166534;margin:0;">{len(matched)}</h2>
    <p>Matched Skills</p>
    </div>
    """, unsafe_allow_html=True)

    c3.markdown(f"""
    <div style="background:#fee2e2;padding:20px;border-radius:10px;text-align:center;">
    <h2 style="color:#991b1b;margin:0;">{len(missing)}</h2>
    <p>Missing Skills</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)

    c5.markdown(f"""
    <div style="background:#fef9c3;padding:20px;border-radius:10px;text-align:center;">
    <h2 style="color:#a16207;margin:0;">{len(partial)}</h2>
    <p>Partial Matching Skills</p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([3, 1])

    
    with left:
        st.markdown("### 📈 Skill Match Overview")

        fig = go.Figure()
        fig.add_bar(x=df_skills["Skill"], y=df_skills["Resume Skill %"], name="Resume", marker_color="#2563eb")
        fig.add_bar(x=df_skills["Skill"], y=df_skills["Job Requirement %"], name="Job Requirement", marker_color="#22c55e")
        fig.update_layout(barmode="group", height=350, yaxis_title="Percentage")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### ⚖️ Skill Comparison")
        for skill, value in skill_comparison.items():
            st.markdown(f"**{skill}**")
            st.progress(value / 100)

        st.markdown("### 🎯 Key Skill Match Percentages")
        k1, k2, k3, k4 = st.columns(4)

        def skill_circle(col, skill, percent):
            if percent >= 80:
                bg, fg = "#dcfce7", "#166534"
            elif percent >= 50:
                bg, fg = "#fef9c3", "#a16207"
            else:
                bg, fg = "#fee2e2", "#991b1b"

            col.markdown(f"""
            <div style="background:{bg};width:80px;height:80px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;margin:auto;">
            <b style="color:{fg};font-size:22px;">{percent}%</b>
            </div>
            <p style="text-align:center;margin-top:6px;">{skill}</p>
            """, unsafe_allow_html=True)

        for col, s, v in zip([k1, k2, k3, k4], SKILLS, resume_scores):
            skill_circle(col, s, v)

    
    with right:
        st.markdown("### 👤 Role View")
        st.radio("", ["Job Seeker", "Recruiter"], horizontal=True)

        radar = go.Figure()
        radar.add_trace(go.Scatterpolar(
            r=resume_scores + [resume_scores[0]],
            theta=SKILLS + [SKILLS[0]],
            fill="toself",
            name="Current Profile",
            line_color="#2563eb"
        ))
        radar.add_trace(go.Scatterpolar(
            r=jd_scores + [jd_scores[0]],
            theta=SKILLS + [SKILLS[0]],
            fill="toself",
            name="Job Requirement",
            line_color="#22c55e"
        ))
        radar.update_layout(polar=dict(radialaxis=dict(range=[0, 100])), height=300)
        st.plotly_chart(radar, use_container_width=True)

        st.markdown("### 🚀 Upskilling Recommendations")
        for skill in missing + partial:
            st.warning(f"Improve **{skill}** through courses and hands-on projects")

   
    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Skill Gap Analysis Report", ln=True, align="C")
        pdf.ln(8)

        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 8, f"Overall Match: {overall_match}%", ln=True)
        pdf.cell(0, 8, f"Matched Skills: {len(matched)}", ln=True)
        pdf.cell(0, 8, f"Partial Matching Skills: {len(partial)}", ln=True)
        pdf.cell(0, 8, f"Missing Skills: {len(missing)}", ln=True)
        pdf.ln(5)

        for _, row in df_skills.iterrows():
            pdf.cell(
                0, 8,
                f"{row['Skill']} - Resume {row['Resume Skill %']}% | Job {row['Job Requirement %']}%",
                ln=True
            )

        return pdf.output(dest="S").encode("latin-1")

  
    st.markdown("---")
    p1, p2 = st.columns(2)

    with p1:
        st.download_button("Download PDF Report", generate_pdf(), "SkillGapReport.pdf")

    with p2:
        st.download_button("Download CSV Report", df_skills.to_csv(index=False), "SkillGapReport.csv")

else:
    st.info("Please upload both Resume and Job Description to generate analysis")
