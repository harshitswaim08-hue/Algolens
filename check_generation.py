import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("Testing Gemini generation...")

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Give one short Python optimization tip."
    )

    print("\nSUCCESS!")
    print("Response:")
    print(response.text)

except Exception as e:
    print("\nFAILED!")
    print("Error:", e)