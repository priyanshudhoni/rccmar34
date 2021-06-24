import pyttsx3
import datetime
import pyaudio
import speech_recognition as sc
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
jarvis=pyttsx3.init()
voices=jarvis.getProperty('voices')
jarvis.setProperty('voice',voices[1].id)
jarvis.setProperty('rate',150)
def cpu():
    e=str(psutil.cpu_percent())
    perform("The Cpu percentage is"+e)
    d=psutil.sensors_battery
    perform("the battery percentage is")
    perform(battery.percent)
def screenshot():
    p=pyautogui.screenshot()
    p.save("C://Users//HP//Desktop//Arjun//p.png")

def perform(d):
    jarvis.say(d)
    jarvis.runAndWait()
def time():
    time2=datetime.datetime.now().strftime("%H:%M:%S")
    perform("The current time is")
    perform(time2)
def date():
    year1=int(datetime.datetime.now().year)
    month1=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    jarvis.say("The current date is")
    perform(date)
    perform(month1)
    perform(year1)
def joke():
    perform(pyjokes.get_joke())
    
                                     
def greet():
    hour=datetime.datetime.now().hour
    perform("Hello Priyanshu Sir")
    perform("I am your personal assistant Jarvis")
    if(hour>6 and hour<12):
        perform("Good Morning Sir")
    elif(hour>=12 and  hour<18):
        perform("Good Afternoon Sir")
    elif(hour>=18 and hour<24):
        perform("Good Evening Sir")
    else:
        perform("Good Noght Sir")

def command():
    w=sc.Recognizer()
    with sc.Microphone() as rr:
        print("Listening..............")
        w.pause_threshold=1
        q=w.listen(rr)
    try:
        e=w.recognize_google(q)
        print("The order to be executed is.....")
        print(e)
    except Exception as r:
        print(r)
        perform("Sorry please say it again")
    return e
def sendmail(receiver,data):
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.login("priyanshurcciit@gmail.com","CSE2019/101")
    s.sendmail("priyanshusinghrcciit",receiver,data)
    s.close()

    
               
    
    
    

                
def jarvis_on_act():
    while(True):
        perform("Mention your wish")
        r=command().lower()
        if "time" in r:
            time()
        elif "date" in r:
            date()
        elif "stop" in r:
            break
        elif "wikipedia" in r:
            r=r.replace("wikipedia","")
            ok=wikipedia.summary(r,sentences=2)
            perform(ok)
        elif "send mail" in r:
            try:
               print("Pease say the content")
               perform("Please say the content")
               
               d=command().lower()
               sendmail("abhikchanda12@gmail.com",d)
               perform("Task done mail is sent")
            except Exception as l:
                print(l)
            
        elif "search" in r:
             perform("What to search?")
             path="C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
             f=command().lower()
             wb.get(path).open_new_tab(f+".com")
             
        elif "logout" in r:
            os.system("shutdown -1")
        elif "restart" in r:
            os.system("shutdown /r /t 1")
        elif "shutdown" in r:
            os.system("shutdown /s /t 1")
        elif "play songs" in r:
            path="C://Users//HP//Desktop//Songs"
            songs=os.listdir(path)
            os.startfile(os.path.join(path,songs[0]))
        elif "remember that" in r:
            perform("What should I remember?")
            data=command()
            perform("You told me to remember that"+data)
            remember=open("priyanshujarvis.txt","w")
            remember.write(data)
            remember.close()
        elif "do you remember anything" in r:
            rem=open("priyanshujarvis.txt","r")
            perform("You told me to remember that"+rem.read())
            rem.close()
                          
        elif "screenshot" in r:
            screenshot()
            perform("Screenshot taken")
        elif "cpu" in r:
            cpu()
        elif "jokes" in r:
            joke()
            
            

        
        
        

greet()
time()
date()
jarvis_on_act()

        
        
    
    
