import pandas as pd

print("Washing machine started 🧼")

# Read dirty data
data = pd.read_csv("data/sample_claims.csv")

print("Dirty data:")
print(data)

# Clean data
clean_data = data.dropna()

print("Clean data:")
print(clean_data)

print("All clothes are clean 🎉")
