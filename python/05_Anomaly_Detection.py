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
# Rule-Based Anomaly Detection
# ==========================

def detect_anomaly(row):
    flags = []

    # Low Quiz Score
    if row["Quiz_Score"] < 50:
        flags.append("Low Quiz Score")

    # High Time Spent
    if row["Time_Spent_Min"] > 90:
        flags.append("High Time Spent")

    # Low Feedback
    if row["Feedback_Rating"] < 2:
        flags.append("Low Feedback")

    if len(flags) == 0:
        return "Normal"

    return ", ".join(flags)

# Create Anomaly Flag Column
df["Anomaly_Flag"] = df.apply(detect_anomaly, axis=1)

# ==========================
# Summary
# ==========================

print("\nAnomaly Summary")
print(df["Anomaly_Flag"].value_counts())

print("\nDetected Anomalies")
print(df[df["Anomaly_Flag"] != "Normal"])

# ==========================
# Save Output
# ==========================

output_path = "Data/cleaned/Anomaly_Detected_Data.xlsx"
df.to_excel(output_path, index=False)

print("\nAnomaly Detection Completed Successfully!")
print("Output saved to:", output_path)