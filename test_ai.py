from ai.ai_analyzer import (
    summarize_code,
    suggest_improvements,
    generate_improved_code
)

test_code = """
def calculate_sum(n):
    total = 0

    for i in range(n):
        total += i

    return total
"""

print("=" * 50)
print("ALGOLENS AI TEST")
print("=" * 50)

# Test 1: Summary
print("\n[1] Testing Code Summary...")

try:
    result = summarize_code(test_code)
    print("SUCCESS")
    print(result)

except Exception as e:
    print("FAILED")
    print("Error:", e)


# Test 2: Suggestions
print("\n[2] Testing AI Suggestions...")

try:
    result = suggest_improvements(test_code)
    print("SUCCESS")
    print(result)

except Exception as e:
    print("FAILED")
    print("Error:", e)


# Test 3: Improved Code
print("\n[3] Testing Improved Code...")

try:
    result = generate_improved_code(test_code)
    print("SUCCESS")
    print(result)

except Exception as e:
    print("FAILED")
    print("Error:", e)


print("\n" + "=" * 50)
print("AI TEST COMPLETED")
print("=" * 50)