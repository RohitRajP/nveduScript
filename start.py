import pyttsx3
import os
from gtts import gTTS
from playsound import playsound
from multiprocessing import Process

def playMusic():
    print("Started Audio")
    playsound(os.getcwd()+"/Seorita - Shawn Mendes, Camila Cabello.mp3")

def sayWords():
    
    engine.say("This folder containes:")
 

path = str(os.getcwd()).split('/')

currDir = path[len(path)-1]

if(currDir == 'nvedu'):
    currDir = 'root'

engine = pyttsx3.init() # object creation

""" RATE"""
engine.setProperty('rate', 100)     # setting up new voice rate
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)  # changes the voice
sayWords()
# procs2 = Process(target=sayWords)
# procs2.start()

# inputKey = input()

# if(inputKey == 'e'):
#     procs2.terminate()

os.chdir(os.getcwd()+"/music/")
print(os.getcwd())




procs = Process(target=playMusic)
procs.start() 

# playMusic()

inputKey = input()



if(inputKey == 'e'):
    procs.terminate()

inputKey = input()

# for dirName in os.listdir():
#     engine.say(dirName)
#     engine.runAndWait()