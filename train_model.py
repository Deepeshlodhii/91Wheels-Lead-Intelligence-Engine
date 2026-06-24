import pandas as pd
import lightgbm as lgb
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)



# Load Dataset

df = pd.read_csv(
    "data/91Wheels_leads_dataset_5000.csv"
)

# Features

X = df.drop(
    columns=["user_id", "purchased"]
)

# Target

y = df["purchased"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model

model = lgb.LGBMClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

# Train

model.fit(
    X_train,
    y_train
)

# Evaluate

pred = model.predict(X_test)

acc = accuracy_score(
    y_test,
    pred
)

print(
    f"Accuracy: {acc:.4f}"
)

# Save Model

joblib.dump(
    model,
    "models/lead_model.pkl"
)

print(
    "Model Saved Successfully!"
)
pred = model.predict(X_test)

print(f"Accuracy : {accuracy_score(y_test,pred):.4f}")
print(f"Precision: {precision_score(y_test,pred):.4f}")
print(f"Recall   : {recall_score(y_test,pred):.4f}")
print(f"F1 Score : {f1_score(y_test,pred):.4f}")