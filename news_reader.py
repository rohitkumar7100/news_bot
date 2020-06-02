import pandas as pd
import pyttsx3
import datetime
import runner as r

import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def readfile_clean():
    data=pd.read_csv('Headlines_data.csv')
    return data

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("hi good morning")
    elif hour>=12 and hour <18:
        speak("hi good afternoon")
    else:
        speak("hey good evening")
    speak("I am a News Bot, My name is Disha, How may i help you")

def takecommand():
    '''
    if error of pyaudio, first install
    pip install pipwin
    then
    pipwin install pyaudio
    '''
    print("inside takecommand")
    r = sr.Recognizer()
    print("111")
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            speak("Sorry, Can you say that again")
            return "None"
        return query
        
def talking_bot():
    query=takecommand().lower()
    if 'disha' in query:
        wishMe()
        query=takecommand().lower()
        if 'latest news' in query:
            speak("Collecting Latest news, Please wait")
            
            
            r.scrap()
            a= readfile_clean()
            lst=a['HeadLine'].tolist()
            speak("Here are the top 10 news from india today")
            for i in lst:
                speak(i)
            speak("Thank you")

    elif 'stop' in query:
        speak("Bye Bye")
        exit()
    else:
        speak("are you talking to me.. call me disha")
        talking_bot()

if __name__ =="__main__":
    
    talking_bot()
        


