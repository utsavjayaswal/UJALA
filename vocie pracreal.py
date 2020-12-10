# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:43:32 2020

@author: utsav
"""
import pyttsx3
import speech_recognition as sr
import practice
import mooddec

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

def whatisinroom():
    op=practice.objdetec()
    objs='there is a'
    for i in op:
        objs+=i+'and'
    speak(objs)     

def howismood():
    moods=mooddec.mooddetect()
    beg='the moods of people here are '
    for i in range(len(moods)):
        beg+='person'+str(i+1)+' is '+moods[i]+' and '
    print(beg)
    speak(beg)        
       

print('start')
speak("you are welcome,how may i help you")
text=get_audio()
command1=['what is in the room','kamre mein kya hai']
command2=['google','man kaisa hai','logon ka mood kaisa hai','main kaisa hai','mod kaisa hai','how is mood','how is mod']
flag=0
for phrase in command1:
    if phrase in text.lower():
        whatisinroom()
        flag=1

for phrase in command2:
    if phrase in text.lower():
        howismood()
        flag=1
        

                  
        
        
        
        


        
        




