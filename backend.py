import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Google API key not found. Check .env file.")

# Configure Generative AI
genai.configure(api_key=api_key)

# Initialize FastAPI
app = FastAPI()

# Request Model
class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

@app.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Translate '{request.text}' from {request.source_lang} to {request.target_lang}.")
        return {"translation": response.text}
    except Exception as e:
        return {"error": str(e)}
