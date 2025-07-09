import streamlit as st
import pandas as pd

# Load reshaped grade file
df = pd.read_csv("Biology_Grades_Reshaped.csv")

st.set_page_config(page_title="Biology Grade Dashboard", layout="wide")
st.title("📚 Biology Grading Dashboard")

# Sidebar filter
student = st.sidebar.selectbox("🔍 Select Student", df["full_name"].unique())
category = st.sidebar.selectbox("📂 Select Category", df["category"].unique())

filtered = df[(df["full_name"] == student) & (df["category"] == category)]

# Show assessment table
st.subheader(f"Assessments for {student} - {category}")
st.dataframe(filtered)

# Bar chart of GB1 grade distribution
st.subheader("🎓 GB1 Grade Distribution")
st.bar_chart(filtered["gb1_grade"].value_counts())

# Download CSV
st.download_button("📥 Download Student Data", filtered.to_csv(index=False), file_name=f"{student}_grades.csv")
