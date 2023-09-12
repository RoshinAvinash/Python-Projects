import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

#Setting up voice engine
engine = pyttsx3.init('sapi5')
#Setting up voice
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice',voices[0].id) #For Female voice
#Making the AI speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wishing me
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <10:
        speak("Good Morning")
    elif hour >= 10 and hour < 16:
        speak("Good Afternoon")
    elif hour >= 16 and hour <19:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am your personal assistant and I can automate the boring stuff, so please let me know how I can help you..")
    
#Taking micrphone input from the user and return string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query} \n")
    except:
        speak("Hey!")
        speak("Say clearly please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()

    while True:
        question = takecommand().lower()

        #Logic for executing tasks.

        #To find out current time
        if 'time' in question or 'what is time' in question:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        #Searching in wikipedia
        elif 'wikipedia' in question:
            speak("Searching Wikipedia")
            question = question.replace("wikipedia","")
            results = wikipedia.summary(question,sentences=1)
            speak("According to wikipedia the summary is ")
            print(results)
            speak(results)
        
        #Opening vscode
        elif 'open code' in question or 'vs code' in question:
            codepath = "C:\\Users\\roshin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        #Opening youtube
        elif 'open youtube' in question :
            webbrowser.get('windows-default').open('http://www.youtube.com')
        
        #Opening Google
        elif 'open google' in question :
            webbrowser.get('windows-default').open('http://www.google.com')
        
        #Opening ChatGPT
        elif 'open chatgpt' in question or 'open chat gpt' in question:
            webbrowser.get('windows-default').open('https://chat.openai.com/')
        
        #Playing music
        elif 'play music' in question:
            music_dir = "C:\\Users\\roshin\\Music"
            songs = os.listdir(music_dir)
            n = len(songs)
            print(songs)
            random_number = random.randrange(n)
            os.startfile(os.path.join(music_dir, songs[random_number]))
        
        #For writing Quick notes
        #Having a file Quick_Notes.txt is important in the same directory before using this automation.
        elif 'write a note' in question or 'quick note' in question or 'notes' in question:
            speak("What should i write?")
            flag = True
            while flag:
                note = takecommand()
                if note == "None":
                    continue
                else:
                    file = open('Quick_Notes.txt', 'a')

                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(f"{strTime} :-\n")
                    file.write(f"{note}\n")
                    print("Written in the file")
                    file.close()
                    flag = False
        
        #For Quitting
        elif "quit" in question or "exit" in question:  
            speak("Bye bye, hope to see you soon, and have a nice day.")
            exit()
        
        elif question != "none":
            speak("Sorry, for now i can perform only few tasks")   