import os
import sys
import json
import pyttsx3
import speech_recognition as sr

settings={ 
 "configs": json.load(open(os.getcwd()+"/ankaspark.default.json",'r')),
}

if os.path.exists(os.getcwd()+"/ankaspark.json"):
 settings.update(json.load(open(os.getcwd()+"/ankaspark.json",'r')))

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
   if sys.argv and settings.get("configs").get("speak_console_text_write")==True:
      print(text)
   engine.say(text)
   engine.runAndWait()

speak("Hello I am "+settings.get("configs").get("hey_suffix"))
