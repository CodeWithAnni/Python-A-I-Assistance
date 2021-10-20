import pyttsx3
import speech_recognition as sr
import os
import time
import datetime
import sys
import pyautogui
import random
import playsound
import keyboard
import pywhatkit
from pywikihow import search_wikihow
import webbrowser
import requests
from bs4 import BeautifulSoup
import PyPDF4
from googletrans import Translator
from gtts import gTTS
import pyjokes
from pytube import YouTube
import wikipedia
from tkinter import *

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    print("")
    print(f">>>> Ether Said : {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("")

def TakeCommand():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("")
            print(">>>> Ether Is Listening....")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=7)

        try:
            print(">>>> Ether Is Recognizing....")
            print("")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f">>>> You Said : {query}\n")
        except:
            return ""
        return query.lower()
    except Exception as e:
        print("Plz Check That You Have Connected To Microphone Properly.")

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning Sir, It's {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon Sir, It's {tt}")
    else:
        speak(f"Good Evening Sir, It's {tt}")
    # speak("I am Online, Tell me how can I help you ?")

def TaskExe():

    def Music():
        speak("Tell Me The NamE oF The Song!")
        musicName = TakeCommand()

        if 'akeli' in musicName:
            os.startfile('E:\\Songs\\akeli.mp3')

        elif 'blanko' in musicName:
            os.startfile('E:\\Songs\\blanko.mp3')

        else:
            pywhatkit.playonyt(musicName)

        speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        speak("Your Command Has Been Completed Sir!")

    def Temp():
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} celcius")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = TakeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of The Place ")
            name = TakeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            speak("no problem sir")

    def Reader():
        speak("Tell Me The Name Of The Book!")

        name = TakeCommand()

        if 'india' in name:

            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf','rb')
            pdfreader = PyPDF4.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Pages In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("In Which Language , I Have To Read ?")
            lang = TakeCommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                speak(text)

        elif 'europe' in name:
            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf','rb')
            pdfreader = PyPDF4.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Pages In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("In Which Language , I Have To Read ?")
            lang = TakeCommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                speak(text)

    def CloseAPPS():
        speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        speak("Whats Your Command ?")
        comm = TakeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak("Done Sir")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        speak(Text)
        
    def ChromeAuto():
        speak("Chrome Automation started!")

        command = TakeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    def screenshot():
        speak("Ok Boss , What Should I Name That File ?")
        name1 = TakeCommand()
        name = name1 + ".png"
        path1 = "E:\\Kaushik Shresth\\Screenshots\\"+ name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("E:\\Kaushik Shresth\\Screenshots")
        speak("Here Is Your ScreenShot") 

    while True:

        query = TakeCommand()
        query = str(query)

        if 'hello' in query:
            # speak("Hello Sir , I Am Voice Assistant.")
            speak("Your Personal AI Assistant!")
            speak("How May I Help You?")

        elif 'how are you' in query:
            speak("I Am Fine Sir!")
            speak("Whats About YOU?")

        elif 'you need a break' in query:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak("Just Say Wake Up Jarvis!")
            break

        elif 'youtube search' in query:
            speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir!")

        elif 'website' in query:
            speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched!")

        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = TakeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat my word' in query:
            speak("speak Sir!")
            repeat = TakeCommand()
            speak(f"You Said : {repeat}")

        elif 'my location' in query:
            speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'alarm' in query:
            speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            speak("Video Downloaded")
            
        elif 'translator' in query:
            Tran()
        
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No speakable Data Available!")

        elif 'how to' in query:
            speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
            
        elif 'temperature' in query:
            Temp()

        elif 'read book' in query:
            Reader()

TaskExe()