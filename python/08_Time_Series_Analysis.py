import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

file_path = "Data/cleaned/Segmented_Data.xlsx"

df = pd.read_excel(file_path)

# ==========================================
# Display Dataset
# ==========================================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

# ==========================================
# Convert Date Column
# ==========================================

df["Date"] = pd.to_datetime(df["Date"])

# Create Month Column
df["Month"] = df["Date"].dt.to_period("M")

# ==========================================
# Monthly Average Quiz Score
# ==========================================

monthly_score = df.groupby("Month")["Quiz_Score"].mean()

print("\nMonthly Average Quiz Score")
print(monthly_score)

# Plot Quiz Score Trend
monthly_score.plot(kind="line", marker="o")

plt.title("Monthly Average Quiz Score")
plt.xlabel("Month")
plt.ylabel("Average Quiz Score")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# ==========================================
# Monthly Average Time Spent
# ==========================================

monthly_time = df.groupby("Month")["Time_Spent_Min"].mean()

print("\nMonthly Average Time Spent")
print(monthly_time)

# Plot Time Spent Trend
monthly_time.plot(kind="line", marker="o")

plt.title("Monthly Average Time Spent")
plt.xlabel("Month")
plt.ylabel("Average Time Spent (Minutes)")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# ==========================================
# Monthly Average Feedback Rating
# ==========================================

monthly_feedback = df.groupby("Month")["Feedback_Rating"].mean()

print("\nMonthly Average Feedback Rating")
print(monthly_feedback)

# Plot Feedback Trend
monthly_feedback.plot(kind="line", marker="o")

plt.title("Monthly Average Feedback Rating")
plt.xlabel("Month")
plt.ylabel("Average Feedback Rating")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()

print("\nTime Series Analysis Completed Successfully!")