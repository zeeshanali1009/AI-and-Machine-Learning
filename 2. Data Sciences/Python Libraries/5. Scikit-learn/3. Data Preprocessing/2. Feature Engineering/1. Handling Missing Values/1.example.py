import pandas as pd
from sklearn.impute import SimpleImputer

# Sample data with missing values
df = pd.DataFrame({
    'Age': [25, 30, None, 28, 22],
    'Salary': [50000, 60000, 55000, None, 58000]
})

# Imputer: Replace missing values with the mean
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])

print(df)
