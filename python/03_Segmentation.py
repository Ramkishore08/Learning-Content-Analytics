import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ==========================
# Load cleaned dataset
# ==========================

file_path = "Data/cleaned/Cleaned_Education_Data.xlsx"
df = pd.read_excel(file_path)

print(df.head())

# ==========================
# Select features for clustering
# ==========================

X = df[["Quiz_Score", "Time_Spent_Min"]]

# ==========================
# Apply K-Means Clustering
# ==========================

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Student_Group"] = kmeans.fit_predict(X)

# ==========================
# View cluster counts
# ==========================

print("\nCluster Distribution:")
print(df["Student_Group"].value_counts())

# ==========================
# Visualize clusters
# ==========================

plt.figure(figsize=(8,5))
plt.scatter(df["Quiz_Score"], df["Time_Spent_Min"], c=df["Student_Group"], cmap="viridis")

plt.title("Student Segmentation (K-Means Clustering)")
plt.xlabel("Quiz Score")
plt.ylabel("Time Spent (Minutes)")

plt.colorbar(label="Cluster Group")
plt.show()

# ==========================
# Save output file (IMPORTANT)
# ==========================

output_path = "Data/cleaned/Segmented_Data.xlsx"
df.to_excel(output_path, index=False)

print("\nSegmented dataset saved successfully!")