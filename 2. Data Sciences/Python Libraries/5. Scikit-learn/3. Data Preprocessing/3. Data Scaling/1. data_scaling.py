from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.array([[10, 200],
              [20, 400],
              [30, 600]])

# Apply Standard Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Original Data:\n", X)
print("\nStandard Scaled Data:\n", X_scaled)
