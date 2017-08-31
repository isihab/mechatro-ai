#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS


#Text_to_speech
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='bn')
    tts.save("audio.mp3")
    os.system("audio.mp3")


#Main_function
def mechatro(val):
    if "how are you" in val:
        speak("I am fine")
 
    if "what is your name" in val:
        speak("I am Mechatro")

    if "What can you do for me" in val:
        speak("I can do anything for you")





 
# Record Audio
def recaud():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What you want me to do for you, sir?")
        audio = r.listen(source)
     
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

value = recaud()


print("out:" + value)

