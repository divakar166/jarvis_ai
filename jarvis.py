# from playsound import playsound
import sys
import time
import pywhatkit
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import pywhatkit as kit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import Ui_MainWindow
from datetime import datetime
import urllib.request
import urllib.parse
import re
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
now = datetime.now()

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        self.wishMe()
        self.querySolver()

    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe(self):
        hour = int(datetime.now().hour)
        if 0 <= hour < 12:
            print("Good Morning!")
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            print("Good Afternoon!")
            self.speak("Good Afternoon!")
        else:
            print('Good Evening!')
            self.speak("Good Evening!")
        print('Hey!I am Zero. Please tell me how may I help you,Sir!')
        self.speak("Hey!I am Zero. Please tell me how may I help you,Sir!")

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=2, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

    def querySolver(self):
        while True:
            query = self.takeCommand().lower()
            if 'quit' in query or 'exit' in query or 'quit Zero' in query or 'exit Zero' in query or 'bye' in query or 'bye Zero' in query:
                self.speak("Thank you Sir for your time .  !!!! Have a nice day. ...")
                break
            elif 'hello' in query or 'hello Zero' in query or 'hi Zero' in query or 'hi' in query or 'hey Zero' in query or 'hey' in query:
                self.speak("Hello Sir...!!!!  How are you ?")
            elif 'good' in query or 'i am fine' in query:
                self.speak("That's good,Sir")
            elif 'how are you' in query:
                self.speak("i'm fine, how are you doing?")
            elif 'good' in query:
                self.speak("sound good. let me know if you need anything. ")
            elif 'ok' in query:
                self.speak("okay")
            elif 'who are you' in query:
                self.speak("i am a virtual assistant. Can do certain things/")
            elif 'wikipedia' in query:
                self.speak('Searching Wikipedia.......')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia ")
                print(results)
                self.speak(results)
            elif 'send message' in query:
                pywhatkit.sendwhatmsg("+916395047573", "Hello from GeeksforGeeks", now.hour, now.minute+1)
                print("Successfully Sent!")
            elif 'open notepad' in query:
                self.speak('Opening Notepad')
                os.system("start notepad")
            elif 'close notepad' in query:
                self.speak("Closing Notepad")
                os.system("taskkill /f /im notepad.exe")
            elif 'open wordpad' in query:
                self.speak("Opening Wordpad")
                os.system("start wordpad")
            elif 'close wordpad' in query:
                self.speak("Closing Wordpad")
                os.system("taskkill /f /im wordpad.exe")
            elif 'open excel' in query:
                self.speak("Opening MS Excel")
                os.system("start excel")
            elif 'close excel' in query:
                self.speak("Closing MS Excel")
                os.system("taskkill /f /im excel.exe")
            elif 'open powerpoint' in query:
                self.speak("Opening PowerPoint")
                os.system("start powerpnt")
            elif 'close powerpoint' in query:
                self.speak("Closing powerpoint")
                os.system("taskkill /f /im powerpnt.exe")
            elif 'open access' in query:
                self.speak("Opening MS Access")
                os.system("start msaccess")
            elif 'close access' in query:
                self.speak("Closing MS Access")
                os.system("taskkill /f /im msaccess.exe")
            elif 'open browser' in query:
                self.speak("Opening Browser")
                os.system("start chrome")
            elif 'close browser' in query:
                self.speak("Closing Browser")
                os.system("taskkill /f /im chrome.exe")
            elif 'open chrome' in query:
                self.speak("Opening Chrome")
                os.system("start chrome")
            elif 'close browser' in query:
                self.speak("Closing Browser")
                os.system("taskkill /f /im chrome.exe")
            elif 'open calculator' in query:
                self.speak("Opening Calculator")
                os.system("start calc")
            elif 'close calculator' in query:
                self.speak("Closing Calculator")
                os.system("taskkill /f /im calculator.exe")
            elif 'open firefox' in query:
                self.speak("Opening Firefox")
                os.system("start firefox")
            elif 'close firefox' in query:
                self.speak("Closing firefox")
                os.system("taskkill /f /im firefox.exe")
            elif 'open control panel' in query or 'control panel' in query:
                self.speak("Opening Control Panel")
                os.system("start control panel")
            elif 'open camera' in query:
                self.speak("Opening Camera")
                print("Opening Camera")
                os.system("start microsoft.windows.camera:")
            elif 'close camera' in query:
                self.speak("Closing Camera")
                os.system("taskkill /f /im windowscamera.exe")
            elif 'time' in query or 'what is time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak(f"Sir, the time is {strTime}")
            elif 'who is salman khan' in query:
                self.speak("salman khan is a heavy driver")
            elif 'what are you doing Zero' in query:
                self.speak("i am searching for your favorite songs ")
            elif 'thank you Zero' in query or 'thank you' in query:
                self.speak("Welcome Sir !!! ... .")
            elif 'play' in query or 'youtube' in query or 'in youtube' in query or 'on youtube' in query:
                dec = {"on youtube":"","in youtube":"","youtube":""," ":"+","play":""}
                for key,value in dec.items():
                    query = query.replace(key,value)
                query_string = urllib.parse.urlencode({"search_query": f"{query}"})
                html_content = urllib.request.urlopen("https://www.youtube.com.hk/results?" + query_string)
                search_results = re.findall(r'url\"\:\"\/watch\?v\=(.*?(?=\"))', html_content.read().decode())
                if search_results:
                    webbrowser.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
            elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")
            elif 'how are you' in query:
                speak("i'm fine, how's your day going ?")
            elif 'good' in query:
                speak("sound good. let me know if you need anything. ")
            elif 'ok' in query:
                speak("okk  !!!  Sir  ")
            elif 'who are you' in query:
                speak("I am a virtual assistant created to do certain tasks.")
            elif 'who is salman khan' in query:
                speak("salman khan is a heavy driver")
            elif 'what are you doing zero ' in query:
                speak("i am learning something new!")
            elif 'open spotify' in query or 'spotify' in query:
                self.speak("Opening Spotify!")
                webbrowser.open("www.open.spotify.com")
            elif 'on google' in query or 'in google' in query or 'google' in query:
                g_dec = {"in google":"","on google":"","google":""," ":"+"}
                for key,value in g_dec.items():
                    query = query.replace(key,value)
                webbrowser.open("www.google.com/search?q="+f"{query}")
            elif 'who is' in query:
                self.speak('Searching Wikipedia.......')
                query = query.replace("who is","")
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia ")
                print(results)
                self.speak(results)
            elif 'what is' in query:
                self.speak('Searching Wikipedia.......')
                query = query.replace("what is","")
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia ")
                print(results)
                self.speak(results)
            elif 'open stackoverflow' in query:
                webbrowser.open_new("stackoverflow.com")
            elif 'open' in query:
                self.speak("What should I open, Sir!")
            elif '' in query:
                self.speak('Anything for me, Sir!')
            else:
                self.speak("Say that again please!")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startTask()

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\Zero.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.pushButton.clicked.connect(self.startMainTask)

    def startMainTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\d13449fb76b34cb71584f5bfb7c6dee9.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\59d39ea8cfb59-unscreen.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\radiohalo-800.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()
        self.ui.pushButton.setText("STOP")
        self.ui.pushButton.clicked.connect(self.stopMainTask)

    def stopMainTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\d13449fb76b34cb71584f5bfb7c6dee9.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.stop()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\59d39ea8cfb59-unscreen.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.stop()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\radiohalo-800.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.stop()
        startExecution.stop()

app = QApplication(sys.argv)
Zero = Main()
Zero.show()
exit(app.exec_())
