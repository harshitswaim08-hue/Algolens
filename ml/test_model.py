import os
import sys
import joblib

# Project root ko Python path mein add karo
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(PROJECT_ROOT)

from analyzer.code_parser import analyze_code


# Model path
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model.pkl"
)

# Load model
model = joblib.load(MODEL_PATH)


# Sample code
code = """
def calculate_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total


numbers = [1, 2, 3, 4, 5]

result = calculate_sum(numbers)

print(result)
"""


# Analyze code
result = analyze_code(code)

if result is None:
    print("Invalid Python code")
    exit()


# Extract features
features = [[
    result["lines"],
    result["functions"],
    result["loops"],
    result["conditions"],
    result["variables"],
    result["loop_depth"]
]]


# Predict
prediction = model.predict(features)


print("\n" + "=" * 50)
print("ALGOLENS ML PREDICTION")
print("=" * 50)

print(
    f"Predicted Quality Score: {prediction[0]:.2f}"
)

print("=" * 50)