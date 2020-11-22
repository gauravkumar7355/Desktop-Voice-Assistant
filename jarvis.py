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
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from lsHotword import ls
from tensorflow.keras.callbacks import ModelCheckpoint

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)
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

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    def run(self):
        self.JARVIS()
    def takeCommand(self):
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
        wishMe()
        while True:
            ls.lsHotword_loop()
            self.query = self.takeCommand().lower()

            # logic for executing task based on query
            if 'wikipedia' in self.query:
                speak('Searching wikipedia')
                query = query.replace('wikipedia','')
                results = wikipedia.summary(query, sentences=2)
                speak('According to wikipedia')
                print(results)
                speak(results)
            if 'open youtube' in self.query:
                webbrowser.open('www.youtube.com')

            elif 'open google' in self.query:
                webbrowser.open('google.com')

            elif 'open stack overflow' in self.query:
                webbrowser.open('stackoverflow.com')

            elif 'search' in self.query:
                speak('Searching'+ query)
                webbrowser.open_new_tab(query)
                
                
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir = 'D:\\songs'
                self.songs = os.listdir(self.music_dir)
                random = os.startfile(os.path.join(self.music_dir, songs[1]))
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
            elif 'exit'in self.query:
                speak("Thanks for giving me your time , have a nice day sir")
                exit()
            elif "who made you" in self.query or "who created you" in self.query or "who is your master" in query:
                speak("I have been created by Gaurav Thakur")
            elif "joke" in self.query:
                speak(pyjokes.get_joke())
            elif 'empty recycle bin' in self.query: 
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                speak("Recycle Bin Recycled")
            elif "restart" in self.query: 
                subprocess.call(["shutdown", "/r"]) 


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./jarvisGui.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exit.setStyleSheet("background-image:url(.D:/Jarvis/ui - Copy.png);\n"
        "border:none;")
        self.exit.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie(".D:/Jarvis/pic.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_44.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label_2.setPixmap(QPixmap(".D:/Jarvis/ui"))
        

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_()) 