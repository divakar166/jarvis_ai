from playsound import playsound
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
# import cv2                           #    pip install opencv-python
import random
import pywhatkit as kit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)




class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        playsound('jarvis.mp3')

    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
        #  ______Wish The Time _____

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("Hey!I am Jarvis Sir. Please tell me how may I help you sir ")

    def takeCommand(self):
        # ____ It takes microphone input from the user and returns string output

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
            # print(e)
            print("Say that again please...")
            return "None"
        return query
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startTask()

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\173836.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\spheres-motion-for-ai-product-design-by-gleb-large.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.label_2.setHidden(True)
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\radiohalo-800.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\Hologram 3.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\f8903ad1904347df9561656bcfa8918e_w200.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\vashishtha\\Downloads\\New\\75lD.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

#     takeCommand()
# if __name__ == "__main__":
    # while True:
    #     query = takeCommand().lower()
    #     # a = takeCommand().lower()
    #     if 'quit' in query or 'close' in query or 'exit' in query or 'quit jarvis' in query or 'close jarvis' in query or 'exit jarvis' in query or 'bye' in query or 'bye jarvis' in query:
    #         speak("Thank you Sir for your time .  !!!! Have a nice day. ...")
    #         break
    #     elif 'hello' in query or 'hello jarvis' in query or 'hi jarvis' in query or 'hi' in query or 'hey jarvis' in query or 'hey' in query:
    #         speak("Hello Sir...!!!!  How are you ?")
    #         break
    #     if 'wikipedia' in query:
    #         speak('Searching Wikipedia.......')
    #         query = query.replace("wikipedia", "")
    #         results = wikipedia.summary(query, sentences=2)
    #         speak("According to Wikipedia ")
    #         print(results)
    #         speak(results)
    #         # ____ Open system Software______#
    #     elif 'send message' in query:
    #         pywhatkit.sendwhatmsg("+916395047573", "Hello from GeeksforGeeks", 12,30)
    #         print("Successfully Sent!")
    #
    #     elif 'open notepad' in query:
    #         npath = "C:\\Windows\\system32\\notepad.exe"
    #         os.startfile(npath)
    #     elif 'open wordpad' in query:
    #         npath = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
    #         os.startfile(npath)
    #     elif 'open cmd' in query:
    #         os.system("Start cmd")
    #     elif 'open control panel' in query:
    #         kpath = "C:\\Users\\RS\\AppData\\Roaming\\Microsoft\\Windows\\Start\\control panel.exe"
    #         os.system("kpath")
    #
    #
    #         # __add new module___   ___
    #     # elif 'open camera' in query:
    #     #     cap=cv2.VideoCapture(0)
    #     #     while True:
    #     #         ret,img = cap.read()
    #     #         cv2.imshow('webcam',img)
    #     #         k=cv2.waitkey(50)
    #     #         if k==27:
    #     #             break
    #     #     cap.release()
    #     #     cv2.destroyAllWindow()
    #
    #     elif 'play music' in query:
    #         music_dir = "C:\\Users\\vashishtha\\Music"  # ___Create a  directory_____(Path of Play music)
    #         songs = os.listdir(music_dir)
    #         # rd=random.choice(songs)
    #         # os.startfile(os.path,join(music_dir,rd))                       #_>>  Import random number
    #         os.startfile(os.path.join(music_dir, songs[0]))  # _0->  Zero is a indexing number of play musio__
    #
    #
    #
    #
    #         # elif 'how are you' in query:
    #         #     speak("i'm fine, how's your day going ?")
    #         # elif 'good' in query:
    #         #     speak("sound good. | let me know of you need anything. ")
    #         # elif 'ok' in query:
    #         #     speak("okk  !!!  Sir  ")
    #         # elif 'who are you' in query:
    #         #     speak("i am a Virtual assistant created by priyanshu !!!  ")
    #         # elif 'who is salman khan' in query:
    #         #     speak("salman khan is a heavy driver")
    #         # elif 'what are you doing friday ' in query:
    #         #     speak("i am searching for your favorite songs ")
    #         # elif 'thanks you ' in query:
    #         #     speak("  Welcome Sir !!! ... .")
    #     elif 'the time' in query:
    #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
    #         speak(f"Sir, the time is {strTime}")
    #
    #     elif 'how are you' in query:
    #         speak("i'm fine, how's your day going ?")
    #
    #     elif 'good' in query:
    #         speak("sound good. | let me know of you need anything. ")
    #     elif 'ok' in query:
    #         speak("okk")
    #
    #     elif 'who are you' in query:
    #         speak("i am a Virtual assistant created by priyanshu !!!  ")
    #
    #     elif 'who is salman khan' in query:
    #         speak("salman khan is a heavy driver")
    #
    #     elif 'what are you doing jarvis' in query:
    #         speak("i am searching for your favorite songs ")
    #     elif 'thanks you jarvis ' in query:
    #         speak("Welcome Priyanshu !!! ... .")
    #
    #
    #
    #         # ________Wekipedia__  __
    #
    #
    #
    #     # elif "send massege" in query:  ##  install new module __ import pywhatkit
    #     #     pywhatkit.sendwhatmsg("+918279356365", "hello brother is this first  jarvis Project", 12, 18)
    #
    #
    #
    #
    #     elif 'open youtube' in query:
    #         webbrowser.open("www.youtube.com")
    #
    #     elif 'open my website' in query:
    #         webbrowser.open("prilit.unaux.com")
    #
    #     elif 'open facebook' in query:
    #         webbrowser.open("www.facebook.com")
    #
    #     elif 'open google' in query:
    #         webbrowser.open("www.google.com")
    #         # _ Search then google so command out this line
    #
    #         speak("sir,what should i search on google")  # __this functio is usng
    #         cm = takeCommand().lower()  # ___command out  this line
    #         webbrowser.open(f"{cm}")  # ____This line is command
    #
    #
    #
    #
    #     elif 'open stackoverflow' in query:
    #         webbrowser.open("stackoverflow.com")
    #
    #         # _____  Send SMS _____
    #
    #     # def sendEmail(to, content):                         #   No send Email And in Send SMS in Number
    #     #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     #     server.ehlo()
    #     #     server.starttls()
    #     #     server.login('youremail@gmail.com', 'your-password')
    #     #     server.sendmail('youremail@gmail.com', to, content)
    #     #     server.close()
    #     #
    #     # elif 'play music' in query:
    #     #     music_dir = 'F:\All Programs'
    #     #     songs = os.listdir(music_dir)
    #     #     print(songs)
    #     #     os.startfile(os.path.join(music_dir, songs[0]))
    #
    #     #
    #     # elif 'open code' in query:
    #     #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    #     #     os.startfile(codePath)
    #
    #     # __________Emial Send ____________
    #     #
    #     # elif 'email to Priyanshu' in query:
    #     #     try:
    #     #         speak("What should I say?")
    #     #         content = takeCommand()
    #     #         to = "princekumar228535@gmail.com"
    #     #         sendEmail(to, content)
    #     #         speak("Email has been sent!")
    #     #     except Exception as e:
    #     #         print(e)
    #     #         speak("Sorry my friend . I am not able to send this email")
