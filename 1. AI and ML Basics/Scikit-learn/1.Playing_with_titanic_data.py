# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# Step 1: Load Titanic dataset
df = sns.load_dataset('titanic')
# Step 2: Handle missing values
df['age'] = df['age'].fillna(df['age'].mean())                         # Impute age with mean
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])      # Impute embarked with mode
df['fare'] = df['fare'].fillna(df['fare'].median())                   # Impute fare with median
# Step 3: Drop columns with high missing values or irrelevant ones
df.drop(columns=['deck', 'alive', 'who', 'adult_male', 'embark_town', 'class'], inplace=True)
# Step 4: Convert selected categorical columns into dummy/indicator variables
# Do this only for 'sex' and 'embarked'
sex_dummies = pd.get_dummies(df['sex'], drop_first=True)             # 'male' column (female dropped)
embarked_dummies = pd.get_dummies(df['embarked'], drop_first=True)   # 'Q' and 'S' columns (C dropped)
# Step 5: Concatenate dummy variables back into the original dataframe
df = pd.concat([df, sex_dummies, embarked_dummies], axis=1)
# Step 6: Drop original categorical columns after conversion
df.drop(columns=['sex', 'embarked', 'sibsp', 'parch'], inplace=True)
# Step 7: Define features and target
X = df.drop('survived', axis=1)   # Features
y = df['survived']                # Target variable
# Step 8: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Step 9: Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
# Step 10: Make predictions
y_pred = model.predict(X_test)
# Step 11: Evaluate the model
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
# Optional: Show predictions row by row
results = X_test.copy()
results['Actual'] = y_test
results['Predicted'] = y_pred
results['Prob_Survived'] = model.predict_proba(X_test)[:, 1]
print("\nSample Predictions:")
print(results.head(10))
