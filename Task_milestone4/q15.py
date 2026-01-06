import streamlit as st
import pandas as pd

st.title("Resume vs Job Skill Analyzer")

resume = st.text_area("Resume Text")
job = st.text_area("Job Description")

if st.button("Analyze"):
    matched = ["Python", "SQL"]
    missing = ["AWS"]

    st.metric("Skill Match", "66%")

    st.subheader("Matched Skills")
    st.write(matched)

    st.subheader("Missing Skills")
    st.write(missing)

    df = pd.DataFrame({
        "Skill": matched + missing,
        "Status": ["Matched"]*2 + ["Missing"]
    })

    st.bar_chart(df["Status"].value_counts())

    st.download_button(
        "Download Report",
        df.to_csv(index=False),
        "report.csv"
    )
