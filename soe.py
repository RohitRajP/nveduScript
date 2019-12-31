import vlc 
import pyttsx3
import os
from multiprocessing import Process


def sayWords(dialog):
    engine = pyttsx3.init() # object creation
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 120)
    engine.setProperty('voice', voices[11].id)  # changes the voice
    engine.say(dialog)
    engine.runAndWait()


def listAllFiles():
    sayWords("Listing all subfiles: ")
    for fileName in os.listdir():
        sayWords(str(fileName))


if __name__=="__main__":

    while True:

        inputKey = input()

        if(inputKey == "l"):
            listAllFiles()