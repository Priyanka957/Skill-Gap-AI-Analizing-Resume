import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "Category": ["Matched", "Missing"],
    "Count": [3, 2]
})

st.bar_chart(data.set_index("Category"))
