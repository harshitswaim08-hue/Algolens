from ai.ai_analyzer import generate_improved_code


test_code = """
def find_pairs(numbers):
    result = []

    for i in numbers:
        for j in numbers:
            result.append((i, j))

    return result
"""


result = generate_improved_code(test_code)

print("\n===== AI IMPROVED CODE =====\n")
print(result)