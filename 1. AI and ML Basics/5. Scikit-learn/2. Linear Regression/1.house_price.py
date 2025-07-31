# Step 1: Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the California Housing dataset as a DataFrame
data = fetch_california_housing(as_frame=True)
df = data.frame  # includes all features and target MedHouseVal

# Step 3: Preliminary data exploration
print(df.isnull().sum())              # Should show 0 null values for all columns
print(df.describe())                 # Summary statistics for features and target

# Step 4: (Optional) drop any columns you don't need
# Here, we keep all because they are numeric and useful predictors

# Step 5: Define features (X) and target (y)
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']  # median house value in units of $100,000

# Step 6: Split into training and testing sets (80% train / 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7: Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

# Step 9: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)

# Step 10: Compare actual vs predicted (first 10 rows)
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nSample Predictions:")
print(results.head(10))

# Step 11: Plot Actual vs Predicted values (regression line)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         color='red', linestyle='--')
plt.xlabel("Actual Median House Value ($100k)")
plt.ylabel("Predicted Median House Value ($100k)")
plt.title("Actual vs. Predicted Prices")
plt.grid(True)
plt.show()

# Step 12: Plot distribution of residuals (Actual – Predicted)
residuals = y_test - y_pred
plt.figure(figsize=(8, 5))
sns.histplot(residuals, kde=True, bins=30, color='green')
plt.xlabel("Residual = Actual – Predicted")
plt.title("Residual Distribution")
plt.grid(True)
plt.show()
