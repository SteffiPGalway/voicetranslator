#import packages
from streamlit_webrtc import webrtc_streamer
from gpytranslate import Translator
import speech_recognition as sr
import streamlit as st
from gtts import gTTS
import asyncio

# def get_speech():
#     # initialize the recognizer
#     r = sr.Recognizer()
#     # obtain audio from the microphone
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print("How can I help you today?")
#         audio = r.listen(source)
#     return audio

# def write_to_file(audio):
#     # write audio to a WAV file
#     with open("results.wav", "wb") as f:
#         f.write(audio.get_wav_data())
#     audio_file = "results.wav"
#     return audio_file   

# def convert_speech_to_text(audio_file):
#     # open the file
#     with sr.AudioFile(audio_file) as source:
#         # load audio to memory
#         audio_data = r.record(source)
#         # recognize speech using Google Speech Recognition
#     try:
#         # convert speech to text
#         text = r.recognize_google(audio_data, language="de-DE")
#         print(text)
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#     return text

webrtc_streamer(key="sample")

#import audio file
audio_file = "results.wav"

# initialize the recognizer
r = sr.Recognizer()

input_lang = st.selectbox(
    "Source language",
    ("English", "German", "French","Spanish"),
)

st.write("Source language:", input_lang)

if input_lang == "English":
    src_lang = "en-UK"
elif input_lang == "German":
    src_lang = "de-DE"
elif input_lang == "French":
    src_lang = "fr-FR"  
elif input_lang == "Spanish":
    src_lang = "es-ES"

output_lang = st.selectbox(
    "Target language",
    ("English", "German", "French","Spanish"),
)

st.write("Target language:", output_lang)

# obtain audio from the microphone
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# open the file
with sr.AudioFile(audio_file) as source:
    # load audio to memory
    audio_data = r.record(source)
    # recognize speech using Google Speech Recognition
    try:
        # convert speech to text
        text = r.recognize_google(audio_data, language=src_lang)
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
async def main():
    t = Translator()
    translation = await t.translate(text, targetlang=output_lang)
    language = await t.detect(translation.text)
    print(f"Translation: {translation.text}\nDetected language: {src_lang}")
    tts = gTTS(text=translation.text, lang=output_lang, slow=True)
    tts.save('speech.mp3')


if __name__ == "__main__":
    asyncio.run(main())
