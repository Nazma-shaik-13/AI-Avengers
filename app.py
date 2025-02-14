import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit application
st.title("Translingua-AI: Multi-Language Translator 🌍")

# Input text for translation
user_input = st.text_area("Enter text to translate:")

# Language selection
source_language = st.selectbox("Select source language:", ["English", "Spanish", "French", "German", "Chinese"])
target_language = st.selectbox("Select target language:", ["English", "Spanish", "French", "German", "Chinese"])

# Replace the ChatCompletion part with GenerativeModel
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

if st.button("Translate"):
    if user_input:
        with st.spinner("Translating..."):
            prompt = f"Translate the following text from {source_language} to {target_language}: {user_input}"
            response = model.generate_content(prompt)
            translation = response.text if response else "No response"
            st.success(f"Translation: {translation}")
    else:
        st.error("Please enter text to translate.")