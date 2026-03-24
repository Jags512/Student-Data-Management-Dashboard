import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('../data/students.csv')

st.title("📊 Student Data Dashboard")

# KPIs
st.metric("Average Marks", round(df['marks'].mean(), 2))
st.metric("Average Attendance", round(df['attendance'].mean(), 2))

# Marks by Branch
st.subheader("Marks by Branch")
branch_marks = df.groupby('branch')['marks'].mean()
st.bar_chart(branch_marks)

# Attendance by Year
st.subheader("Attendance by Year")
year_attendance = df.groupby('year')['attendance'].mean()
st.line_chart(year_attendance)

# Raw Data
st.subheader("Raw Data")
st.write(df)
