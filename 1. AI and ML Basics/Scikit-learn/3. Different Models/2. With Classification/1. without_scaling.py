from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifiers
dt = DecisionTreeClassifier(random_state=42)
rf = RandomForestClassifier(random_state=42)

dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Predictions
dt_preds = dt.predict(X_test)
rf_preds = rf.predict(X_test)

# Accuracy
print("Decision Tree Accuracy (No Scaling):", accuracy_score(y_test, dt_preds))
print("Random Forest Accuracy (No Scaling):", accuracy_score(y_test, rf_preds))
