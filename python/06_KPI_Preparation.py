import pandas as pd

# ==========================
# Load Cleaned Dataset
# ==========================

file_path = "Data/cleaned/Cleaned_Education_Data.xlsx"
df = pd.read_excel(file_path)

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

# ==========================
# Convert Feedback Rating to Numeric
# ==========================

df["Feedback_Rating"] = pd.to_numeric(df["Feedback_Rating"], errors="coerce")

# ==========================
# KPI Calculations
# ==========================

total_students = len(df)

average_quiz_score = df["Quiz_Score"].mean()

average_time_spent = df["Time_Spent_Min"].mean()

average_feedback_rating = df["Feedback_Rating"].mean()

completed_students = (df["Completion_Status"] == "Completed").sum()

completion_rate = (completed_students / total_students) * 100

# ==========================
# Display KPI Results
# ==========================

print("\n========== KPI DASHBOARD ==========")

print(f"Total Students          : {total_students}")

print(f"Average Quiz Score      : {average_quiz_score:.2f}")

print(f"Average Time Spent      : {average_time_spent:.2f} Minutes")

print(f"Average Feedback Rating : {average_feedback_rating:.2f}")

print(f"Completed Students      : {completed_students}")

print(f"Completion Rate         : {completion_rate:.2f}%")

# ==========================
# Course-wise KPI Summary
# ==========================

course_summary = df.groupby("Course").agg({
    "Quiz_Score": "mean",
    "Time_Spent_Min": "mean",
    "Feedback_Rating": "mean"
}).round(2)

print("\n========== Course-wise KPI ==========")
print(course_summary)

# ==========================
# Save KPI Summary
# ==========================

output_path = "Data/cleaned/KPI_Summary.xlsx"

course_summary.to_excel(output_path)

print("\nKPI Summary saved successfully!")
print("Output File:", output_path)