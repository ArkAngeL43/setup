import os 
import sys
import requests
from requests_html import *
import json 
import python_weather
import time 
import calendar 
import dill
from os import system, name
from time import sleep
from requests_html import HTMLSession 
import colorama
from colorama import Fore
from sys import platform
from gtts import gTTS
from gtts import gTTS
import asyncio
import requests 
from requests import *

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
   
   
def screen_clear():
   if name == 'nt':
      _ = system('cls')

def CS(X):  
   time.sleep(X)
   os.system("clear")

os.system(' sudo apt-get update ')

time.sleep(0.1)
os.system(' clear ')
os.system(' mpg123 hru.mp3 ')
os.system(' clear ')
GB = str(input(" ==>> "))

if 'bad' in GB:
         time.sleep(0.1)
         os.system(' clear ')
         os.system(' mpg123 oh.mp3 ')
         os.system(' clear ')
         print(Fore.BLUE+"|////////////////////////|")
         time.sleep(0.1)
         print(Fore.BLUE+"|1: lofi live radio      |")
         time.sleep(0.1)
         print(Fore.BLUE+"|2: gamer live radio     |")
         time.sleep(0.1)
         print(Fore.BLUE+"|3: ncs top 50           |")
         time.sleep(0.1)
         print(Fore.BLUE+"|4: spotify              |")
         time.sleep(0.1)
         print(Fore.BLUE+"|5: study radio live     |")
         time.sleep(0.1)
         print(Fore.BLUE+"|6: ambitent music       |")
         time.sleep(0.1)
         print(Fore.BLUE+"|////////////////////////|") 


if 'good' in GB:
          time.sleep(0.1)
          os.system(' mpg123 great.mp3 ')
          os.system(' clear ')
          print(Fore.BLUE+"|////////////////////////|")
          time.sleep(0.1)
          print(Fore.BLUE+"|1: lofi live radio      |")
          time.sleep(0.1)
          print(Fore.BLUE+"|2: gamer live radio     |")
          time.sleep(0.1)
          print(Fore.BLUE+"|3: ncs top 50 live      |")
          time.sleep(0.1)
          print(Fore.BLUE+"|4: spotify              |")
          time.sleep(0.1)
          print(Fore.BLUE+"|5: study radio live     |")
          time.sleep(0.1)
          print(Fore.BLUE+"|6: ambitent music       |")
          time.sleep(0.1)
          print(Fore.BLUE+"|////////////////////////|")          
good = str(input(" song ==> "))

if '6' in good:
       time.sleep(0.1)
       os.system(' mpg123 heard.mp3 ')
       os.system(' clear ')
       os.system(' open https://www.youtube.com/watch?v=qt_urUz42vI ')

if '5' in good: 
       time.sleep(0.1)
       os.system(' mpg123 heard.mp3 ')
       os.system(' clear ')
       os.system(' open https://www.youtube.com/watch?v=auhMEZD3F1E ')

if '4' in good:
       time.sleep(0.1)
       os.system(' mpg123 heard.mp3 ')
       os.system(' clear ')
       os.system(' open https://open.spotify.com/ ')

if '3' in good:
       time.sleep(0.1)
       os.system(' mpg123 heard.mp3 ')
       os.system(' clear ')
       os.system(' open https://www.youtube.com/watch?v=feaL7YKwsyo ')

if '1' in good:
       time.sleep(0.1)
       os.system(' mpg123 heard.mp3 ')
       os.system(' clear ')
       os.system(' open https://www.youtube.com/watch?v=1SorANsO9wE ')

if '2' in good:
       time.sleep(0.1)
       os.system(' mpg123 heard.mp3 ')
       os.system(' clear ')
       os.system(' open https://www.youtube.com/watch?v=6H8f1fa_bJQ ')

os.system(' mpg123 scrape.mp3')
os.system(' clear ')
yes = str(input(" Y/N "))

if 'y' in yes:
       os.system(' mpg123 scraping.mp3 ')
       os.system(' python3 scrape.py ')


if 'n' in yes:
       os.system(' clear ')
       os.system(' mpg123 ok.mp3')
       os.system(' clear ') 

elif 'Y' in yes:
         time.sleep(0.1)
         os.system(' mpg123 scraping.mp3 ')
         os.system(' python3 scrape.py ')

elif 'N' in yes:
         time.sleep(0.1)
         os.system(' mpg123 ok.mp3 ')
         os.system(' clear ')      

os.system(' mpg123 weather.mp3 ')
print(" ########################################### ")
X = str(input(" Y/N ==>> "))

if 'n' in X:
        time.sleep(0.1)
        os.system(' clear ') 
        os.system(' mpg123 ok.mp3 ')

if 'Y' in X:
       time.sleep(0.1)
       os.system(' clear ')
       os.system(' mpg123 weather2.mp3 ')
       os.system(' clear ')
       os.system(' weather Port Saint Lucie Floirda ')

elif 'Yes' in X:
           time.sleep(0.1)
           os.system(' mpg123 weather2.mp3 ')
           os.system(' clear ')
           os.system(' weather Port Saint Lucie Floirda ')

elif 'yes' in X:
           time.sleep(0.1)
           os.system(' mpg123 weather2.mp3 ')
           os.system(' clear ')
           os.system(' weather Port Saint Lucie Floirda ')

elif 'no' in X:
         time.sleep(0.1)
         os.system(' mpg123 ok.mp3 ')
         os.system(' clear ')

elif 'No' in X:
          time.sleep(0.1)
          os.system(' mpg123 ok.mp3 ')
          os.system(' clear ')

elif 'y' in X:
         time.sleep(0.1)
         os.system(' clear ')
         os.system(' mpg123 weather2.mp3 ')
         os.system(' clear ')
         os.system(' weather Port Saint Lucie Floirda ')

os.system(' mpg123 cal.mp3 ')
cal = str(input(" Y/n ==>> "))

if 'N' in cal:
        time.sleep(0.1)
        os.system(' mpg123 ok.mp3 ')
        os.system(' clear ')       

if 'Y' in cal:
       time.sleep(0.1)
       os.system(' mpg123 heard2.mp3 ')
       os.system(' clear ')
       time.sleep(0.1)
       os.system(' clear ')
       import calendar 
       print(Fore.BLUE+"??????????????????????????????????????")
       the_year = int(input(' Enter The Year ==> '))
       the_month = int(input(' Enter The Month ==> '))
       print(Fore.BLUE+"??????????????????????????????????????")
       print()
       print(calendar.month(the_year, the_month))

elif 'y' in cal:
         time.sleep(0.1)
         os.system(' mpg123 heard2.mp3 ')
         time.sleep(0.1)
         os.system(' clear ')
         import calendar 
         print(Fore.BLUE+"??????????????????????????????????????")
         the_year = int(input(' Enter The Year ==> '))
         the_month = int(input(' Enter The Month ==> '))
         print(Fore.BLUE+"??????????????????????????????????????")
         print()
         print(calendar.month(the_year, the_month))       

elif 'n' in cal:
         time.sleep(0.1)
         os.system(' mpg123 ok.mp3 ')
         os.system(' clear ')

os.system(' clear ')
os.system(' mpg123 sat.mp3 ') 
os.system(' clear ')

P = str(input(" Y/N ==>> "))

if 'Y' in P:
       time.sleep(0.1)
       os.system(' clear ')
       os.system(' mpg123 nice.mp3 ')
       os.system(' exit && cd .. && cd .. && exit ')

if 'no' in P:
        time.sleep(0.1)
        os.system(' clear ')
        os.system(' mpg123 damn.mp3 ')
        os.system(' clear ')
        os.system(' exit && cd.. && cd.. && exit ') 

elif 'No' in P:
          time.sleep(0.1)
          os.system(' clear ')
          os.system(' mpg123 damn.mp3 ')
          os.system(' clear ')
          os.system(' exit && cd.. && cd.. && exit ') 

elif 'N' in P:
         time.sleep(0.1)
         os.system(' clear ')
         os.system(' mpg123 damn.mp3 ')
         os.system(' clear ')
         os.system(' exit && cd.. && cd.. && exit ') 

elif 'n' in P:
         time.sleep(0.1)
         os.system(' clear ')
         os.system(' mpg123 damn.mp3 ')
         os.system(' clear ')
         os.system(' exit && cd.. && cd.. && exit ') 

elif 'yee' in P:
           time.sleep(0.1)
           os.system(' clear ')
           os.system(' mpg123 nice.mp3 ')
           os.system(' exit && cd .. && cd .. && exit ')

elif 'Yes' in P:
           time.sleep(0.1)
           os.system(' clear ')
           os.system(' mpg123 nice.mp3 ')
           os.system(' exit && cd .. && cd .. && exit ')

elif 'yes' in P: 
         time.sleep(0.1)
         os.system(' clear ')
         os.system(' mpg123 nice.mp3 ')
         os.system(' exit && cd .. && cd .. && exit ')