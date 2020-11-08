import pyttsx3
import datetime
import tkinter
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
from bs4 import BeautifulSoup
import winshell
import subprocess
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 12 :
        speak('Good Morning')
    elif hour >= 12 and hour <16 :
        speak('Good Afternoon')

    else :
        speak('Good Evening')
    speak('I am jarvis sir, Please tell me how may I help you')

def takeCommand():
    # it take microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Say that again plese.....')
        return 'None'
    return query

if __name__ == "__main__":
    clear = lambda : os.system('cls')
    clear()
    speak("Hello Sir")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'search' in query:
            speak('Searching'+ query)
            webbrowser.open_new_tab(query)
            
            
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'exit'in query:
            speak("Thanks for giving me your time , have a nice day sir")
            exit()
        elif "who made you" in query or "who created you" in query or "who is your master" in query:
            speak("I have been created by Gaurav Thakur")
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")

        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 