import os

from dotenv import load_dotenv
from google import genai


# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please check your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


# --------------------------------------------------
# AI CODE SUMMARY
# --------------------------------------------------

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

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# --------------------------------------------------
# AI CODE SUGGESTIONS
# --------------------------------------------------

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

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


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

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text