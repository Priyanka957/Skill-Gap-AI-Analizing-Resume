import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Skill": ["AWS", "Docker"],
    "Status": ["Missing", "Missing"]
})

csv = df.to_csv(index=False)

st.download_button(
    "Download Skill Gap Report",
    csv,
    "skill_gap.csv",
    "text/csv"
)
