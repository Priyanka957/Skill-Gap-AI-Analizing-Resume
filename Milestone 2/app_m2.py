import streamlit as st
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skill Extraction Dashboard", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* Styling for the skill pills */
    .skill-pill {
        background:#E6F4EA;
        color:#256029;
        padding:5px 12px;
        border-radius:15px;
        font-size:12px;
        margin:3px;
        display:inline-block;
        font-weight: bold;
    }
    /* The Green Main Header */
    .main-header {
        background:#3E8E7E;
        padding:16px;
        border-radius:6px;
        color:white;
        margin-bottom:20px;
    }
    /* This CSS forces both containers to have the exact same height */
    [data-testid="stVerticalBlockBorderWrapper"] {
        min-height: 850px !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="main-header">
    <h3 style="margin:0;">Milestone 2: Skill Extraction using NLP Module (Weeks 3–4)</h3>
    <p style="font-size:13px; margin:0;">spaCy & BERT pipelines • Technical & Soft Skills • Structured Display</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
u1, u2 = st.columns(2)
resume_file = u1.file_uploader("Upload Resume (.txt)", ["txt"])
jd_file = u2.file_uploader("Upload Job Description (.txt)", ["txt"])

if resume_file and jd_file:
    # Example Data matching your screenshots
    res_tech_skills = ["python", "sql"]
    res_soft_skills = ["Communication"]
    jd_tech_skills = ["python", "sql", "aws"]
    name, role = "AAVULA PRIYANKA", "Software Engineer"
    conf_score = 95 

    st.markdown("### Skill Extraction Interface")
    
    # Dashboard Layout with two equal columns
    left_col, right_col = st.columns(2)

    # ================= LEFT BOX: RESUME SKILLS =================
    with left_col:
        # st.container(border=True) ensures everything stays INSIDE the white box
        with st.container(border=True):
            st.subheader("Resume Skills")
            tab1, tab2 = st.tabs(["Resume", "Job Description"])
            
            with tab1:
                pills = "".join([f'<span class="skill-pill">{s}</span>' for s in res_tech_skills])
                st.markdown(pills, unsafe_allow_html=True)
            
            with tab2:
                jd_pills = "".join([f'<span class="skill-pill">{s}</span>' for s in jd_tech_skills])
                st.markdown(jd_pills, unsafe_allow_html=True)

            st.markdown("<br><hr>", unsafe_allow_html=True)
            st.subheader("Highlighted Text")
            st.markdown(f"""
                <div style="line-height:4.1;">
                    <b style="color:#3E8E7E; font-size:18px;">{name}</b><br>
                    <span style="color:#555;">{role}</span><br><br>
                    <b>PROFESSIONAL SUMMARY</b><br>
                    <p style="font-size:18px;">To start my career as a {role} in a dynamic organization where I can utilize my technical skills and grow professionally.</p>
                    <b>SKILLS</b><br>
                    <p style="font-size:18px;">{", ".join(res_tech_skills)}</p>
                </div>
            """, unsafe_allow_html=True)

    # ================= RIGHT BOX: SKILL DISTRIBUTION =================
    with right_col:
        with st.container(border=True):
            st.subheader("Skill Distribution")
            
            # Pie Chart logic
            fig = go.Figure(go.Pie(
                labels=["Technical Skills", "Soft Skills"],
                values=[len(res_tech_skills), len(res_soft_skills)],
                hole=0.6,
                marker=dict(colors=["#3E8E7E", "#9ED6C6"]),
                textinfo="none"
            ))
            fig.update_layout(
                height=280, 
                margin=dict(t=10, b=10, l=0, r=0), 
                legend=dict(orientation="v", yanchor="top", y=1, xanchor="right", x=1.1)
            )
            st.plotly_chart(fig, use_container_width=True)

            # Metric Grid matching image_3adc09
            m1, m2 = st.columns(2)
            m1.metric("Technical Skills", len(res_tech_skills))
            m2.metric("Soft Skills", len(res_soft_skills))
            
            m3, m4 = st.columns(2)
            m3.metric("Total Skills", len(res_tech_skills) + len(res_soft_skills))
            m4.metric("Avg Confidence", f"{conf_score}%")

            st.markdown("<br><hr>", unsafe_allow_html=True)
            st.subheader("Detailed Skills")
            for s in res_tech_skills:
                st.write(f"**{s}**")
                st.progress(conf_score / 100)
else:
    st.info("Please upload your Resume and Job Description files to view the dashboard.")