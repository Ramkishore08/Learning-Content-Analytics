import pandas as pd

file_path = "Data/cleaned/Cleaned_Education_Data.xlsx"
df = pd.read_excel(file_path)

print(df.head())
#Overall Performance Metrics
print("\nAverage Quiz Score:", df["Quiz_Score"].mean())
print("Average Time Spent:", df["Time_Spent_Min"].mean())
print("Average Feedback Rating:", df["Feedback_Rating"].mean())

# Course Performance Analysis
course_perf = df.groupby("Course")["Quiz_Score"].mean().sort_values(ascending=False)
print("\nCourse Performance:\n", course_perf)

#Visualize Best Courses
import matplotlib.pyplot as plt

course_perf.plot(kind="bar")
plt.title("Average Quiz Score by Course")
plt.xlabel("Course")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.show()

#Engagement Analysis
engagement = df.groupby("Content_Type")["Time_Spent_Min"].mean().sort_values(ascending=False)
print("\nEngagement by Content Type:\n", engagement)

#Engagement Visualization
engagement.plot(kind="bar", color="orange")
plt.title("Engagement by Content Type")
plt.ylabel("Time Spent")
plt.xticks(rotation=45)
plt.show()

#Relationship Analysis
plt.scatter(df["Time_Spent_Min"], df["Quiz_Score"])
plt.title("Time Spent vs Quiz Score")
plt.xlabel("Time Spent")
plt.ylabel("Quiz Score")
plt.show()