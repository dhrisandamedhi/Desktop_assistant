from typing import Dict
import pyttsx3      #pip install pyttsx3
import speech_recognition as sr     #pip install SpeechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import os 
import random
import smtplib

from wikipedia.wikipedia import search

d1 = {"Dhrisanda Medhi":"dhrisandamedhi37@gmail.com"}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")

    assist_name = "Sophia"
    speak(f"I am {assist_name}. Please tell me how can i help you sir?")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.energy_threshold = 600
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.........")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Unable to recognize your voice. Say that again please.........")
        speak("Unable to recognize your voice. Say that again please.")
        return "None"
    
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('dhrisandaoffical@gmail.com','dhrisanda1@')
    server.sendmail('dhrisandaoffical@gmail.com', to, content)
    server.close()

if __name__=="__main__" :
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 5)
            speak("Acording to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Sir, What should i search?")
            sq = takecommand().lower()
            url = 'https://www.youtube.com/search?q=' + sq
            webbrowser.get().open(url)

        elif 'open google' in query:
            speak("Sir, What should i search?")
            sq = takecommand().lower()
            url = 'https://www.google.com/search?q=' + sq
            webbrowser.get().open(url)
        elif 'break' in query or 'stop'in query:
            speak("i'm stopping now")
            print('Assistant stop')
            break
        elif 'open geeksforgeeks' in query:
            webbrowser.open('https://www.geeksforgeeks.org/')
        
        elif 'play music youtube' in query:
            webbrowser.open('https://www.youtube.com/watch?v=t8655cvDc48')

        elif 'time' in query:
            the_Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {the_Time}")
            print(f"Sir, the time is {the_Time}")

        elif 'play music' in query:
            music_dir = 'E:\\Videos\\'
            songs = os.listdir(music_dir)
            file = random.choice(songs)
            os.startfile('E:\\Videos\\' + file)

        elif 'open vs code' in query:
            vs_Path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_Path)
        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'who are you' in query:
            speak("I am Sophia sir")
        
        elif "stop" in query or "exit" in query or "end" in query or "close" in query:
            speak("Thanks for using me sir and take care and have a nice day sir")
            break

        elif 'send mail' in query or 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("whome should i send")
                t1 = takecommand().lower()
                to = d1.get(t1)
                sendEmail(to, content)
                print("Email has been sent !")
                speak("Email has been sent !")
            except Exception as e:
                print("I am not able to send this email")
                speak("I am not able to send this email")