import os
import sys
import json
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

settings={ 
 "configs": json.load(open(os.getcwd()+"/ankaspark.default.json",'r')),
 "commands": sys.argv[1::]
}

if os.path.exists(os.getcwd()+"/ankaspark.json"):
 settings.update(json.load(open(os.getcwd()+"/ankaspark.json",'r')))

def speak(text):
   engine=pyttsx3.init()
   engine.say(text)
   engine.runAndWait()


speak("Hello")