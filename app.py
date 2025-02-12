import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/translate"

# UI Title
st.title("TransLingua: AI-Powered Translator")

# User Inputs
text = st.text_area("Enter text to translate:")
source_lang = st.selectbox("Source Language", ["English", "Spanish", "French", "German", "Chinese", "Hindi", "Arabic"])
target_lang = st.selectbox("Target Language", ["English", "Spanish", "French", "German", "Chinese", "Hindi", "Arabic"])

# Translate Button
if st.button("Translate"):
    if text:
        data = {"text": text, "source_lang": source_lang, "target_lang": target_lang}
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            st.success(f"Translation: {response.json().get('translated_text', 'Error translating text')}")
        else:
            st.error("Translation failed. Please try again.")
    else:
        st.warning("Please enter text to translate.")
