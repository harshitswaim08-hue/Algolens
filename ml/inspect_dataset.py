import pandas as pd
import os


# ==========================================
# DATASET PATH
# ==========================================

dataset_path = os.path.join(
    os.path.dirname(__file__),
    "dataset.csv"
)


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(dataset_path)


# ==========================================
# BASIC INFORMATION
# ==========================================

print("\n" + "=" * 50)
print("        ALGOLENS DATASET INSPECTION")
print("=" * 50)

print(f"\nTotal rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")


# ==========================================
# COLUMNS
# ==========================================

print("\nColumns:")

for column in df.columns:
    print(f"- {column}")


# ==========================================
# MISSING VALUES
# ==========================================

print("\nMissing values:")

print(df.isnull().sum())


# ==========================================
# DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print(f"\nDuplicate rows: {duplicates}")


# ==========================================
# QUALITY SCORE
# ==========================================

print("\nQuality Score Statistics:")

print(
    df["quality_score"].describe()
)


# ==========================================
# UNIQUE VALUES
# ==========================================

print("\nUnique values per feature:")

for column in df.columns:

    if column != "code":

        print(
            f"{column}: "
            f"{df[column].nunique()} unique values"
        )


# ==========================================
# SCORE DISTRIBUTION
# ==========================================

print("\nQuality Score Distribution:")

print(
    df["quality_score"]
    .value_counts()
    .sort_index()
)


print("\n" + "=" * 50)
print("Dataset inspection completed.")
print("=" * 50)