import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env file se environment variables load karein
load_dotenv()

# Environment variable se key read karein
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(
            "gemini-3.6-flash",
            system_instruction="Provide clear, well-formatted plain text answers without huge empty spacing"
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {str(e)}"