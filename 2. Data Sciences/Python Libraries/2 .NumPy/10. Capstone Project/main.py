import pandas as pd
import numpy as np

# Reading the Excel file
df = pd.read_excel(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\Python Libraries\2 .NumPy\10. Capstone Project\employee_data_with_issues.xlsx")

# Display first 5 rows
print(df.head())

# Checking for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Filling missing values with mean (for numerical columns)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["Experience"].fillna(df["Experience"].mean(), inplace=True)

# Confirm no missing values in key columns
print("\nMissing values after initial fill:")
print(df.isnull().sum())

# Replacing infinity values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill those NaNs with column mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Removing duplicate rows
df.drop_duplicates(inplace=True)

# Handling negative salaries by replacing them with column mean
df["Salary"] = np.where(df["Salary"] < 0, df["Salary"].mean(), df["Salary"])

# Removing outliers in Salary using 3-sigma rule
salary_mean = df["Salary"].mean()
salary_std = df["Salary"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]

# Final preview after cleaning
print("\nCleaned Data Preview:")
print(df.head())

# Optional: Summary of final data
print("\nFinal dataset shape:", df.shape)
