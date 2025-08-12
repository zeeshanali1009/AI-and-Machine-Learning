import pandas as pd

# Sample dataset
data = {
    'Name': ['Ali', 'Ahmed', 'Sara', 'Fatima', 'Zain'],
    'Age': [25, 30, 22, None, 29],
    'Gender': ['M', 'M', 'F', 'F', 'M'],
    'Email': ['ali@gmail.com', 'ahmed@yahoo.com', 'sara@hotmail.com', 'fatima@gmail.com', 'zain@gmail.com'],
    'Salary': [50000, 60000, 52000, 58000, None],
    'Employee_ID': [101, 102, 103, 104, 105]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
