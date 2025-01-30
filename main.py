# filepath: /Users/shuvamghosh/Desktop/MyJervis/main.py
import os
import eel
import webbrowser
import subprocess

from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call(["/bin/bash", "device.sh"])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
    webbrowser.open("http://localhost:8000/index.html")

    eel.start('index.html', mode=None, host='localhost', block=True)

if __name__ == "__main__":
    start()