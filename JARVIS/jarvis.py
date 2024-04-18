import pyttsx3
import time
import datetime
import speech_recognition as sr
import sys
import smtplib
import wikipedia
import webbrowser as wb
import os
import psutil
import pyautogui
import pyjokes
import speedtest_cli
import requests
import subprocess
from plyer import notification
from pygame import mixer 

from bs4 import BeautifulSoup

for i in range(3):
    a = input("Enter Password to use jarvis: ")
    pw_file = open("Password.txt")
    pw = pw_file.read()
    pw_file.close()
    if(a==pw):
        print("WELCOME SIR! Tell me how can i help you")
        break
    elif(i == 2 and a!=pw):
        exit()
    elif(a!= pw):
        print("Try Again")
                            
from tkinter import Tk
from Intro import GIFViewerApp

root = Tk()
app = GIFViewerApp(root)
root.mainloop()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ai_safety_warning():
    """
    Function to display a warning message about potential dangers of AI.
    """
    speak("WARNING: AI systems can pose potential dangers if not used responsibly.")
    speak("Please ensure that you use AI technologies safely and ethically.")
    speak("Always consider the potential risks and consequences of AI applications.")

# Call the function to display the warning message


def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is " + current_time)

def get_date():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().strftime("%B")
    current_day = datetime.datetime.now().day
    speak("Today's date is " + str(current_day) + " " + current_month + " " + str(current_year))

def wish_me():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    elif 18 <= hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Sir! This is late night. Prioritize rest and breaks while working late to maintain productivity and well-being. Establish boundaries and practice self-care to mitigate the negative impacts of late-night work.")
    speak("JARVIS at your service. Please tell me SIR how can I help you?")

def stop():
    speak("Stopping code execution...")
    sys.exit()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()  # Convert to lowercase to make command recognition case-insensitive
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't reach the Google Speech Recognition service.")
        return ""

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshhers@gmail.com', '123')
    server.sendmail('harshhers@gmail.com', to, content)
    server.close()

def get_cpu_report():
    CPU = str(psutil.cpu_percent())
    speak("CPU is at " + CPU + " " ) 
    battery = psutil.sensors_battery()
    speak("Battery is at " + str(battery.percent) + " percent")


def joke():
    speak(pyjokes.get_joke())
 
if __name__ == "__main__":
    # ai_safety_warning()
    # wish_me()
    while True:
        query = take_command()

        if 'wish me' in query:
            wish_me()
        elif 'change password' in query:
            speak("What's the new password")
            new_pw = input("Enter the new password :- ")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done Sir")
            speak(f"Your new password is {new_pw}")
            
        elif'open' in query:
            from dict import opeappweb
            opeappweb(query)
        elif'close' in query:
            from dict import closeapp
            closeapp(query)
            
        elif 'time' in query:
            get_time()
            
        elif 'date' in query:
            get_date()
            
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple matches. Can you please specify?")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any information on that topic.")
                
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "abc@gmail.com"
                send_email(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Unable to send email.")
                
        elif "open chrome" in query:
            speak("What should I search?")
            search_query = take_command()
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab('https://www.google.com/search?q=' + search_query)
            
        elif 'logout' in query:
            os.system("shutdown -1")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif 'start songs' in query:
            song_dir = 'C:\\MinGW\\C by college\\ProjectWAD\\songs\\Arijit Singh'
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0]))
            
        elif 'remember that' in query:
            speak("What Should I remember?")
            data = take_command()
            speak("You said me to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said to me remember that " + remember.read())
            
        elif 'cpu report' in query:
            get_cpu_report()
            
        elif'screen shot' in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            speak("Done! Screen Short")
            
        elif'take my photo' in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("Enter")
            pyautogui.sleep(3)
            speak("Smile")
            pyautogui.press("enter")
            
        elif 'say me a joke' in query:
            joke()
            
        elif 'news' in query:
            from News import letestnews
            letestnews()
            
        elif 'calculate' in query:
            from calculator import wolframAlpha
            from calculator import calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            calc(query)
            
        elif 'schedule my day' in query:
            task = [] #Empty List
            speak("Do you want to clear all schedule (Please Write [Y] or [N])")
            response = input("Do you want to clear all schedule (Please Write Yes or No): ")

            if "Y" in response:
                file = open("task.txt","w")
                file.write("")
                file.close()
                no_tasks = int(input("Enter the number of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    task.append(input("Enter the tasks :- "))
                    file = open("task.txt","a")
                    file.write(f"{i}.{task[i]}\n")
                    file.close()
            elif "N" in response:
                no_tasks = int(input("Enter the number of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    task.append(input("Enter the tasks :- "))
                    file = open("task.txt","a")
                    file.write(f"{i}.{task[i]}\n")
                    file.close()
                        
       
        elif 'show my schedule' in query:
            try:
                from pygame import mixer
                from plyer import notification

                file = open("task.txt", "r")  
                content = file.read()  
                file.close()  

                mixer.init()
                mixer.music.load("notification.mp3")
                mixer.music.play()

                notification.notify(
                    title="My Schedule :- ",
                    message=content,
                    timeout=15
                )
            except Exception as e:
                print("An error occurred while showing the schedule:", e)
                
        elif 'internet speed' in query:
            wifi = speedtest_cli.Speedtest()
            upload_net = wifi.upload()/1048576 # 1 megabyte = 1024*1024 bytes
            download_net = wifi.download()/1048576
            print("Wifi upload speed is ",upload_net)
            print("Wifi download speed is ",download_net)
            speak("Wifi upload speed is " + str(upload_net))
            speak("Wifi download speed is " + str(download_net))
        
        # elif 'ipl score' in query:
            
        #     url = "https://www.cricbuzz.com/"
        #     page = requests.get(url)
        #     soup = BeautifulSoup(page.text,"html.parser")
           
            
        #     team_elements = soup.find_all(class_="cb-over-flo cb hmscg-tm-nm")
        #     team1 = team_elements[0].get_text() if team_elements else "Team 1"
        #     team2 = team_elements[1].get_text() if len(team_elements) > 1 else "Team 2"
        #     score_elements = soup.find_all(class_="cb-over-flo")
        #     team1_score = score_elements[8].get_text() if len(score_elements) > 8 else "N/A"
        #     team2_score = score_elements[10].get_text() if len(score_elements) > 10 else "N/A"
            
            
        #     a = print(f"{team1} : {team1_score}")   
        #     b = print(f"{team2} : {team2_score}")
        
        #     notification.notify(
        #         title = "IPL Score:- ",
        #         message = f"{team1} : {team1_score}\n{team2} : {team2_score}",
        #         timeout = 10
        #     )
        elif 'ipl score' in query:
            import requests
            from bs4 import BeautifulSoup
            from plyer import notification
        
            url = "https://www.iplt20.com/match/2024/1415"
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
        
            match_cards = soup.find_all("div", class_="scoreCollection__content cricket")
        
            if match_cards:
                live_scores = []
                for card in match_cards:
                    team1 = card.find("div", class_="cscore_team icon-font-before").text.strip()
                    team2 = card.find("div", class_="cscore_team icon-font-after").text.strip()
                    score = card.find("div", class_="cscore_score").text.strip()
                    live_scores.append((team1, team2, score))
        
                team1, team2, team1_score, team2_score = "Team 1", "Team 2", "N/A", "N/A"
                if live_scores:
                    team1, team2, score = live_scores[0]
                    team1_score, team2_score = score.split("v")
        
                print(f"{team1} : {team1_score.strip()}")
                print(f"{team2} : {team2_score.strip()}")
        
                notification.notify(
                    title="IPL Score:- ",
                    message=f"{team1} : {team1_score.strip()}\n{team2} : {team2_score.strip()}",
                    timeout=10
                )
            else:
                print("No live matches currently")
                notification.notify(
                    title="IPL Score:- ",
                    message="No live matches currently",
                    timeout=10
                )
        
        
        elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        subprocess.Popen(["python","C:\\MinGW\\JARVIS\\FocusMode.py"])
                        exit()
                    else:
                        pass
        elif"my focus" in query:
            from FocusGraph import  focus_graph
            focus_graph()
        
        
        elif 'stop' in query:
            stop()
        