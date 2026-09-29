import os
import time

from dotenv import load_dotenv
from google import genai


# ==================================================
# LOAD API KEY
# ==================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please check your .env file."
    )


# ==================================================
# GEMINI CLIENT
# ==================================================

client = genai.Client(api_key=API_KEY)


# ==================================================
# MODELS
# ==================================================

PRIMARY_MODEL = "gemini-3.6-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"


# ==================================================
# GEMINI REQUEST
# ==================================================

def generate_with_retry(prompt):

    models = [
        PRIMARY_MODEL,
        FALLBACK_MODEL
    ]

    last_error = None

    for model_name in models:

        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                return response.text

            except Exception as e:

                last_error = e
                error_text = str(e)

                # Retry temporary availability errors
                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                ):

                    if attempt == 0:
                        print(
                            f"{model_name} temporarily unavailable."
                        )

                        time.sleep(3)
                        continue

                    print(
                        f"{model_name} unavailable. "
                        f"Trying next model..."
                    )

                    break

                # Don't hide other errors
                raise

    raise last_error


# ==================================================
# AI CODE SUMMARY
# ==================================================

def summarize_code(code):

    prompt = f"""
You are an expert software engineer.

Analyze the following Python code.

Provide a concise and easy-to-understand explanation containing:

1. What the code does
2. Main purpose of the code
3. How the code works
4. Important observations

Do not rewrite the code.
Do not provide unnecessary information.

Python Code:

{code}
"""

    return generate_with_retry(prompt)


# ==================================================
# AI CODE SUGGESTIONS
# ==================================================

def suggest_improvements(code):

    prompt = f"""
You are an expert software engineer and code optimization assistant.

Analyze the following Python code and provide useful improvement suggestions.

Focus on:

1. Performance problems
2. Time complexity
3. Space complexity
4. Code quality
5. Readability
6. Possible optimizations

Give your response in this format:

### Problems Detected

- List important problems found in the code.

### Improvement Suggestions

- Give clear and practical suggestions.

### Optimization Explanation

- Explain how the code could be made more efficient.

Do not make up problems if the code is already good.
Keep the explanation concise and beginner-friendly.

Python Code:

{code}
"""

    return generate_with_retry(prompt)


# ==================================================
# AI IMPROVED CODE
# ==================================================

def generate_improved_code(code):

    prompt = f"""
You are an expert Python developer.

Improve the following Python code.

Goals:

1. Improve time complexity where possible.
2. Reduce unnecessary memory usage.
3. Improve readability.
4. Keep the original functionality unchanged.

Return ONLY the improved Python code.

Do not add explanations.
Do not use markdown code fences.

Original Python Code:

{code}
"""

    return generate_with_retry(prompt)