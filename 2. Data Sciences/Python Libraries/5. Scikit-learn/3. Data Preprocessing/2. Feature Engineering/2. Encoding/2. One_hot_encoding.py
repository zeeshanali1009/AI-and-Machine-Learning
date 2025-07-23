import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample dataset
data = {
    'Color': ['Red', 'Green', 'Blue', 'Green', 'Red'],
    'Price': [100, 150, 120, 130, 110]
}

df = pd.DataFrame(data)

# Reshape the 'Color' column (required for sklearn)
color = df[['Color']]

# Initialize OneHotEncoder
ohe = OneHotEncoder(sparse=False)

# Apply OneHotEncoder
encoded_colors = ohe.fit_transform(color)

# Convert to DataFrame
encoded_df = pd.DataFrame(encoded_colors, columns=ohe.get_feature_names_out(['Color']))

# Concatenate with original data (excluding original 'Color')
final_df = pd.concat([df.drop('Color', axis=1), encoded_df], axis=1)

# Show result
print("One-Hot Encoded Data:")
print(final_df)
