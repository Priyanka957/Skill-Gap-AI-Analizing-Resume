import streamlit as st

matched_skills = ["Python", "SQL", "Streamlit"]
missing_skills = ["Docker", "AWS"]

st.subheader("Matched Skills")
st.write(matched_skills)

st.subheader("Missing Skills")
st.write(missing_skills)
