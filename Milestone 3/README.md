# Infosys Springboard

## Milestone 3: Skill Matching & Gap Analysis using NLP

---

## Project Overview

This project is developed as part of the **Infosys Springboard Individual Project**.

**Milestone 3** extends the skill extraction system developed in Milestone 2 by introducing **skill matching between resumes and job descriptions**. The system analyzes both inputs, compares extracted skills, identifies matches and gaps, and presents the results in a clear and visual manner using NLP techniques.

---

## Milestone 3 Objectives

* Compare resume skills with job description skills
* Identify matched and missing skills
* Perform skill gap analysis
* Calculate skill match percentage
* Visualize results for better interpretation
* Enhance usability and clarity of outputs

---

## Features Implemented

* Resume vs Job Description skill comparison
* Matched skills identification
* Missing skill detection
* Skill match percentage calculation
* Interactive and structured output display

---

## Technologies Used

* Python 3
* Streamlit
* Natural Language Processing (NLP)
* spaCy
* BERT
* Plotly
* Custom CSS
* Git & GitHub

---

## Project Structure

```
Milestone_3/
│
├── data/
│   ├── job_description2.txt      # Job description input file
│   └── resume2.txt               # Resume input file
│
├── app_m3.py                     # Main Streamlit application
├── outputscreenshot.jpeg         # Output screenshot
└── README.md                     # Project documentation
```

---

## How to Run the Application

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```
2. Navigate to the Milestone 3 directory:

   ```bash
   cd Milestone_3
   ```
3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:

   ```bash
   streamlit run app_m3.py
   ```

---

## Output

* Displays matched skills between resume and job description
* Shows missing skills required for the job role
* Provides overall skill match percentage
* Visual representations for easier analysis

---

## Conclusion

Milestone 3 successfully implements a **skill matching and gap analysis system**, helping users evaluate how well a resume aligns with a given job description. This milestone makes the project more practical and career-oriented.

---

