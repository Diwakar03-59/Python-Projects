import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[2].id)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said ", query)
        
    except Exception() as e:
        print("Say that again please !")
        return "None"
    
    return query
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening")
        
    speak("Hi ,I am Papaa Ki Parie. Your personal assistant. How may I assist you")
    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #to give the results of the query
        
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            speak("Searching Wikipedia...")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia ")
            print(results)
            speak(results)
            
            
        if "gaana" in query:
            speak("opening gaana music..")
            webbrowser.get(chrome_path).open("gaana.com")
            
            
        if "swayam" in query:
            speak("opening Swayam..")
            webbrowser.get(chrome_path).open("swayam.gov.in")
            
            
        if "makaut" in query:
            speak("opening makaut...")
            webbrowser.get(chrome_path).open("makaut1.ucanapply.com/smartexam/public/")
            
        
        if "whatsapp" in query:
            speak("opening whatsapp...")
            webbrowser.get(chrome_path).open("web.whatsapp.com")
            
            
        if "gmail" in query:
            speak("opening gmail..")
            webbrowser.get(chrome_path).open("accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            
        if "internshala" in query:
            speak("opening internshala..")
            webbrowser.get(chrome_path).open("internshala.com")
            
        if "songs" in query:
            speak("playing downloaded songs")
            music_dir = 'E:\\downloaded songs'
            r = random.randint(0,29)
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[r]))
            
        if "spyder" in query:
            path = 'C:\\Users\DEEPAKKUMAR\\anaconda3\\pythonw.exe'
            speak("opening spyder")
            os.startfile(path)
            
        if "bluej" in query:
            path = "C:\\Program Files (x86)\\BlueJ\\BlueJ.exe"
            speak("opening bluej")
            os.startfile(path)
            
        if "youtube" and "music" in query:
            speak("opening youtube music")
            webbrowser.get(chrome_path).open("music.youtube.com")
            break
            
        
        if "youtube" in query:
            speak("Opening Youtube..")
            webbrowser.get(chrome_path).open("youtube.com")
            
        if "genie" in query:
            path1 = "C:\\Program Files (x86)\\Geany\\bin\\geany.exe"
            speak("opening geany ")
            os.startfile(path1)
            
        if "c programming" in query:
            path3 = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            speak("opening dev c++")
            os.startfile(path3)
            
        if "sublime text" in query:
            path4 = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            speak("opening sublime text 3")
            os.startfile(path4)
            
        if "who are you" in query:
            speak("I am Hazel assistant.")
            
        if "play goat" in query:
            speak("Playing goat by Diljit Dosanjh")
            path5 = "C:\\Users\\DEEPAKKUMAR\\Music\\Playlists\\GOAT.mp3"
            os.startfile(path5)
        
            
            
            
            
            
            
        
            
        
            
            
            
            

    
