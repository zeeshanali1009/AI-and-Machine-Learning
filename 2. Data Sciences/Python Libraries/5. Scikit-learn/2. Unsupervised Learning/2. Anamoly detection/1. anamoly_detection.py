from sklearn.ensemble import IsolationForest
import numpy as np

# Normal and abnormal transaction amounts
X = np.array([
    [200], [220], [210], [230], [240], [250],  # normal
    [1500], [1700]  # suspicious
])

# Train model
iso = IsolationForest(contamination=0.2)  # ~20% are anomalies
iso.fit(X)

# Predict
outliers = iso.predict(X)  # -1 = anomaly, 1 = normal
print("Anomaly Detection Result:", outliers)
