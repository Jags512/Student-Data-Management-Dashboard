import pandas as pd

df = pd.read_csv('../data/students.csv')

# Data Cleaning
df.drop_duplicates(inplace=True)

# KPIs
avg_marks = df['marks'].mean()
top_branch = df.groupby('branch')['marks'].mean().idxmax()
attendance_avg = df['attendance'].mean()

print("Average Marks:", avg_marks)
print("Top Performing Branch:", top_branch)
print("Average Attendance:", attendance_avg)

# Save processed data
df.to_csv('../data/processed_students.csv', index=False)
