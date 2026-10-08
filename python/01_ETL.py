import pandas as pd

# ==========================
# Read Excel File
# ==========================

file_path = "Data/raw/MasterEducation&_EdTech_Data.xlsx"

df = pd.read_excel(file_path)

# ==========================
# Display Dataset Details
# ==========================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nRows and Columns")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# ==========================
# Data Cleaning
# ==========================

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with only one non-empty value
df = df.dropna(thresh=2)

# Fill missing numeric values
numeric_columns = df.select_dtypes(include="number").columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing text values
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].fillna("Unknown")

# ==========================
# Clean Age Column
# ==========================

# Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Replace invalid ages
df.loc[(df["Age"] <= 0) | (df["Age"] > 100), "Age"] = pd.NA

# Fill missing/invalid ages with average
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

# ==========================
#clean data column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# ==========================
# Save Cleaned Dataset
# ==========================

output_path = "Data/cleaned/Cleaned_Education_Data.xlsx"

df.to_excel(output_path, index=False)

print("\nCleaned dataset saved successfully!")

# ==========================
# Verify Cleaning
# ==========================

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nRows and Columns After Cleaning")
print(df.shape)

print("\nFirst 5 Rows of Cleaned Data")
print(df.head())