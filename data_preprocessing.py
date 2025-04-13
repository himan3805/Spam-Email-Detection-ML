import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("spam_dataset.csv")

# Drop "Email No." since it's not needed
df.drop(columns=["Email No."], inplace=True)

# Ensure "Prediction" column exists
if "Prediction" not in df.columns:
    raise ValueError("❌ 'Prediction' column not found in dataset!")

# Split features and labels
X = df.drop(columns=["Prediction"])  # Features (word counts)
y = df["Prediction"]  # Labels (Spam/Ham)

# Train-Test Split (80-20 ratio)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("✅ Data Preprocessing Completed & Saved!")
