import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = sns.load_dataset('titanic')

# Impute missing values (safe way, no warnings)
df['age'] = df['age'].fillna(df['age'].mean())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['fare'] = df['fare'].fillna(df['fare'].median())

# Drop columns
df.drop(columns=['deck', 'alive', 'who', 'adult_male', 'embark_town', 'class'], inplace=True)

# Convert categorical columns to dummies
df = pd.get_dummies(df, columns=df.select_dtypes(include='object').columns, drop_first=True)

# Drop unhelpful columns
df.drop(columns=['sibsp', 'parch'], inplace=True)

# Features and Target
X = df.drop('survived', axis=1)
y = df['survived']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
