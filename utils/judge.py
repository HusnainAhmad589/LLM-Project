import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyD73rUZGbVYIxUpUW8HtIVH48tjN2cvFXw"))
model = genai.GenerativeModel("models/gemini-flash-latest")

def evaluate_essay(essay):
    prompt = f"""
    You are an automated essay scoring system.

    Score the essay from 1 to 6 based on:
    - Content relevance
    - Organization
    - Grammar
    - Coherence

    Essay:
    \"\"\"{essay}\"\"\"

    Respond ONLY in JSON:
    {{
      "score": number,
      "feedback": "short explanation"
    }}
    """

    response = model.generate_content(prompt)
    return response.text
