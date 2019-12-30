import pyttsx3
import os
from playsound import playsound
from multiprocessing import Process
import keyboard  
from pydub import AudioSegment
from pydub.playback import play
import vlc 

def sayWords(dialog):
    engine = pyttsx3.init() # object creation
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[11].id)  # changes the voice
    engine.say(dialog)
    engine.runAndWait()

# def playMedia():
#     # sound = AudioSegment.from_file(os.getcwd()+"/music/Seorita - Shawn Mendes, Camila Cabello.mp3", format="mp3")
#     # last_5_seconds = sound[-10000:].fade_out(10000)
#     # play(last_5_seconds)
#     player = vlc.MediaPlayer(os.getcwd()+"/music/Seorita - Shawn Mendes, Camila Cabello.mp3")
#     player.play()

if __name__=="__main__":
    
    proc1 = Process(target=sayWords, args={"Hi there"})
    # proc2 = Process(target=playMedia)
    proc1.start()
    
    inpKey = input()

    if(inpKey == 's'):
        proc1.terminate()
        # proc2.start()

        player = vlc.MediaPlayer(os.getcwd()+"/music/Seorita - Shawn Mendes, Camila Cabello.mp3")
        player.play()

        inpKey = input()

        if(inpKey == 's'):
            player.pause()
            inpKey = input()

            if(inpKey == 's'):
                player.set_time(20000)
                player.play()
                print(str(player.get_length()))
    
    npKey = input()
