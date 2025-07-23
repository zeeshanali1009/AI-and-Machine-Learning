from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Fake data: area in sq ft → price in lakhs
X = np.array([[800], [1000], [1200], [1500], [1800]])  # Area
y = np.array([15, 20, 24, 30, 36])  # Price

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Predicted Prices:", y_pred)
print("MSE:", mean_squared_error(y_test, y_pred))
