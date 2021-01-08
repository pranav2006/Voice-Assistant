import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
import json
import requests
import smtplib
    ######################  random   ######################
my_name = "my name is ultron"

creator = "my creator name is pranav"
    ###########################  audio  #########################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

    #print(voices)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("Good Morning!")


    elif hour>=12 and hour<18:
        speak("Good Afternoon!")


    else:
        speak("Good Evening!")

    speak("How May I Help You Sir")


def takeCommand():
        #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening...")
        print("listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        speak("WAIT A MOMENT")
        print("wait a moment...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception as e:
        print(e)
        speak("pardon,please say that again...")
        print("pardon,please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    while True:
        # if 1:
        query = takeCommand().lower()

            # for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.co.in/")
            speak('opening youtube please wait for some seconds')

        elif 'google' in query:
            webbrowser.open("https://www.google.co.in/")
            speak('opening google please wait for some seconds')

        elif 'flow' in query:
            webbrowser.open("https://stackoverflow.com/")
            speak('opening stack over flow please wait for some seconds')

        elif 'hub' in query:
            webbrowser.open("https://github.com/")
            speak('opening github please wait for some seconds')

        elif 'reddit' in query:
            webbrowser.open("https://www.reddit.com/")
            speak('opening reddit please wait for some seconds')

            ##songs using random func

        elif 'play' in query or 'hit it' in query:
            try:
                music_dir = 'E:\\songs'
                songs = os.listdir(music_dir)
                lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
                try:
                    music_dir = 'E:\\songs'
                    songs = os.listdir(music_dir)
                    lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
                    print("5th")
                    choose_song = random.choice(lst)
                    os.startfile(os.path.join(music_dir, songs[choose_song]))
                    try:
                        music_dir = 'E:\\songs'
                        songs = os.listdir(music_dir)
                        lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
    
                        choose_song = random.choice(lst)
                        print("1st")
                    except:
                        try:
                            music_dir = 'E:\\songs'
                            songs = os.listdir(music_dir)
                            lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
    
                            choose_song = random.choice(lst)
                            print("2nd")
                        except:
                            try:
                                music_dir = 'E:\\songs'
                                songs = os.listdir(music_dir)
                                lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
    
                                choose_song = random.choice(lst)
                                print("3rd")
                            except:
                                try:
                                    music_dir = 'E:\\songs'
                                    songs = os.listdir(music_dir)
                                    lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
    
                                    choose_song = random.choice(lst)
                                    print("4th")
                                except:
                                    print("1 more time")
                                
                except:
                    music_dir = 'E:\\songs'
                    songs = os.listdir(music_dir)
                    lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
                    print("5th")
                    choose_song = random.choice(lst)
                os.startfile(os.path.join(music_dir, songs[choose_song]))
                
            speak("nice song")
            ## stoping the song

            #changing music
        elif 'next' in query:
            speak("changing music")
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            a = random.choice(lst)
            os.startfile(os.path.join(music_dir, songs[a]))




            #opening apps and closing apps
    ######################################   opening android studio   ###################################################

        elif 'open android studio' in query:
            codepath = "C:\\Program Files\\Android\\Android Studio1\\bin\\studio64.exe"
            os.startfile(codepath)
            speak("opening android studio")
            time.sleep(10)
            speak("sucessfully opened")

    #####################################  closing android studio  ####################################################
        elif 'close android studio' in query:
            speak("closing android studio")
            os.system("TASKKILL /F /IM studio64.exe")
            speak("sucessfully closed android studio")
    #####################################  opening vs code   ########################################################

        elif 'open vs' in query or 'open visual studio code' in query:
            codepath = "C:\\Users\\pp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("opening Visual Studio Code")
            time.sleep(5)
            speak("sucessfully opened")

    #####################################  closing vs code   ########################################################

        elif 'close vs' in query or 'close visual studio code' in query:
            speak("closing Visual Studio Code")
            os.system("TASKKILL /F /IM Code.exe")
            speak("sucessfully closed Visual Studio Code")

    ####################################   opening vm ware   #######################################################



    ################################## closing chrome   ###########################################################






    ###############################################################################################################

        elif 'what is your name' in query or 'who are you' in query:
            speak(my_name)

        elif 'creator' in query:
                speak(creator)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
    ##################################################### opening varoius files   ################################################
        elif 'english' in query:
            speak("opening file")
            movies_dir = 'F:\\ENGLISH'
            movies = os.listdir(movies_dir)
            file = os.startfile(movies_dir)

        elif 'marvel' in query:
            speak("opening file")
            movies_dir = 'F:\\ENGLISH\\marvel'
            movies = os.listdir(movies_dir)
            file = os.startfile(movies_dir)

        elif 'harry potter' in query:
            speak("opening file")
            movies_dir = 'F:\\ENGLISH\\harry potter'
            movies = os.listdir(movies_dir)
            file = os.startfile(movies_dir)


        elif 'malayalam' in query:
            speak("opening file")
            movies_dir = 'F:\\MALAYALAM'
            movies = os.listdir(movies_dir)
            file = os.startfile(movies_dir)

        elif 'hindi' in query:
            speak("opening file")
            movies_dir = 'F:\\HINDI'
            movies = os.listdir(movies_dir)
            file = os.startfile(movies_dir)


        elif 'coding' in query:
            speak("opening file")
            movies_dir = 'A:\\coding'
            movies = os.listdir(movies_dir)
            coding_file = os.startfile(movies_dir)


    #######################################################################################################################
        elif 'news' in query:
            speak("today's head line is")
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=6b3c6c1b013e4d18811081757c078e50"
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news["articles"]
            for articles in arts:
                speak(articles['title'])
                speak("next news is")
        ################################################
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pranavlg06@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
    ####################################  sleep  #######################################################################
        if 'sleep for 2 minutes' in query or 'sleep for 2' in query:
            randomm = ["yeah i really need a nap", "2 minutes", "see you in 2 minutes"]
            two = random.choice(randomm)
            speak(two)
            oo = 60*2
            time.sleep(oo)
            speak ("i am awake sir")

        if 'go to hell' in query:
            break

        if 'how are you' in query:
            speak("i am doing good")

        if 'sleep for 5 minutes' in query or 'sleep for 5' in query:
            two = ["yeah i really need a nap", "5 minutes", "see you in 5 minutes"]
            hh = random.choice(two)
            speak(hh)
            pr = 60*5
            time.sleep(pr)
            speak("i am awake sir")

        if 'sleep for 10 minutes' in query or 'sleep for 10' in query:
            jj = ["yeah i really need a nap", "10 minutes", "see you in 10 minutes"]
            kk = random.choice(jj)
            speak(kk)
            yy = 60*10
            time.sleep(yy)
            speak("i am awake sir")

        if 'sleep for 30 minutes' in query or 'sleep for 30' in query:
            llkb = ["yeah i really need a nap", "30 minutes", "see you in 30 minutes"]
            pppppppd = random.choice(llkb)
            speak(pppppppd)
            polpp = 60*30
            time.sleep(polpp)
            speak("i am awake sir")


        if 'sleep for 1 hour' in query or 'sleep for 1' in query:
            zx = 60*60
            time.sleep(zx)
            speak("it is been one hour")

        if 'movie time protocol' in query or 'movietime protocol' in query or 'movie' in query:
            speak("initializing movie time protocol")
            import winwifi
            winwifi.WinWiFi.disconnect()
            ll = 60*120
            time.sleep(ll)
            speak ("i am awake sir")
            speak("sir Connecting to wifi")

    ########################  break the programme   #########################################################################
        if 'goodnight' in query:
            strTime = datetime.datetime.now().strftime("%H %M %S")
            speak("good night, sleep well sir")
            break

        if 'mute' in query:
            break

        if 'go offline' in query:
            speak('ok sir')
            speak('closing all systems')
            speak('disconnecting from servers')
            speak('going offline')
            break

        if 'good morning' in query or 'what''s up' in query:
            speak("good morning sir")
            time.sleep(0.55)
            speak("let me tell the news")
            time.sleep(2)
            speak("today's head line is")
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=6b3c6c1b013e4d18811081757c078e50"
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news["articles"]
            for articles in arts:
                speak(articles['title'])
                speak("next news is")
                speak("that is all for now")

    #$###############################  shut down and logout   ##########################################################
        if 'cut the wire' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak('shutting down your computer')
            os.system('shutdown -s')

        if 'logout' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            os.system('shutdown /s /t, 0')
