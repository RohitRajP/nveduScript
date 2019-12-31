import vlc 
import pyttsx3
import os
from multiprocessing import Process, Value, Array

def taskFun(testValue):
    print(str(testValue))
    testValue = 10
    
def printValue(testValue):
    print(str(testValue))

if __name__=="__main__":

    testValue = Value('i',0)

    proc1 = Process(target=taskFun, args={testValue})
    proc2 = Process(target=printValue, args={testValue})
    proc1.start()
    inputKey = input()
    proc1.terminate()
    proc2.start()
    inputKey = input()