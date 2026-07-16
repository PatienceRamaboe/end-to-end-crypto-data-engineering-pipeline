import pandas as pd

# Read raw data
df = pd.read_csv("Data/Raw_Data.csv")

print("Rows before cleaning:", len(df))

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Convert date column
df["date"] = pd.to_datetime(df["date"])

print("Rows after cleaning:", len(df))

# Save cleaned data
df.to_csv("Data/Clean_Data.csv", index=False)

print("✅ Clean data saved successfully!")