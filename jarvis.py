import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty("voices")

print(voices[1].id)

engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():

    hour= int(datetime.datetime.now().hour)

    if(hour>=0 and hour<=12):

         speak("good morning minhaj")

    elif(hour>12 and hour<18):

        speak("gud afternoon minhaj")


    else:
        speak("Good evening minhaj")


    speak("iam jemi. please tell me how i help u?")

    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recgninzing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:

        # print(e)

        speak("please say that again...")
        return "None"

    return query
        
    # it take input from microphone and retrun string output



def sendEmail(to, content):


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thisismyentertainmentss@gmail.com', 'password')
    server.sendmail('thisismyentertainmentss@gmail.com', to, content)
    server.close()

   


       
if __name__ == "__main__":

    wishme()
    while True:




        query =takeCommand().lower()
 
    
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


        elif 'open whatsapp' in query:
    
            webbrowser.open("whatsapp.com")

        elif 'movie' in query:

            music_dir ='G:\\movies'

            movies = os.listdir(music_dir)
            print(movies  )
            os.startfile(os.path.join(music_dir,movies[0]))

        elif 'bye' in query:

            break

        elif 'time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, THe time is {strtime}")


        elif 'code' in query:

            codepath="C:\\Users\\Minhaj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif "send email" in query:

            try:

                speak("what shoud i say")
                content =takeCommand()
                to="minhajsinanvp@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    
        elif "search" in query:

            query=query.replace("search","")
            webbrowser.open(f"{query}")

