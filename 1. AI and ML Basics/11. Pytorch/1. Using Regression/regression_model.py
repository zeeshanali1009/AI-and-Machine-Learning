import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# 1. Load the California Housing dataset
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=["Price"])

# 2. Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Normalize the features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32)

# 5. Define the regression model class
class RegressionModel(nn.Module):
    def __init__(self, input_dim):
        super(RegressionModel, self).__init__()
        self.linear1 = nn.Linear(input_dim, 64)  # Linear layer
        self.relu = nn.ReLU()                   # Non-linear activation
        self.linear2 = nn.Linear(64, 1)         # Output layer

    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        return out

# 6. Create model instance
input_dim = X_train_tensor.shape[1]
model = RegressionModel(input_dim)

# 7. Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 8. Train the model
epochs = 100
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 9. Save the model
torch.save(model.state_dict(), "regression_model.pth")
print("Model saved as regression_model.pth")

# 10. Load the model again (optional)
loaded_model = RegressionModel(input_dim)
loaded_model.load_state_dict(torch.load("regression_model.pth"))
loaded_model.eval()

# 11. Make predictions using the loaded model
with torch.no_grad():
    predictions = loaded_model(X_test_tensor).numpy()

print("Predictions on test data:")
print(predictions[:5])
