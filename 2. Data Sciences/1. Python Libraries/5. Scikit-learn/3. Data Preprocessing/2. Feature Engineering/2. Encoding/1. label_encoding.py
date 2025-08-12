import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    'Color': ['Red', 'Green', 'Blue', 'Green', 'Red'],
    'Price': [100, 150, 120, 130, 110]
}

df = pd.DataFrame(data)

# Show original data
print("Original Data:")
print(df)

# Initialize LabelEncoder
le = LabelEncoder()

# Apply LabelEncoder on 'Color' column
df['Color_encoded'] = le.fit_transform(df['Color'])

# Show result
print("\nLabel Encoded Data:")
print(df)
