import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv("diabetes.csv")  # Make sure this file is in the same folder

# Features and label
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model in the current scikit-learn format
with open("diabetes-prediction-rfc-model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model retrained and saved successfully!")
