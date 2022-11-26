#------------- Modules Imported ------------

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
import re
import requests
import PyPDF2


#------------ Taking Voice Input ------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


#------------ Use voices[0] for male voice  &  voices[1] for female voice ------------
engine.setProperty('voice', voices[0].id)


#------------ Function for Assistant Speaking ----------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#------------ Function to Greet your Master ------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 12 :
        speak('Good Morning')
    elif hour >= 12 and hour <16 :
        speak('Good Afternoon')

    else :
        speak('Good Evening')
    speak('Pratibha maam and Ranjan Sir. I am your personal assistant, Please tell me how may I help you')


#------------ Function to Listen & Recognize ----------
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


#----------- Function to read -----------
def pdf_reader():
    book= open('C:\\Users\\Gaurav Thakur\\Downloads\\final.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book);
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book{pages}")
    pg=int(input("Please enter the page number: "))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    speak(text)
    
    

if __name__ == "__main__":
    clear = lambda : os.system('cls')
    clear()
    speak("Hello")
    wishMe()
    while True:
        query = takeCommand().lower()

        #------ logic for executing task based on query ------
        
        # --- search on wikipedia ---
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
            
        # --- Open Youtube ---
        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            
        # --- Open Google ---
        elif 'open google' in query:
            webbrowser.open('google.com')

        # --- Open StackOverflow ---
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        # --- Search query on Default webBrowser ---
        elif 'search' in query:
            speak('Searching'+ query)
            webbrowser.open_new_tab(query)
            
        # --- Weather in particular City ---
        elif 'weather' in query or 'tempature' in query:
            url= f"https://www.google.com/search?q={query}"
            k=requests.get(url)
            data=BeautifulSoup(k.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"The {query} is {temp}")
                
        # --- Read PDF ---
        elif "read pdf" in query:
            pdf_reader()  
            
        # --- Play Music fron local File
        elif 'play music' in query:
            music_dir = 'D:\\Music PlayList'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        
        # --- Current Time ---
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            
        # --- Exit from progrm ---
        elif 'exit'in query:
            speak("Thanks for giving me your time , have a nice day")
            exit()
            
        # --- Owner's Name ---
        elif "who made you" in query or "who created you" in query or "who is your master" in query:
            speak("I have been created by Group 8, under the guidence of Pratibha ma'am ")
            
        # --- For entertainment purpose ---
        elif "joke" in query:
            speak(pyjokes.get_joke())
            
        # --- Empty Recycle Bin ---
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")

        # --- Restart PC ---
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"])
            
#------------ End Of Program ------------
