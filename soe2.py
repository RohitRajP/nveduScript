import vlc 
import pyttsx3
import os
from multiprocessing import Process

if __name__=="__main__":

    engine = pyttsx3.init() # object creation
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 100)
    engine.setProperty('voice', voices[11].id)  # changes the voice
    engine.say("Hello")
    engine.runAndWait()