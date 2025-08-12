from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample data
X = np.array([[1, 100],
              [2, 200],
              [3, 300]])

# Apply Min-Max Scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print("Original Data:\n", X)
print("\nMinMax Scaled Data:\n", X_scaled)
