#import packages
# from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import os

# load_dotenv()

# api_key = os.getenv('OPENAI_API_KEY')

# Ask the user's api key
with st.form('form'):
    user_api_key = st.text_input('Enter OpenAI API token:', type='password')
    submit = st.form_submit_button('Submit')

if submit:
    if len(user_api_key) == 51 and user_api_key.startswith('sk-'):
        client = OpenAI(api_key=user_api_key)
        st.success('api key is successfully entered')
    else:
        st.error('Your api key is invalid.')
        st.stop()

# Make the client visible to other codes below it. 
client = OpenAI(api_key=user_api_key)

# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# client = OpenAI()

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