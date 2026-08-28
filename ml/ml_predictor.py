import os
import sys
import joblib

import pandas as pd

# ==================================================
# PROJECT ROOT
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from analyzer.code_parser import analyze_code


# ==================================================
# MODEL PATH
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model.pkl"
)


# ==================================================
# LOAD MODEL
# ==================================================

model = joblib.load(MODEL_PATH)


# ==================================================
# PREDICT QUALITY
# ==================================================

def predict_quality(code):

    result = analyze_code(code)

    if result is None:
        return None

    features = pd.DataFrame([{
    "lines": result["lines"],
    "functions": result["functions"],
    "loops": result["loops"],
    "conditions": result["conditions"],
    "variables": result["variables"],
    "loop_depth": result["loop_depth"]
}])

    prediction = model.predict(features)

    return round(
        float(prediction[0]),
        2
    )