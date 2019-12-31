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
    sayWords("Now in: ")
    sayWords(str(os.getcwd()))

def moveOneFileForward(dirFiles,dirFilesIndex):
    sayWords(dirFiles[dirFilesIndex])

def moveOneFileBackward(dirFiles,dirFilesIndex):
    sayWords(dirFiles[dirFilesIndex])

if __name__=="__main__":

    dirFiles = []
    dirFilesIndex = 0

    listAllFilesProc = Process(target=listAllFiles)
    sayDirectoryProc = Process(target=sayDirectory)
    moveOneFileForwardProc = Process(target=moveOneFileForward)
    moveOneFileBackwardProc = Process(target=moveOneFileBackward)

    while True:

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
        elif(inputKey == "sa"):
            listAllFilesProc.terminate()
                