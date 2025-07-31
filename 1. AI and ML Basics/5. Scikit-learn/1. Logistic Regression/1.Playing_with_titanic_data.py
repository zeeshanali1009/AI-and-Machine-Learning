# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load Titanic dataset
df = sns.load_dataset('titanic')

# Step 2: Handle missing values
df['age'] = df['age'].fillna(df['age'].mean())                         # Impute 'age' with mean
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])      # Impute 'embarked' with mode
df['fare'] = df['fare'].fillna(df['fare'].median())                   # Impute 'fare' with median

# Step 3: Drop columns with many missing values or irrelevant info
df.drop(columns=['deck', 'alive', 'who', 'adult_male', 'embark_town', 'class'], inplace=True)

# Step 4: Convert categorical variables into dummy variables
sex_dummies = pd.get_dummies(df['sex'], drop_first=True)              # Convert 'sex' to 'male'
embarked_dummies = pd.get_dummies(df['embarked'], drop_first=True)    # Convert 'embarked' to 'Q', 'S'

# Step 5: Concatenate dummy variables back into the DataFrame
df = pd.concat([df, sex_dummies, embarked_dummies], axis=1)

# Step 6: Drop original categorical columns and other unnecessary ones
df.drop(columns=['sex', 'embarked', 'sibsp', 'parch'], inplace=True)

# Step 7: Define features (X) and target (y)
X = df.drop('survived', axis=1)    # All columns except 'survived'
y = df['survived']                 # Target variable

# Step 8: Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 9: Train Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 10: Predict on test data
y_pred = model.predict(X_test)

# Step 11: Evaluate model
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Step 12: Show predictions and predicted probabilities
results = X_test.copy()
results['Actual'] = y_test
results['Predicted'] = y_pred
results['Prob_Survived'] = model.predict_proba(X_test)[:, 1]

# Display first 10 rows of results
print("\nSample Predictions (0 = did not survive, 1 = survived):")
print(results[['Actual', 'Predicted', 'Prob_Survived']].head(10))
