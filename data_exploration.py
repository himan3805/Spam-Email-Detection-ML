import pandas as pd

# Load Dataset
df = pd.read_csv("spam_dataset.csv")  # Change filename if needed

# Display first few rows
print("📌 First 5 rows of dataset:\n", df.head())

# Display dataset shape
print(f"\n📌 Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Check for missing values
missing_values = df.isnull().sum()
print("\n📌 Missing values per column:\n", missing_values[missing_values > 0])

# Display column names
print("\n📌 Column Names:\n", df.columns.tolist())

# Check if 'email' and 'Label' exist
expected_columns = ['email', 'Label']  # Adjust based on actual column names
if not all(col in df.columns for col in expected_columns):
    print("\n🚨 Warning: Expected 'email' and 'Label' columns not found!")
    print("✅ Columns found:", df.columns.tolist())

# Display class distribution (if 'Label' column exists)
if 'Label' in df.columns:
    print("\n📌 Class Distribution:\n", df['Label'].value_counts())

# Print dataset info
print("\n📌 Dataset Info:\n")
print(df.info())
