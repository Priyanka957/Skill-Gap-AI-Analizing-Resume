import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Skill": ["Python", "SQL", "AWS"],
    "Similarity Score": [0.95, 0.88, 0.40]
})

st.table(df)
