import os
import sys
import json
import pyttsx3
import platform
from tkinter import *
import speech_recognition as sr
working_directory=os.getcwd()
settings={
 "assistant_crd": os.path.realpath(".")+"/",
 "assistant_wd": working_directory,
 "schema_protocol" : "ankaspark-ai"
}
settings.update(json.load(open(os.getcwd()+"/ankaspark.default.json",'r')))
if os.path.exists(working_directory+"/ankaspark.json"):
 settings.update(json.load(open(os.getcwd()+"/ankaspark.json",'r')))
window=Tk()
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
   if sys.argv and settings.get("speak_console_text_write")==True:
      print(text)
   engine.say(text)
   engine.runAndWait()

class AnkaSpark():
   def __init__(self,argv):
      super(AnkaSpark, self).__init__()
      self.init_ui()
      self.argv=argv

   def init_ui(self):
      window.title(settings.get("screen").get("title"))
      window.geometry(settings.get("screen").get("width_and_height"))

   def cli(self):
      print(settings)

   def platformWindows(self):
      import winreg
      print("Running Windows Platform....")

   def run(self):
     if platform.system()=="Windows":
      self.platformWindows()
     if self.argv:
       self.cli()
     else:
      #window.mainloop()
      print("Running UI")

if __name__ == '__main__':
   ai=AnkaSpark(sys.argv[1::])
   ai.run()
