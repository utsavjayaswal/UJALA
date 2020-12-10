# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:13:13 2020

@author: utsav
"""


import time
from plyer import notification
import pyttsx3
import datetime
import speech_recognition as sr
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate' ,150)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=5)
        print('time over')
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            
    return said

events=[]
times=[]
speak('what event you want to add sir listening')
tempeve=get_audio()
events.append(tempeve)
speak('at what time you want to add it sir say in hour and am pm format')
temptime=get_audio()
a,b=temptime.split()
times.append(a)

print(type(times[0]))
hr,mint=a.split(':')
print(events)
print(times)




#hr=int(input('hour'))
#mint=int(input('mint'))
#ampm=str(input('a.m. or p.m.'))

if(b=='p.m.' or b=='pm'):
    (hr)=int(hr)+12
print(hr)
print(mint)
print(datetime.datetime.now().hour) 
print(datetime.datetime.now().minute)
print(times.index(str(hr)+':'+str(mint)))   
while True:
    if(hr==datetime.datetime.now().hour and mint==datetime.datetime.now().minute):
        text=events[times.index(str(hr)+':'+str(mint))]
        print(text)
        speak(text)
        break
print('exited')



    
    
    
