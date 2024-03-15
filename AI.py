import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello Sir I am Optimus Prime S013x. Please tell me how can i help you.")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say it again plz...")
        return None
    return query 

if __name__ =="__main__":
    # speak("welcome master")
    # wishMe()
    # speak()
    # takeCommand()
    if 1: 
        query = takeCommand().lower()   #converting user query into lower case

        
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query =query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        elif 'open google' in query:
            webbrowser.open("google.com")

        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")            

        elif 'play music' in query:
            music_dir = "C:\\Users\\91892\\PycharmProjects\\python -jarvis\\JARVIS AI\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is{strTime}")
