import datetime
from playsound import playsound
import pygame
alarmHr=int(input("Enter the hour:"))
alarmMin=int(input("Enter the minute:"))
pygame.mixer.init()
alarmPM=input(' AM/PM: ')
if alarmPM=='PM' or alarmPM=='pm':
    alarmHr+=12
while True:
    if alarmHr==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
       # print("playing....")#
       playsound(r"C:\Users\rithi\OneDrive\Desktop\Projects\AlarmClock\01 - Namo Namo - SenSongsMp3.Co.mp3")
       break
        
