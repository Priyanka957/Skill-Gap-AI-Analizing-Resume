import streamlit as st
import pdfplumber
import docx
import re
import plotly.graph_objects as go


TECHNICAL_SKILLS = {
    "python", "machine learning", "tensorflow", "data visualization", "sql",
    "computer vision", "java", "c++", "pytorch", "nlp", "deep learning",
    "data analysis", "scikit-learn", "pandas", "numpy", "matplotlib"
}
SOFT_SKILLS = {
    "communication", "teamwork", "leadership", "time management", "problem solving",
    "adaptability", "creativity", "work ethic", "interpersonal skills", "critical thinking"
}


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(file):
    return docx.process(file)


def extract_text(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file.type == "text/plain":
        return file.getvalue().decode("utf-8")
    elif file.type in ["application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        return extract_text_from_docx(file)
    else:
        return ""


def extract_skills(text):
    text_lower = text.lower()
    extracted_technical = set()
    extracted_soft = set()
    for skill in TECHNICAL_SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
            extracted_technical.add(skill.title())
    for skill in SOFT_SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
            extracted_soft.add(skill.title())
    return list(extracted_technical), list(extracted_soft)


def match_percentage(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    matched = set(resume_skills).intersection(set(jd_skills))
    return round(len(matched) / len(set(jd_skills)) * 100, 2)


def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines:
        line_strip = line.strip()
        if line_strip and not re.search(r'(objective|summary|profile|skills|experience|education)', line_strip, re.I):
            return line_strip
    return "Name not found"


def extract_professional_summary(text):
    lines = text.split('\n')
    summary_lines = []
    capture = False
    for line in lines:
        if re.match(r'^(professional summary|summary|profile|objective)', line.strip(), re.I):
            capture = True
            continue
        if capture:
            if line.strip() == "" or re.match(r'^[A-Z ]{3,}$', line.strip()):
                break
            summary_lines.append(line.strip())
    return "\n".join(summary_lines) if summary_lines else "Professional summary not found."

def extract_skills_section(text):
    lines = text.split('\n')
    skills_lines = []
    capture = False
    for line in lines:
        if re.match(r'^(skills|technical skills|skill set)', line.strip(), re.I):
            capture = True
            continue
        if capture:
            if line.strip() == "" or re.match(r'^[A-Z ]{3,}$', line.strip()):
                break
            skills_lines.append(line.strip())
    return "\n".join(skills_lines) if skills_lines else "Skills section not found."


def render_skill_tags(skills):
    for skill in sorted(skills):
        st.markdown(f"<span style='background-color:#e1f5fe; color:#0277bd; padding:5px 12px; margin:3px; border-radius:15px; font-weight:600; display:inline-block'>{skill}</span>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Skill Extraction Interface", layout="wide")

   
    st.markdown("""
        <div style="background-color:#3c8dbc; padding:15px; border-radius:5px; color:white; margin-bottom:15px;">
            <h2>Milestone 2: Skill Extraction using NLP Module (Weeks 3-4)</h2>
            <p style="font-style:italic; color:#d0e6f8;">
                Module: Skill Extraction using NLP - spaCy and BERT-based pipelines - Technical and soft skills identification - Structured skill display
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Skill Extraction Interface")

    
    uploaded_resume = st.sidebar.file_uploader("Upload Resume (txt, pdf, docx)", type=["txt", "pdf", "doc", "docx"])
    uploaded_jd = st.sidebar.file_uploader("Upload Job Description (txt, pdf, docx)", type=["txt", "pdf", "doc", "docx"])
    cols_btn = st.sidebar.columns([1,1])
    refresh = cols_btn[0].button("🔄 Refresh")
    tailor = cols_btn[1].button("✂️ Tailor")

    if uploaded_resume and uploaded_jd and (refresh or True):
        resume_text = extract_text(uploaded_resume)
        jd_text = extract_text(uploaded_jd)

        resume_tech, resume_soft = extract_skills(resume_text)
        jd_tech, jd_soft = extract_skills(jd_text)

        total_resume_skills = len(resume_tech) + len(resume_soft)
        total_jd_skills = len(jd_tech) + len(jd_soft)
        matched_skills = set(resume_tech + resume_soft).intersection(set(jd_tech + jd_soft))

        
        confidence_scores = []
        for skill in resume_tech + resume_soft:
            if skill in matched_skills:
                confidence_scores.append(1.0)
            else:
                confidence_scores.append(0.6)

        avg_confidence = round(sum(confidence_scores) / len(confidence_scores) * 100, 2) if confidence_scores else 0

      
        person_name = extract_name(resume_text)
        prof_summary = extract_professional_summary(resume_text)
        skills_section = extract_skills_section(resume_text)

       
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("#### 📄 Resume Skills")
            if resume_tech:
                st.markdown("**Technical Skills**")
                render_skill_tags(resume_tech)
            if resume_soft:
                st.markdown("**Soft Skills**")
                render_skill_tags(resume_soft)
            if not resume_tech and not resume_soft:
                st.info("No skills found in resume.")

            st.markdown("---")

            st.markdown("#### 📋 Job Description Skills")
            if jd_tech:
                st.markdown("**Technical Skills**")
                render_skill_tags(jd_tech)
            if jd_soft:
                st.markdown("**Soft Skills**")
                render_skill_tags(jd_soft)
            if not jd_tech and not jd_soft:
                st.info("No skills found in job description.")

            st.markdown("---")

            st.markdown("#### ✨ Highlighted Text")

            st.markdown(f"**Name:** {person_name}")
            st.markdown("**Professional Summary:**")
            st.text(prof_summary)
            st.markdown("**Skills:**")
            st.text(skills_section)

        with col2:
            st.markdown("#### 📊 Skill Distribution")
            labels = ["Technical Skills", "Soft Skills"]
            values = [len(resume_tech), len(resume_soft)]
            colors = ['#2E8BC0', '#00A86B']

            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5, marker_colors=colors)])
            fig.update_traces(textinfo="label+value", textfont_size=14)
            fig.update_layout(margin=dict(t=25, b=25, l=10, r=10), height=280)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")

           
            col_a, col_b = st.columns(2)
            col_c, col_d = st.columns(2)
            col_a.metric("Technical Skills", len(resume_tech))
            col_b.metric("Soft Skills", len(resume_soft))
            col_c.metric("Total Skills", total_resume_skills)
            col_d.metric("Avg Confidence", f"{avg_confidence} %")

            st.markdown("---")

            st.markdown("#### 🔍 Detailed Skills")
            for idx, skill in enumerate(sorted(resume_tech + resume_soft)):
                confidence = confidence_scores[idx]
                cols = st.columns([5, 1])
                with cols[0]:
                    st.write(f"**{skill}**")
                    st.progress(confidence)
                with cols[1]:
                    st.markdown("✅" if confidence >= 1.0 else "❌")

    else:
        st.info("Please upload both Resume and Job Description files to perform skill extraction.")

if __name__ == "__main__":
    main()