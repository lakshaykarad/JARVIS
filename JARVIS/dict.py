import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dict = {"commandprompt": "cmd", "paint": "mspaint", "word": "winword", "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt"}

def opeappweb(query):
    speak("Launching,Sir")
    
    if '.com' in query or '.co.in' in query or '.in' in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
        
    else:
        key = list(dict.keys())
        for app in key:
            if app in query:
                os.system(f"start {dict[app]}")

 

def closeapp(query):
    speak("Closing, Sir")
    
    tabs_to_close = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    for key, value in tabs_to_close.items():
        if f'{key} tab' in query or f'{value} tab' in query:
            for _ in range(value):
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
            speak("All tabs closed")
            return
    
    key = [app for app in dict if app in query]
    if key:
        os.system(f"taskkill /f /im {dict[key[0]]}.exe")
