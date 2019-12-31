import vlc 
import pyttsx3
import os
from multiprocessing import Process, Value

def sayWords(dialog):
    engine = pyttsx3.init() # object creation
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 120)
    engine.setProperty('voice', voices[11].id)  # changes the voice
    engine.say(dialog)
    engine.runAndWait()


def listAllFiles():
    sayWords("Listing all files: ")
    for fileName in os.listdir():
        if(str(fileName) == "run.py"):
            continue
        sayWords(str(fileName))

def sayDirectory():
    sayWords("Now in: "+str(os.getcwd()).split('/').pop())

def moveOneFileForward(dirFiles,dirFilesIndex):
    sayWords(dirFiles[dirFilesIndex])

def moveOneFileBackward(dirFiles,dirFilesIndex):
    sayWords(dirFiles[dirFilesIndex])
    
def moveForward(dirFiles,dirFilesIndex):
    sayWords("Now in: "+str(os.getcwd()).split('/').pop())

def moveBackward():
    sayWords("Now in: "+str(os.getcwd()).split('/').pop())

if __name__=="__main__":

    dirFiles = []
    dirFilesIndex = 0

    listAllFilesProc = Process(target=listAllFiles)
    sayDirectoryProc = Process(target=sayDirectory)
    moveOneFileForwardProc = Process(target=moveOneFileForward)
    moveOneFileBackwardProc = Process(target=moveOneFileBackward)
    moveForwardProc = Process(target=moveForward)
    moveBackwardProc = Process(target=moveBackward)

    while True:

        dirFiles = []

        for fileName in os.listdir():
            dirFiles.append(fileName)

        inputKey = input()
        
        if(listAllFilesProc.is_alive() == True):
            listAllFilesProc.terminate()
        elif(sayDirectoryProc.is_alive() == True):
            sayDirectoryProc.terminate()
        elif(moveOneFileForwardProc.is_alive() == True):
            moveOneFileForwardProc.terminate()
        elif(moveOneFileBackwardProc.is_alive() == True):
            moveOneFileBackwardProc.terminate()
        elif(moveForwardProc.is_alive() == True):
            moveForwardProc.terminate()
        elif(moveBackwardProc.is_alive() == True):
            moveBackwardProc.terminate()

        if(inputKey == "l"):
            listAllFilesProc = Process(target=listAllFiles)
            listAllFilesProc.start()
        elif(inputKey == "n"):
            sayDirectoryProc = Process(target=sayDirectory)
            sayDirectoryProc.start()
        elif(inputKey == "e"):
            if(dirFilesIndex < len(dirFiles)-1):
                dirFilesIndex+=1
            else:
                dirFilesIndex=0
            moveOneFileForwardProc = Process(target=moveOneFileForward, args=(dirFiles,dirFilesIndex))
            moveOneFileForwardProc.start()
        elif(inputKey == "q"):
            if(dirFilesIndex > 0):
                dirFilesIndex-=1
            else:
                dirFilesIndex=len(dirFiles)-1
            moveOneFileBackwardProc = Process(target=moveOneFileBackward, args=(dirFiles,dirFilesIndex))
            moveOneFileBackwardProc.start()
        elif(inputKey == "c"):
            if(dirFiles[dirFilesIndex].find(".mp3") == -1):
                os.chdir(str(os.getcwd())+"/"+dirFiles[dirFilesIndex])
                moveForwardProc = Process(target=moveForward, args=(dirFiles,dirFilesIndex))
                moveForwardProc.start()
            else:
                print("playing music")
                player = vlc.MediaPlayer(str(os.getcwd())+"/"+dirFiles[dirFilesIndex])
                player.play()
        elif(inputKey == "z"):
            os.chdir('..')
            moveBackwardProc = Process(target=moveBackward)
            moveBackwardProc.start()


        
                