import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ==================================================
# PATHS
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model.pkl"
)


# ==================================================
# LOAD DATASET
# ==================================================

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print(
    f"Dataset loaded successfully: {len(df)} rows"
)


# ==================================================
# SELECT FEATURES
# ==================================================

features = [
    "lines",
    "functions",
    "loops",
    "conditions",
    "variables",
    "loop_depth"
]

target = "quality_score"


X = df[features]

y = df[target]


# ==================================================
# TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print(
    f"Training samples: {len(X_train)}"
)

print(
    f"Testing samples: {len(X_test)}"
)


# ==================================================
# MODEL
# ==================================================

print("\nTraining Random Forest model...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)


# ==================================================
# PREDICTION
# ==================================================

predictions = model.predict(
    X_test
)


# ==================================================
# EVALUATION
# ==================================================

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)


print("\n" + "=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

print(
    f"Mean Absolute Error (MAE): {mae:.2f}"
)

print(
    f"R² Score: {r2:.2f}"
)


# ==================================================
# SAVE MODEL
# ==================================================

joblib.dump(
    model,
    MODEL_PATH
)


print("\n" + "=" * 50)
print("MODEL TRAINING COMPLETED")
print("=" * 50)

print(
    f"Model saved at: {MODEL_PATH}"
)

print("=" * 50)