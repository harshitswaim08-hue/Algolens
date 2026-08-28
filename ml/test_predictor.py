import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)

from ml.ml_predictor import predict_quality


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


score = predict_quality(code)

print("=" * 50)
print("ALGOLENS ML PREDICTION TEST")
print("=" * 50)
print(f"Quality Score: {score}")
print("=" * 50)