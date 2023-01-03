import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[1].id)


obj = JarvisAI.JarvisAssistant()


def t2s(text):
    obj.text2speech(text)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        

    speak("I am BixBy sir! How can I help You")

def takeCommand():
    #It takes micropone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said : {query}\n")
    
    except Exception as e:
       print(e)
       print("Say that again please....")
       return "None"
    return query

if __name__ == "__main__":
    speak("Hello Everyone")
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('Wikipedia','')
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'open stack over flow' in query:
            webbrowser.open("Stack over flow.com")

        elif 'play music' in query:
            music_dir='F:\\TY\\TY 5 sem\\Mega Project\\music_dir'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            now = datetime.datetime.now()
            strTime = print (now.strftime("%Y-%m-%d %H:%M:%S"))
            print ("Current date and time : ")
            speak(f"Sir, the time is{strTime}")
             
        elif 'open code' in query:
           codepath= "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)
           
    
        res = obj.mic_input()

        elif re.search('news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        t2s(news_res[0])
        t2s(news_res[1])

        else 'Exit' in query:
            Exit()



 
        

    

    
     
