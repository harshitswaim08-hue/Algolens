import sys
import os
import csv
import random

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(PROJECT_ROOT)

from analyzer.code_parser import analyze_code


TOTAL_SAMPLES = 1000

OUTPUT_FILE = os.path.join(
    os.path.dirname(__file__),
    "dataset.csv"
)

random.seed(42)


# ==================================================
# CODE GENERATORS
# ==================================================

def generate_high(i):

    n = 20 + (i % 480)

    if i % 3 == 0:
        return f"""
def calculate_sum(numbers):
    return sum(numbers)

numbers = list(range({n}))
result = calculate_sum(numbers)
print(result)
"""

    elif i % 3 == 1:
        return f"""
def find_max(numbers):
    return max(numbers)

numbers = list(range({n}))
result = find_max(numbers)
print(result)
"""

    else:
        limit = 10 + (i % 50)

        return f"""
def filter_numbers(numbers):
    return [
        number for number in numbers
        if number > {limit}
    ]

numbers = list(range({n}))
result = filter_numbers(numbers)
print(result)
"""


def generate_medium_high(i):

    n = 20 + (i % 280)

    if i % 2 == 0:
        return f"""
def calculate_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total

numbers = list(range({n}))
result = calculate_sum(numbers)
print(result)
"""

    target = i % n

    return f"""
def search(numbers, target):

    for number in numbers:

        if number == target:
            return True

    return False

numbers = list(range({n}))
result = search(numbers, {target})
print(result)
"""


def generate_medium_low(i):

    n = 10 + (i % 50)
    limit = 5 + (i % 30)

    if i % 2 == 0:

        return f"""
def analyze_numbers(numbers):

    result = []

    for number in numbers:

        if number > {limit}:

            if number % 2 == 0:
                result.append(number * 2)

            else:
                result.append(number + 1)

    return result

numbers = list(range({n}))
result = analyze_numbers(numbers)
print(result)
"""

    return f"""
def find_pairs(numbers):

    pairs = []

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] != numbers[j]:
                pairs.append(
                    (numbers[i], numbers[j])
                )

    return pairs

numbers = list(range({n}))
result = find_pairs(numbers)
print(len(result))
"""


def generate_low(i):

    n = 3 + (i % 10)
    limit = 1 + (i % 5)

    if i % 2 == 0:

        return f"""
def process_data(data):

    result = []

    for a in data:
        for b in data:
            for c in data:
                for d in data:

                    if a != b:
                        if b != c:
                            if c != d:
                                if a > {limit}:
                                    result.append(
                                        a + b + c + d
                                    )

    return result

data = list(range({n}))
result = process_data(data)
print(result)
"""

    return f"""
def classify(numbers):

    result = []

    for number in numbers:

        if number > 10:
            if number > 20:
                if number > 30:
                    if number > 40:
                        if number > 50:
                            result.append(
                                "very-large"
                            )

    return result

numbers = list(range({n}))
result = classify(numbers)
print(result)
"""


# ==================================================
# QUALITY SCORE
# ==================================================

def calculate_quality_score(result, level):

    score = 100

    complexity = str(
        result.get("time_complexity", "O(1)")
    ).lower()

    lines = result.get("lines", 0)
    conditions = result.get("conditions", 0)
    variables = result.get("variables", 0)
    loop_depth = result.get("loop_depth", 0)
    loops = result.get("loops", 0)

    if "o(2" in complexity or "exponential" in complexity:
        score -= 30

    elif "o(n^3" in complexity:
        score -= 25

    elif "o(n^2" in complexity:
        score -= 15

    elif "o(n log n" in complexity:
        score -= 8

    elif "o(n)" in complexity:
        score -= 3

    score -= min(loop_depth * 3, 15)
    score -= min(conditions, 10)
    score -= min(max(variables - 10, 0), 8)

    if lines > 200:
        score -= 10

    elif lines > 100:
        score -= 6

    elif lines > 60:
        score -= 3

    if loops > 5:
        score -= 7

    elif loops > 3:
        score -= 3

    if level == "high":
        score += random.randint(0, 5)

    elif level == "medium_high":
        score -= random.randint(5, 12)

    elif level == "medium_low":
        score -= random.randint(12, 22)

    else:
        score -= random.randint(22, 38)

    return max(20, min(100, score))


# ==================================================
# DATASET GENERATION
# ==================================================

def generate_dataset():

    rows = []

    for i in range(TOTAL_SAMPLES):

        # ------------------------------------------
        # Select quality level
        # ------------------------------------------

        position = i % 4

        if position == 0:
            level = "high"
            code = generate_high(i)

        elif position == 1:
            level = "medium_high"
            code = generate_medium_high(i)

        elif position == 2:
            level = "medium_low"
            code = generate_medium_low(i)

        else:
            level = "low"
            code = generate_low(i)

        # ------------------------------------------
        # Analyze
        # ------------------------------------------

        try:

            result = analyze_code(code)

            if result is None:
                continue

            score = calculate_quality_score(
                result,
                level
            )

            rows.append({
                "code": code.strip(),

                "lines": result.get(
                    "lines", 0
                ),

                "functions": result.get(
                    "functions", 0
                ),

                "loops": result.get(
                    "loops", 0
                ),

                "conditions": result.get(
                    "conditions", 0
                ),

                "variables": result.get(
                    "variables", 0
                ),

                "loop_depth": result.get(
                    "loop_depth", 0
                ),

                "time_complexity": result.get(
                    "time_complexity",
                    "O(1)"
                ),

                "space_complexity": result.get(
                    "space_complexity",
                    "O(1)"
                ),

                "quality_score": score
            })

        except Exception as error:

            print(
                f"Error at sample {i}: {error}"
            )


        # ------------------------------------------
        # Progress
        # ------------------------------------------

        if (i + 1) % 100 == 0:

            print(
                f"Generated: {i + 1}/{TOTAL_SAMPLES}"
            )


    # ==================================================
    # SAVE
    # ==================================================

    fieldnames = [
        "code",
        "lines",
        "functions",
        "loops",
        "conditions",
        "variables",
        "loop_depth",
        "time_complexity",
        "space_complexity",
        "quality_score"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)


    print("\n" + "=" * 50)
    print("ALGOLENS DATASET GENERATED")
    print("=" * 50)

    print(
        f"Samples generated: {len(rows)}"
    )

    print(
        f"Dataset saved at: {OUTPUT_FILE}"
    )

    print("=" * 50)


# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":
    generate_dataset()