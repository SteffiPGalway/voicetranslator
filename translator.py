#import packages
# from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import os

# load_dotenv()

# api_key = os.getenv('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

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

txt_file = "transcription.txt"

# Initialize session state for download confirmation
if "downloaded" not in st.session_state:
  st.session_state.downloaded = False

  # Download button
  if st.download_button(label="Download Transcription",
                        file_name="transcription.txt",data=transcript_text):
      st.session_state.downloaded = True

    # Show success message after download
  if st.session_state.downloaded:
        st.success("Transcription file downloaded successfully!")