import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF

# DATA (FROM MILESTONE 3 OUTPUT)

overall_match = 50
matched_skills = 2
missing_skills = 2

skills_data = {
    "Skill": ["Python", "Machine Learning", "SQL", "AWS"],
    "Resume Skill %": [90, 75, 40, 35],
    "Job Requirement %": [95, 85, 80, 75]
}
df_skills = pd.DataFrame(skills_data)

key_skills = {
    "Python": 90,
    "Machine Learning": 75,
    "SQL": 40,
    "AWS": 35
}

skill_comparison = {
    "Python": 90,
    "Machine Learning": 75,
    "SQL": 40,
    "AWS": 35
}

upskill_recommendations = [
    ("AWS Cloud Basics", "Learn EC2, S3, IAM and deploy a sample project"),
    ("Advanced SQL", "Practice joins, subqueries, indexing and performance tuning"),
]

radar_categories = ["Technical", "Soft Skills", "Experience", "Education", "Certifications"]

radar_job_seeker = [70, 65, 60, 75, 50]
radar_job_requirement = [85, 70, 75, 80, 65]



st.set_page_config(page_title="Skill Gap Analysis", layout="wide")


st.markdown("""
<div style="background:#1e3a8a;padding:18px;border-radius:8px;color:white;">
    <h3 style="margin:0;">Milestone 4: Dashboard & Report Export Module</h3>
    <p style="margin:0;font-size:14px;">Skill Gap Analysis • Role View • PDF & CSV Reports</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Skill Gap Analysis Dashboard")


c1, c2, c3 = st.columns(3)

c1.markdown(f"""
<div style="background:#e0ecff;padding:20px;border-radius:10px;text-align:center;">
<h2 style="color:#1d4ed8;margin:0;">{overall_match}%</h2>
<p>Overall Match</p>
</div>
""", unsafe_allow_html=True)

c2.markdown(f"""
<div style="background:#dcfce7;padding:20px;border-radius:10px;text-align:center;">
<h2 style="color:#166534;margin:0;">{matched_skills}</h2>
<p>Matched Skills</p>
</div>
""", unsafe_allow_html=True)

c3.markdown(f"""
<div style="background:#fee2e2;padding:20px;border-radius:10px;text-align:center;">
<h2 style="color:#991b1b;margin:0;">{missing_skills}</h2>
<p>Missing Skills</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([3, 1])


with left:
    st.markdown("### 📈 Skill Match Overview")

    fig = go.Figure()
    fig.add_bar(
        x=df_skills["Skill"],
        y=df_skills["Resume Skill %"],
        name="Resume",
        marker_color="#2563eb"
    )
    fig.add_bar(
        x=df_skills["Skill"],
        y=df_skills["Job Requirement %"],
        name="Job Requirement",
        marker_color="#22c55e"
    )

    fig.update_layout(
        barmode="group",
        yaxis_title="Percentage",
        height=350
    )

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

    skill_circle(k1, "Python", 90)
    skill_circle(k2, "Machine Learning", 75)
    skill_circle(k3, "SQL", 40)
    skill_circle(k4, "AWS", 35)


with right:
    st.markdown("### 👤 Role View")

    role = st.radio("", ["Job Seeker", "Recruiter"], horizontal=True)

    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=radar_job_seeker + [radar_job_seeker[0]],
        theta=radar_categories + [radar_categories[0]],
        fill="toself",
        name="Current Profile",
        line_color="#2563eb"
    ))

    radar.add_trace(go.Scatterpolar(
        r=radar_job_requirement + [radar_job_requirement[0]],
        theta=radar_categories + [radar_categories[0]],
        fill="toself",
        name="Job Requirement",
        line_color="#22c55e"
    ))

    radar.update_layout(
        polar=dict(radialaxis=dict(range=[0, 100])),
        height=300
    )

    st.plotly_chart(radar, use_container_width=True)

    st.markdown("### 🚀 Upskilling Recommendations")
    for title, desc in upskill_recommendations:
        st.warning(f"**{title}**  \n{desc}")


def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Skill Gap Analysis Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Overall Match: {overall_match}%", ln=True)
    pdf.cell(0, 8, f"Matched Skills: {matched_skills}", ln=True)
    pdf.cell(0, 8, f"Missing Skills: {missing_skills}", ln=True)
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
