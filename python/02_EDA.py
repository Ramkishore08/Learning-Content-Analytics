import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "Data/cleaned/Cleaned_Education_Data.xlsx"
df = pd.read_excel(file_path)

# Basic check
print(df.head())
print(df.info())

# --------------------------
# EDA STARTS HERE
# --------------------------

print(df.describe())

# Age distribution
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.show()

# Course popularity
sns.countplot(x="Course", data=df)
plt.xticks(rotation=45)
plt.show()

# Time vs Score
plt.scatter(df["Time_Spent_Min"], df["Quiz_Score"])
plt.title("Time vs Score")
plt.show()