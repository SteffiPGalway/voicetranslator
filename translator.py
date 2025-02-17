#import packages
# from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import os

# load_dotenv()

OpenAI_API_KEY=input("Enter your OpenAI API Key")

# api_key = os.getenv('OPENAI_API_KEY')

api_key=OpenAI_API_KEY

client = OpenAI()

st.title("Voice Translation App")

audio_value = st.audio_input("Say something!")

if audio_value:
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file = audio_value
  )

  transcript_text = transcript.text
  st.write(transcript_text)
