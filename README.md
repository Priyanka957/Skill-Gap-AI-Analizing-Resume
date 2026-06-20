# 💡 Skill Gap AI Analyzer – Resume & Job Description Analyzer

An AI-powered web application that analyzes resumes and job descriptions to identify matching skills, missing skills, and provide intelligent skill-gap recommendations using NLP and data analysis.

---

## 🚀 Overview

Skill Gap AI Analyzer helps users understand how well their resume matches a job description. It extracts key skills, compares them, and generates insights to improve job readiness.

The system provides:
- Skill extraction from resumes
- Job description parsing
- Skill matching and gap analysis
- Interactive dashboard for visualization

---

## ✨ Key Features

📄 Resume parsing (PDF/DOCX support)  
🧠 NLP-based skill extraction  
🔍 Job description analysis  
📊 Skill matching & gap identification  
📈 Interactive visual dashboards  
📉 Visual representation of missing vs matched skills  
📥 Downloadable analysis reports  

---

## 🛠️ Tech Stack

### Frontend
- Streamlit
- Plotly
- Matplotlib

### Backend / Processing
- Python
- NLP (spaCy / Regex)
- Pandas
- PDFPlumber
- python-docx

### Visualization
- Plotly Express
- Graph Objects

---

## 📂 Project Structure
AI-Resume-Analyzer/
│
├── Final Project/
│ ├── app_final.py
│ ├── requirements.txt
│ ├── skill_gap_report.pdf
│ └── output files
│
├── datasets/
├── models/
├── utils/
└── README.md



---

⚙️ Setup Instructions

1. Clone Repository

git clone https://github.com/Priyanka957/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer


2. Install Dependencies
pip install -r requirements.txt

3. Run Application
streamlit run "Final Project/app_final.py"

🌐 Live Demo

👉 https://skill-gap-ai-analyzer.streamlit.app/

📊 How It Works

Upload Resume (PDF/DOCX)
Enter Job Description
Extract skills using NLP
Compare resume skills with job requirements
Generate results:
Matched Skills
Missing Skills
Skill Gap Score
Visual Charts

👩‍💻 Author

Aavula Priyanka
GitHub: https://github.com/Priyanka957
Live Demo: https://skill-gap-ai-analyzer.streamlit.app/