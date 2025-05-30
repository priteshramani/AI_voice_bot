import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# Set Gemini API Key
import google.generativeai as genai
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
client = genai.configure(api_key=GEMINI_API_KEY)

# Text to speech function
from gtts import gTTS
def text_to_speech(text, filename="voice_output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

st.title("AI Voice Bot using Gemini")
st.write("Type your message, let AI respond, and hear it aloud!")

user_input = st.text_input("Enter your message:")

st.write("You entered:", user_input)

if st.button("Generate & Speak"):
    if user_input:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            ai_reply = response.text
            st.success(f"AI says: {ai_reply}")

            audio_file = text_to_speech(ai_reply)
            st.audio(audio_file)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter or speak something first.")