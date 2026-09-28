import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Checking Gemini model...")

model = client.models.get(
    model="gemini-3.6-flash"
)

print("Model found successfully!")
print(model)