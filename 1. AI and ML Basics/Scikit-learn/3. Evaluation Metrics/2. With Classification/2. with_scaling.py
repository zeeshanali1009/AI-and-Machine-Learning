# Import required libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import accuracy_score

# Load breast cancer dataset
data = load_breast_cancer()
X = data.data       # Features
y = data.target     # Target (0 = malignant, 1 = benign)

# ==============================
# PART 2: With Min-Max Scaling
# ==============================

# Apply Min-Max Scaling
minmax_scaler = MinMaxScaler()
X_minmax = minmax_scaler.fit_transform(X)

# Train-test split on scaled data
X_train_minmax, X_test_minmax, y_train_minmax, y_test_minmax = train_test_split(X_minmax, y, test_size=0.2, random_state=42)

# Train classifiers
dt_minmax = DecisionTreeClassifier(random_state=42)
rf_minmax = RandomForestClassifier(random_state=42)

dt_minmax.fit(X_train_minmax, y_train_minmax)
rf_minmax.fit(X_train_minmax, y_train_minmax)

# Predictions
dt_preds_minmax = dt_minmax.predict(X_test_minmax)
rf_preds_minmax = rf_minmax.predict(X_test_minmax)

# Accuracy scores (Min-Max scaling)
print("Decision Tree Accuracy (Min-Max Scaling):", accuracy_score(y_test_minmax, dt_preds_minmax))
print("Random Forest Accuracy (Min-Max Scaling):", accuracy_score(y_test_minmax, rf_preds_minmax))


# ==============================
# PART 3: With Z-Score (Standard) Scaling
# ==============================

# Apply Standard Scaling (Z-score)
standard_scaler = StandardScaler()
X_standard = standard_scaler.fit_transform(X)

# Train-test split on standard-scaled data
X_train_std, X_test_std, y_train_std, y_test_std = train_test_split(X_standard, y, test_size=0.2, random_state=42)

# Train classifiers
dt_std = DecisionTreeClassifier(random_state=42)
rf_std = RandomForestClassifier(random_state=42)

dt_std.fit(X_train_std, y_train_std)
rf_std.fit(X_train_std, y_train_std)

# Predictions
dt_preds_std = dt_std.predict(X_test_std)
rf_preds_std = rf_std.predict(X_test_std)

# Accuracy scores (Standard scaling)
print("Decision Tree Accuracy (Z-score Scaling):", accuracy_score(y_test_std, dt_preds_std))
print("Random Forest Accuracy (Z-score Scaling):", accuracy_score(y_test_std, rf_preds_std))
