import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import subprocess
import smtplib
import pyjokes
import ctypes
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good Morning! ")
    elif hour >= 12 and hour < 18:
        speak("good AfterNoon! ")
    else:
        speak("good Evening! ")


    speak("I am Anny Your Virtual Assistant please Tell me How may I help You")

def takecommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
         
        print("Listening.....")
        r.pause_threshold = 1
        audio= r.listen(source)
    try:
        print("Recognizing......")  
        query= r.recognize_google(audio, language='en-in')  
        print(f"user said :{query}\n")
    
    except Exception as e:
          print (e)
          print("Say that again please...") 
          return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:    
       query = takecommand().lower()
        
       if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
       
       elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")     

       elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
       elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Thanks for naming me")
 
       elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
       elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
       elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown')
                 
       elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
       elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)
 
       elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
     #   elif "camera" in query or "take a photo" in query:
     #        ec.capture(0, "Jarvis Camera ", "img.jpg")
 
       elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
       elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
       elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
       elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('anny.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
       elif "note" in query:
            speak("Showing Notes")
            file = open('anny.txt',"r")
            print(file.read())
            speak(file.read(6))



       elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

       elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       elif 'open code' in query:
            codePath = "D:\project\anny.py"
            os.startfile(codePath)
 
       elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Anny")
            

       elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
       elif "who are you" in query:
            speak("I am your virtual assistant Anny created by Anon")
 
       elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Anon ")

       elif "who made you" in query or "who created you" in query:
            speak("I have been created by Anon.")
       
       elif 'fine' in query or "am good" in query:
            speak("It's good to know that your fine")     

       elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
       elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Thanks for naming me")
 
 
       elif "how are you" in query:
            speak("I'm fine, glad you me that")
      
       elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
       elif "why you came to world" in query:
            speak("Thanks to ANoN . further It's a secret")

       elif "my gf" in query or " my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
       elif "i love you" in query:
            speak("It's hard to understand") 

       elif "do you love me" in query:
            speak("I am always available for you My Dear")      
              
       elif "funny" in query:
            speak("Thank you My Dear")      

       elif "tired" in query:
            speak("you need some rest. go get some sleep ")        

       elif "bored" in query:
            speak("do you want listen music or want to listen a joke ")  
                  
       elif " good person" in query or "gentle" in query:
            speak("You are the sweetest person in this World  ")  

       elif 'Who is Anon' in query:
            speak("My creator  My owner ")
             
       elif 'joke' in query:
            speak(pyjokes.get_joke())
 
       elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
       
       elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "anamikakr238@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry Mr  Anon. I am not able to send this email")  



                from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('annyVirtualAsstiant.html')

@app.route('/execute-python', methods=['POST'])
def execute_python():
    try:
        subprocess.run(["python", "app.py"], check=True)
        return "Python file executed successfully!"
    except subprocess.CalledProcessError:
        return "Error executing Python file!"

if __name__ == "__main__":
    app.run(debug=True)
