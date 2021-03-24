# Author: Deendayal Kumawat
"""
Date: 05/02/21
Descriptions: AI Assistance(Jarvis)
"""

# Email
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from geopy.geocoders import Nominatim  # For Zip Code
import speedtest  # For internet Speed
import urllib.request
import ctypes
import subprocess
import platform
import whois
import PyPDF2
import pyttsx3
import requests
import speech_recognition as speech
import datetime
import os
import cv2
import random
import pathlib
import winshell as winshell
from requests import get
import wikipedia
import webbrowser
import calendar
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import shutil
import time
from time import sleep
import json
import pyautogui
import psutil
import instaloader
import wolframalpha
import re
from urllib.request import urlopen
from playsound import playsound
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as BS  # For covid 19
from bs4 import BeautifulSoup  # For Weather Forecast
from pywikihow import search_wikihow  # Anything search from how
from PyDictionary import PyDictionary as Diction  # PyDictionary
import keyboard
import config  # My Password file
# Qt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie  # For gif to run
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from assistance_gui import Ui_assistance_gui  # Ui_jarvisGUI is class name and jarvis_GUI file name

# My Created Module
import MyAlarm  # My Created Module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
print(voices[2].id)
print(voices[3].id)
print(voices[4].id)
print(voices[5].id)
print(voices[6].id)
engine.setProperty('voice', voices[0].id)


# engine.setProperty('voice',voices[len(voices) -5].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Checking Internet
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

# System initialize
def checking_system():
    # speak(" System initialize")
    #
    # speak("All System are working....")
    playsound('H:\\Pycharm Code\\assistance\\audio\\jarvis_introdation.wav')
    time.sleep(2)


# to Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir.......')
        tellTime()
        tellDay()
        checking_weather()
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir.......')
        tellTime()
        tellDay()
        checking_weather()
    else:
        speak('Good Evening.......')
        tellTime()
        tellDay()
        checking_weather()
    speak('I am Jarvis Sir, Please tell me, how may i help you...')


# Day
def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        # print(day_of_the_week)
        speak("The day is " + day_of_the_week)


# Time
def tellTime():
    tim = time.strftime('%I:%M %p')
    speak(f"it's {tim}")


# Weather
def checking_weather():
    try:
        check_ip = get('https://api.ipify.org').text
        # print(check_ip)
        url = 'https://get.geojs.io/v1/ip/geo/' + check_ip + '.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        search = f"temepature in {city}"
        # print(search)
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"{search} is {temp}")
    except Exception as e:
        print(e)


# Checking Weather using command
def weather(self):
    try:
        api_key = "xxxxxx-xxxxxxxxxx"  # generate your own api key from open weather
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        speak("tell me which city")
        city_name = self.takeCommand().lower()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            r = ("in " + city_name + " Temperature is " +
                 str(int(current_temperature - 273.15)) + " degree celsius " +
                 ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                 ", humidity is " + str(current_humidiy) + " percent"
                                                           " and " + str(weather_description))
            print(r)
            speak(r)
        else:
            speak(" City Not Found ")
    except Exception as exc:
        print(exc)


# Checking Battery Power
def battery_power():
    try:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f'Sir our system have {percentage} percentage battery power')

        if percentage >= 75:
            speak("we have enough power to contiune our work")
        elif percentage >= 40 or percentage <= 75:
            speak("we should connect our system to charging point to charge our battery")
        elif percentage <= 15 or percentage <= 30:
            speak("we don't have enough power to contiune work, please connect charging")
        elif percentage <= 15:
            speak("we have very low power, Please connect to charging, the system will be shutdown very soon")
    except Exception as e:
        print(e)


# Checking battery and cpu usage
def cpu():
    # usage = str(psutil.cpu_percent())
    # speak('CPU usage is at ' + usage)
    # print('CPU usage is at ' + usage)

    print('                                                                   ')
    print('----------------------CPU Information summary----------------------')
    print('                                                                   ')

    # gives a single float value
    vcc = psutil.cpu_count()
    print('Total number of CPUs :', vcc)

    usage = str(psutil.cpu_percent())
    vcpu = psutil.cpu_percent()
    print('Total CPUs utilized percentage :', vcpu, '%')
    print('CPU usage is at ' + usage)

    print('                                                                   ')
    print('----------------------RAM Information summary----------------------')
    print('                                                                   ')
    # you can convert that object to a dictionary
    # print(dict(psutil.virtual_memory()._asdict()))
    # gives an object with many fields
    vvm = psutil.virtual_memory()

    x = dict(psutil.virtual_memory()._asdict())

    def forloop():
        for i in x:
            print(i, "--", x[i] / 1024 / 1024 / 1024)  # Output will be printed in GBs

    forloop()
    print('                                                                   ')
    print('----------------------RAM Utilization summary----------------------')
    print('                                                                   ')
    # you can have the percentage of used RAM
    print('Percentage of used RAM :', psutil.virtual_memory().percent, '%')
    # 79.2
    # you can calculate percentage of available memory
    print('Percentage of available RAM :', psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, '%')

    print('                                                                   ')
    print('----------------------Battery summary----------------------')
    print('                                                                   ')
    battery = psutil.sensors_battery()
    print("battery is at:" + str(battery.percent))


# News
def news():
    try:  # 
        jsonObj = urlopen(
            'https://newsapi.org/v2/top-headlines?country=in&apiKey=xxxxxxxxxxxxxxxxx')
        data = json.load(jsonObj)
        i = 1

        speak('here are some top news from the times of india')
        print('''=============== TIMES OF INDIA ============''' + '\n')

        for item in data['articles']:
            print(str(i) + '. ' + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1
    except Exception as e:

        print(str(e))


# Send Email
def sendEmail(self):
    try:
        speak('Sir what should i say?....')
        query = self.takeCommand().lower()
        if 'send a file' in query:
            email = config.userEmail  # Your Email Id
            password = config.passwordEmail  # Password of email id
            send_to_email = config.send_to_mail  # Whom you are send the email # For multiple use decorator
            speak('Ok Sir, What is the subject for this email...')
            query = self.takeCommand().lower()
            subject = query  # the subject into email
            speak('and sir, What is the message for this email')
            query2 = self.takeCommand().lower()
            message = query2  # the message for the email
            speak('Sir Please enter the correct path of the file into the shell')
            file_location = input('Please enter file path here ...')  # the file attachment in the email
            speak('Please Wait, I am sending email now...')

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            # setup the attachment
            file_name = os.path.basename(file_location)
            attachment = open(file_location, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders = encode_base64(part)
            part.add_header('Content-Disposition', 'attachment,file_name =  %s' % file_name)
            # Attach the attachment to the MIMEMultipart object
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.ehlo()
            server.starttls()
            server.login(email,
                         password)  # eneter your email and password but you have to enable <less secure app> in your email privacy setting
            text = msg.as_string()
            server.sendmail(email, send_to_email, message)  # enter your email, reciver email, content to send
            server.quit()
            speak('Email has been sent to Deendayal')

    except Exception as ex:
        print(ex)
        print('Sorry Sir, I am not able to send this email ')

    else:
        try:
            email = config.userEmail  # Your Email Id
            password = config.passwordEmail  # Password of email id
            send_to_email = config.send_to_mail  # Whom you are send the email # For multiple use decorator
            message = self.query  # the message in the emaol

            server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.ehlo()
            server.starttls()
            server.login(email,
                         password)  # eneter your email and password but you have to enable <less secure app> in your email privacy setting
            text = msg.as_string()
            server.sendmail(email, send_to_email, message)  # enter your email, reciver email, content to send
            server.quit()
            speak('Email has been sent to Deendayal')

        except Exception as ex:
            print(ex)
            print('Sorry Sir, I am not able to send this email ')


# pdf reader
def pdf_reader():
    count = 0

    path_file = "H:\\Pycharm Code\\assistance\\pdf\\"
    dir_path_os = os.path.dirname(os.path.realpath(path_file))
    dir_path = pathlib.Path(path_file).iterdir()
    # Count
    for path in dir_path:
        if path.is_file():
            count += 1

    speak(f'Sir, {count} pdf files are there in directory, Which file i have to read enter the file name...')
    file_pdf_user = str(input('enter file name correctly...\n'))
    print(file_pdf_user)
    # select_pdf_file = easygui.fileopenbox()

    for root, dirs, files in os.walk(dir_path_os):
        for file in files:

            # change the extension from '.pdf' to
            # the one of your choice.

            try:
                if file.endswith('.pdf'):
                    # file = root+'/'+str(file)
                    file = str(file)
                    # print(file)
                    # print(f"H:\\Pycharm Code\\jarvis\\pdf\\{file_pdf_user}''''''''''''''''''''''''''''''''''''")
                    select_pdf_file = f"H:\\Pycharm Code\\assistance\\pdf\\{file_pdf_user}"

                    with open(select_pdf_file, "rb") as pdf_file_reading:
                        pdfReader = PyPDF2.PdfFileReader(pdf_file_reading)
                        pages = pdfReader.numPages
                        speak(
                            f'Sir, This pdf have total {pages} pages and Author is {pdfReader.documentInfo["/Author"]} and Created by {pdfReader.documentInfo["/Creator"]}')
                        speak('Sir, enter the page number which i have to read')
                        page_read = int(input('Enter the page number'))
                        page = pdfReader.getPage(page_read)
                        text = page.extractText()
                        speak(text)
                break
            except Exception as ex:
                speak('Sir, file not found')
                break


# Hide Folder and Files
def hide_files_folders(self):
    try:
        speak('Sir tell me you want to hide this folder or make it visible for everyone')
        hide_file_dir = self.takeCommand().lower()
        if 'hide' in hide_file_dir or 'hidden' in hide_file_dir:
            os.system('attrib +h /s /d')
            speak('Sir all the files in this folder are now hidden ')
        elif 'visible' in hide_file_dir or 'unhide' in hide_file_dir:
            os.system('attrib -h /s /d')
            speak(
                'Sir all the files in this folder are now visiable to everyone. i wish you are taking own decision.. ')
        elif 'leave it' in hide_file_dir or 'leave it now' in hide_file_dir:
            speak('ok sir')

    except Exception as exc:
        print(exc)


# Showing Disk Usage
def total_disk_usage():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))


# Opening Application
def open_application(query):
    try:
        # __________________________________ Open Chorme ___________________________________
        if "chrome" in query:
            speak("opening Google Chrome")
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            return

        # __________________________________ Open android Studio ___________________________________
        elif 'android studio' in query:
            speak('opening android studio')
            spath = 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe'
            os.startfile(spath)
            return
        # __________________________________ Open Firfox ___________________________________
        elif "firefox" in query or "mozilla" in query:
            speak("Opening Mozilla Firefox")
            os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            return

        # __________________________________ Open Word ___________________________________
        elif "microsoft browser" in query:
            speak("Opening Microsoft browser")
            os.startfile('C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe')
            return

        # __________________________________ Open downloads ___________________________________
        elif "downloads" in query:
            # get username of pc
            username = os.getlogin()
            speak("Opening downloads")
            os.startfile(f'C:\\Users\\{username}\\Downloads')
            return
        # __________________________________ Open Notepad ___________________________________
        elif 'notepad' in query:
            speak('opening notepad')
            npath = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(npath)
            return

        # __________________________________ Open Pycharm ___________________________________
        elif 'pycharm' in query:
            speak('opening pycharm')
            charmpath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
            os.startfile(charmpath)
            return

        # __________________________________ Open Visual Stdio Code ___________________________________
        elif 'media player' in query:
            speak('opening window media player')
            mediapath = 'C:\\Program Files\\Windows Media Player\\wmplayer.exe'
            os.startfile(mediapath)
            return

        # __________________________________ Open vlc Player ___________________________________
        elif 'vlc player' in query:
            speak('opening vlc player')
            vlcpath = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
            os.startfile(vlcpath)
            return
        # __________________________________ Open Color Management ___________________________________
        elif 'color management' in query:
            os.system('colorcpl')

        # __________________________________ Window Backup  ___________________________________
        elif 'window backup' in query:
            os.system('sdclt')

        # __________________________________ Credentials Backup and Restore ___________________________________
        elif 'backup and restore' in query:
            os.system('credwiz')

        # __________________________________ Check Color Calibration  ___________________________________
        elif 'check color calibration' in query:
            os.system('dccw')

        # __________________________________ Check Problem Steps Recorder  ___________________________________
        elif 'psr recorder' in query:
            os.system('psr')

        # __________________________________ Check Performance Monitor  ___________________________________
        elif 'check performance monitor' in query:
            os.system('perfmon.msc')

        # __________________________________ Check Window Version  ___________________________________
        elif 'check window version' in query:
            os.system('winver')

        # __________________________________ Check System Info  ___________________________________
        elif 'check system information' in query:
            os.system('msinfo32')

        # __________________________________ Windows Memory Diagnostic  ___________________________________
        elif 'windows memory diagnostic' in query:
            os.system('mdsched')

        # __________________________________ Check Task List  ___________________________________
        elif 'check task list' in query:
            os.system('tasklist')

        # __________________________________ Windows Mobility Centre  ___________________________________
        elif 'windows mobility centre' in query:
            os.system('mblctr')

        # __________________________________ Get Mac Address  ___________________________________
        elif 'get mac address' in query:
            os.system('getmac')

        # __________________________________ Microsoft Troubleshooting  ___________________________________
        elif 'Microsoft Troubleshooting' in query:
            os.system('control.exe/name Microsoft.Troubleshooting')

        # __________________________________ Check Resource Monitor  ___________________________________
        elif 'check resource monitor' in query:
            os.system('resmon')

        # __________________________________ Check Installed Programme List  ___________________________________
        elif 'check installed programme list' in query:
            os.system('wmic product get name')

        # __________________________________ Driver List  ___________________________________
        elif 'check driver list' in query:
            os.system('driverquery')

        # __________________________________ DirectX Diagnostic Tool  ___________________________________
        elif 'directX diagnostic tool' in query:
            os.system('DxDiag')

        # __________________________________ Disk Defragment  ___________________________________
        elif 'disk defragment' in query:
            os.system('dfrgui')

        # __________________________________ Registry Editor  ___________________________________
        elif 'registry editor' in query:
            os.system('regedit')
            return

        # __________________________________ Control Panel  ___________________________________
        elif 'control panel' in query:
            os.system('control')

        # __________________________________ Windows Services  ___________________________________
        elif 'window services' in query:
            os.system('services.msc')

        # __________________________________ Checking Window Update  ___________________________________
        elif 'window update' in query:
            os.system('explorer ms-settings:windowsupdate ')

        # __________________________________ Task Manager  ___________________________________
        elif 'window task Manager' in query:
            os.system('taskmgr')

        # __________________________________ Mouse Setting  ___________________________________
        elif 'window mouse setting' in query:
            os.system('main.cpl')

        # __________________________________ Add Or Remove  ___________________________________
        elif 'window add or remove' in query:
            os.system('appwiz.cpl')

        # __________________________________ Network Setup  ___________________________________
        elif 'window network setup' in query:
            os.system('ncpa.cpl')

        # __________________________________ System Properties  ___________________________________
        elif 'window system properties' in query:
            os.system('sysdm.cpl')

        # __________________________________ Device Manager  ___________________________________
        elif 'window device manager' in query:
            os.system('devmgmt.msc')

        # __________________________________ On Screen Keyboard  ___________________________________
        elif 'window Keyboard' in query:
            os.system('osk')

        # __________________________________ open Terminal  ___________________________________
        elif "window terminal" in query:
            os.startfile(cmd)


        else:

            speak("Application not available")
            return
    except Exception as exc:
        print(exc)


# Automation Opening Web
def opening_web(self, webquery):
    try:
        # __________________________________ Open LinkedIn __________________________________________
        if 'linkedin' in webquery:
            speak('Sure Sir, Opening Linkedin')
            import LinkedinBot
            LinkedinBot.linkedlinBot()
            return


        # __________________________________ Open Facebook __________________________________________
        elif 'facebook' in webquery:
            speak('Sir What should i post on Your Facebook Account')
            fbPost = self.takeCommand().lower()
            myFbPost = fbPost
            import FacebookBot

            FacebookBot.fbAutoBot(myFbPost)
            # webbrowser.open('https://www.facebook.com')
            return
        # __________________________________ Open Instagram _________________________________________
        elif "instagram" in webquery:
            speak('Sir What should i post on Your Instagram Account')
            instaPost = self.takeCommand().lower()
            myInstaPost = instaPost
            import InstagramBot

            InstagramBot.instaGramBot(myInstaPost)
            return

        # __________________________________ Open Stackoverflow _____________________________________
        elif 'stackoverflow' in webquery:
            speak('Opening Stackoverflow')
            speak('Sir, What should i search on stackoverflow')
            stackflow = self.takeCommand().lower()
            webbrowser.open(f'http://www.stackoverflow.com/{stackflow}')
            return
        # __________________________________ Open Github ____________________________________________
        elif 'github' in webquery:
            speak('Opening github')
            webbrowser.open('https://www.github.com')
            return
        else:

            speak("Not available")
            return
    except Exception as exc:
        print(exc)


# Youtube Automation
def youtubeAuto(self):
    speak("Whats Your Command ?")
    comm = self.takeCommand().lower()

    if 'pause' in comm:
        keyboard.press('space bar')

    elif 'restart' in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'film mode' in comm:
        keyboard.press('t')

    Speak("Done Sir")


# Chorme Automation
def chromeAuto(self):
    speak("Chrome Automation started!")

    command = self.takeCommand().lower()

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'history' in command:
        keyboard.press_and_release('ctrl +h')


# Open Any Website
def any_website_opener(website_name):
    extension = re.search(r"[.]", website_name)
    if not extension:
        if not website_name.endswith(".com"):
            website_name = website_name + ".com"
    try:
        url = 'https://www.' + website_name
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False


# Search anything on wikipedia
def searching_wiki(query):
    speak('Searching on wikipedia.....')
    try:
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
        elif 'search' in query:
            query = query.replace("search", "")
        elif 'what' in query:
            query = query.replace("what", "")
        elif 'when' in query:
            query = query.replace("when", "")
        elif 'where' in query:
            query = query.replace("where", "")
        elif 'who' in query:
            query = query.replace("who", "")
        elif 'is' in query:
            query = query.replace("is", "")

        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(result)
        print(result)
    except Exception as ex:
        print(ex)
        speak("Page not found")


# Checking world Covid 19 data
def checking_Worldometer():
    try:
        my_data = requests.get("https://api.covid19api.com/summary")

    except:
        print("Please connect to Internet and try again.")

    else:

        datastr = my_data.text

        data = json.loads(datastr)

        Global = data["Global"]
        Countries = data["Countries"]
        Date = data["Date"]
        date = Date.replace(Date[-1], "")
        date_list = date.split("T")
        data_date = date_list[0]
        data_time = date_list[1]

        s_no = 0
        print("This data is last updated at - " + "\nDate - " + data_date + "\nTime - " + data_time + "\n\n\n")
        print("Total Cases Worldwide -\n" + "New Confirmed - " + str(
            Global['NewConfirmed']) + "\n" + "Confirmed - " + str(
            Global['TotalConfirmed']) + "\n" + "New Recovered - " + str(
            Global['NewRecovered']) + "\n" + "Total Recovered - " + str(
            Global['TotalRecovered']) + "\n" + "New Death - " + str(
            Global['NewDeaths']) + "\n" + " Total Deaths - " + str(
            Global['TotalDeaths']) + "\n\n")
        print("\nThese the cases countrywise - \n\n")
        for c in Countries:
            s_no += 1
            spaces = (len(str(s_no)) * " ") + "  "

            print(str(s_no) + ". Country - " + str(c['Country']) + "\n" + spaces + "New Confirmed - " + str(
                c['NewConfirmed']) + "\n" + spaces + "Confirmed - " + str(
                c['TotalConfirmed']) + "\n" + spaces + "New Recovered - " + str(
                c['NewRecovered']) + "\n" + spaces + "Recovered - " + str(
                c['TotalRecovered']) + "\n" + spaces + "New Deaths - " + str(
                c['NewDeaths']) + "\n" + spaces + "Deaths - " + str(c['TotalDeaths']) + "\n\n")


# Checking India's every State wise Covid 19 data
def calling_every_state_wise(url):
    try:
        # getting the json data by calling api
        data = ((requests.get(url)).json())
        states = []

        # getting states
        for key in data.items():
            states.append(key[0])

        # getting statewise data
        for state in states:
            f = (data[state]['districtData'])
            tc = []
            dis = []
            act, con, dea, rec = 0, 0, 0, 0

            # getting districtwise data
            for key in (data[state]['districtData']).items():
                district = key[0]
                dis.append(district)
                active = data[state]['districtData'][district]['active']
                confirmed = data[state]['districtData'][district]['confirmed']
                deaths = data[state]['districtData'][district]['deceased']
                recovered = data[state]['districtData'][district]['recovered']
                if district == 'Unknown':
                    active, confirmed, deaths, recovered = 0, 0, 0, 0
                tc.append([active, confirmed, deaths, recovered])
                act = act + active
                con = con + confirmed
                dea = dea + deaths
                rec = rec + recovered
            tc.append([act, con, dea, rec])
            dis.append('Total')
            parameters = ['Active', 'Confirmed', 'Deaths', 'Recovered']

            # creating a dataframe
            df = pd.DataFrame(tc, dis, parameters)
            print('COVID - 19', state, 'District Wise Data')
            print(df)

            # plotting of data
            # plt.bar(dis, df['Active'], width = 0.5, align = 'center')
            # fig = plt.gcf()
            # fig.set_size_inches(18.5, 10.5)
            # plt.xticks(rotation = 75)
            # plt.show()
            # print('*' * 100)
    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking India state wise data of  Covid 19
def calling_all_state_wise():
    try:
        url = 'https://www.coronaclusters.in/'
        # url = 'https://corona.help/'
        # url = 'https://covid19.who.int/table'
        df = pd.read_html(url)[0]
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(df)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking Petrol Prices
def checking_petrol_prices():
    try:
        # link for extract html data
        def getdata(url):
            r = requests.get(url)
            return r.text

        htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
        soup = BeautifulSoup(htmldata, 'html.parser')

        # Declare string var
        # Declare list
        mydatastr = ''
        result = []

        # searching all tr in the html data
        # storing as a string
        for table in soup.find_all('tr'):
            mydatastr += table.get_text()

        # set accourding to your required
        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split("\n\n")

        for item in itemlist[:-5]:
            result.append(item.split("\n"))

        # Calling DataFrame constructor on list
        df = pd.DataFrame(result[:-8])
        print(df)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking Petrol Prices
def checking_diesel_prices():
    try:
        # link for extract html data
        def getdata(url):
            r = requests.get(url)
            return r.text

        htmldata = getdata("https://www.goodreturns.in/diesel-price.html")
        soup = BeautifulSoup(htmldata, 'html.parser')

        # Declare string var
        # Declare list
        mydatastr = ''
        result = []

        # searching all tr in the html data
        # storing as a string
        for table in soup.find_all('tr'):
            mydatastr += table.get_text()

        # set accourding to your required
        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split("\n\n")

        for item in itemlist[:-5]:
            result.append(item.split("\n"))

        # Calling DataFrame constructor on list
        df = pd.DataFrame(result[:-8])
        print(df)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking CNG Gas Prices
def checking_cng_prices():
    try:
        # link for extract html data
        def getdata(url):
            r = requests.get(url)
            return r.text

        htmldata = getdata("https://www.goodreturns.in/cng-price.html")
        soup = BeautifulSoup(htmldata, 'html.parser')

        # Declare string var
        # Declare list
        mydatastr = ''
        result = []

        # searching all tr in the html data
        # storing as a string
        for table in soup.find_all('tr'):
            mydatastr += table.get_text()

        # set accourding to your required
        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split("\n\n")

        for item in itemlist[:-5]:
            result.append(item.split("\n"))

        # Calling DataFrame constructor on list
        df = pd.DataFrame(result[:-8])
        print(df)


    except ConnectionError as er:
        print(er)

    except Exception as err:
        print(err)


# Checking LPG Gas Prices
def checking_lpg_prices():
    try:
        # link for extract html data
        def getdata(url):
            r = requests.get(url)
            return r.text

        htmldata = getdata("https://www.goodreturns.in/lpg-price.html")
        soup = BeautifulSoup(htmldata, 'html.parser')

        # Declare string var
        # Declare list
        mydatastr = ''
        result = []

        # searching all tr in the html data
        # storing as a string
        for table in soup.find_all('tr'):
            mydatastr += table.get_text()

        # set accourding to your required
        mydatastr = mydatastr[1:]
        itemlist = mydatastr.split("\n\n")

        for item in itemlist[:-5]:
            result.append(item.split("\n"))

        # Calling DataFrame constructor on list
        df = pd.DataFrame(result[:-8])
        print(df)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Daily Horoscope
def horoscope(zodiac_sign: int, day: str) -> str:
    try:
        url = (
            "https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
        )
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        return soup.find("div", class_="main-horoscope").p.text


    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking IMDB Movies Rating
def getTitle(url):
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        for title in soup.findAll('div', {'class': 'title_wrapper'}):
            return title.find('h1').text.rstrip()

    except Exception as exc:
        print(exc)


def getInfo(movieUrl, userInput):
    try:
        html = requests.get(movieUrl)
        soup = BeautifulSoup(html.text, 'lxml')
        for div in soup.findAll('div', {'class': 'ratingValue'}):
            print('IMDB rating of \'' + userInput + '\' is: ', div.text)
            print()
            speak('task completed...')

        for div in soup.findAll('div', {'class': 'summary_text'}):
            print('Summary of  \'' + userInput + '\' : ')
            print(div.text.lstrip())


    except ConnectionError as er:

        print(er)

    except Exception as err:

        print(err)


# Checking Cricket Live Score
def checking_cricket_live_score():
    try:
        print('Live Cricket Matches:')
        print('=====================')
        speak("select your desire team")
        url = "http://static.cricinfo.com/rss/livescores.xml"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        i = 1
        for item in soup.findAll('item'):
            print(str(i) + '. ' + item.find('description').text)
            i = i + 1
        links = []
        for link in soup.findAll('item'):
            links.append(link.find('guid').text)

        print('Enter match number or enter 0 to exit:')
        while True:
            try:
                userInput = int(input())
            except NameError:
                print('Invalid input. Try Again!')
                continue
            except SyntaxError:
                print('Invalid input. Try Again!')
            if userInput < 0 or userInput > 30:
                print('Invalid input. Try Again!')
                continue
            elif userInput == 0:
                sys.exit()
            else:
                break

        url = links[userInput - 1]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        while True:
            matchUrl = links[userInput - 1]
            r = requests.get(matchUrl)
            soup = BeautifulSoup(r.text, 'lxml')
            score = soup.findAll('title')
            try:
                r.raise_for_status()
            except Exception as exc:
                print('Connection Failure. Try again!', exc)
                continue
            print(score[0].text + '\n')
            sleep(20)


    except ConnectionError as er:

        print(er)

    except Exception as err:

        print(err)


# Checking Stock Market
def checking_stocks_market():
    try:
        url = 'https://money.rediff.com/companies/market-capitalisation'
        df = pd.read_html(url)[0]
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(df)


    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking Gold Prices
def checking_gold_prices():
    try:
        # The webpage URL whose table we want to extract
        url = "https://www.goodreturns.in/gold-rates/#Weekly+%26+Monthly+Graph+of+Gold+Price+in+India"

        # Assign the table data to a Pandas dataframe
        table = pd.read_html(url)[0]  # use number which table you want [0],[1] etc
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

        # Print the dataframe
        print(table)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking Sliver Prices
def checking_sliver_prices():
    try:
        # The webpage URL whose table we want to extract
        url = "https://www.goodreturns.in/silver-rates/#Indian+Major+Cities+Silver+Rates+Today"

        # Assign the table data to a Pandas dataframe
        table = pd.read_html(url)[0]  # use number which table you want [0],[1] etc
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

        # Print the dataframe
        print(table)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking cryptocurrency Prices
def checking_bitcoin_prices():
    try:
        # url = 'https://cryptocurrencyprices.stockmaster.in/cryptocurrency-prices-in-inr-india/'
        # url = 'https://coinmarketcap.com/coins/views/all/'
        url = 'https://coinranking.com/'
        df = pd.read_html(url)[0]
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(df)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking IFSC Code
def checking_ifsc_code(ifsc_code):
    speak('Checking ifsc code ............')
    try:
        # Assign IFSC code and URL
        # IFSC_Code = 'SBIN0018666'
        URL = "https://ifsc.razorpay.com/"

        # Use get() method
        data = requests.get(URL + ifsc_code).json()
        print(
            "-------------------------------------------------Bank IFSC Code-----------------------------------------------------------------")
        for key, value in data.items():
            print(key, " :- ", value)


    except ConnectionError as er:

        print(er)

    except Exception as err:

        print(err)


# Checking Zip Code
def checking_zip_code(zipcode):
    try:
        # Using Nominatim Api
        geolocator = Nominatim(user_agent="geoapiExercises")

        # Using geocode()
        location = geolocator.geocode(zipcode)

        # Displaying address details
        print("Zipcode:", zipcode)
        print("Details of the Zipcode:")
        print(location)

    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking Domain Name
def checking_domain_name(domain_url):
    speak("Checking domain name....")
    try:
        domain_info = whois.whois(domain_url)

        for key, value in domain_info.items():
            print(str(key) + " : -  " + str(value))
    except ConnectionError as er:
        print(er)
    except Exception as err:
        print(err)


# Checking PNR Status for Indian Railway
def checking_pnr_status():
    try:
        pnr = input('Enter PNR : ')
        speak('Checking please wait..........')
        url = 'http://www.railyatri.in/pnr-status/' + pnr
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        crntStatus = soup.findAll('span', {'class': 'arrival_span'})
        bkngStatus = soup.findAll('span', {'class': 'departure'})
        print(bkngStatus)
        try:
            print('PNR Status', 'Booking Satus: ' + bs[1].text + '\n' + 'Curent Satus: ' + cs[2].text)
        except:
            print("Invalid PNR. Try again!")

    except requests.exceptions.ConnectionError:
        print("Connection Error. Try again!")


# Search meaning of any word from  Dictionary
def word_search_dictionary(self):
    speak("Activated Dictionary!")
    speak("Tell Me The Problem!")
    probl = self.takeCommand().lower()

    if 'meaning' in probl:
        probl = probl.replace("what is the", "")
        probl = probl.replace("jarvis", "")
        probl = probl.replace("of", "")
        probl = probl.replace("meaning of", "")
        result = Diction.meaning(probl)
        speak(f"The Meaning For {probl} is {result}")

    elif 'synonym' in probl:
        probl = probl.replace("what is the", "")
        probl = probl.replace("jarvis", "")
        probl = probl.replace("of", "")
        probl = probl.replace("synonym of", "")
        result = Diction.synonym(probl)
        speak(f"The Synonym For {probl} is {result}")

    elif 'antonym' in probl:
        probl = probl.replace("what is the", "")
        probl = probl.replace("jarvis", "")
        probl = probl.replace("of", "")
        probl = probl.replace("antonym of", "")
        result = Diction.antonym(probl)
        speak(f"The Antonym For {probl} is {result}")

    speak("Exited Dictionary!")


# Showing Wifi Password
def checking_connected_wifi_pwd():
    # now we will store the profiles data in "data" variable by
    # running the 1st cmd command using subprocess.check_output
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    # now we will store the profile by converting them to list
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    # using for loop in python we are checking and printing the wifi
    # passwords if they are available using the 2nd cmd command
    for i in profiles:
        # running the 2nd cmd command to check passwords
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                           'key=clear']).decode('utf-8').split('\n')
        # storing passwords after converting them to list
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        # printing the profiles(wifi name) with their passwords using
        # try and except method
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))


# if __name__ == "__main__":
# ------------------------------------------------------------------------------------------------------------------------------
class MainThread(QThread):
    print("Inside Thread Class")

    def __init__(self):
        super(MainThread, self).__init__()
        # self.run = self.run()

    # MultiThreading
    def run(self):
        # Checking System First
        checking_system()

        # Checking Internet first
        if connect():
            speak('checking Internet connection............')
            speak('Internet Connection is successfully established.....')
        else:
            speak('no internet Connection!!!, Connect Internet first.... ')

        # After Sleep mode wake up
        while True:
            permission = self.takeCommand().lower()
            if 'wake up' in permission or 'are you there' in permission or 'activate' in permission:
                self.taskExecution()
            elif 'goodbye' in permission or 'quite now' in permission:
                speak('Thanks for using me Sir.. Have a good day..')
                sys.exit()

    # take command from user
    # to convert voice into text
    def takeCommand(self):
        r = speech.Recognizer()
        with speech.Microphone(device_index=1) as source:
            print('Listening.....')
            r.pause_threshold = 1
            # For Noise
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source, timeout=4, phrase_time_limit=7)
            # audio = r.listen(source)  # ,timeout=5,phrase_time_limit=8)

        try:
            print('Recognizing.....')
            query = r.recognize_google(audio, language='en-in')
            print(f'user said :-  {query}')

        except Exception as ex:
            # speak('I don't understand...')
            # speak(f'Sorry Sir, Check Your Internet Connection... ')
            print(ex)
            return 'none'
        query = query.lower()
        return query

    # Task Execution
    def taskExecution(self):
        # Checking System First
        # checking_system()
        # Wishing
        wish()
        while True:
            # if 1:
            # query = takeCommand().lower()
            self.query = self.takeCommand()
            # _____________________________ _____Main Logic for Jarvis __________________________________
            # api_key = "xxxxxx-xxxxxxxxxx" Weather API Key Open Weather
            # __________________________________Opening Any Application ___________________________________________
            if 'open' in self.query:
                speak('Sure Sir')
                query = self.query
                open_application(query.lower())

            # __________________________________ Automation Opening Web  __________________________________________
            elif 'check' in self.query:
                speak('Sure Sir')
                webquery = self.query
                opening_web(self, webquery.lower())

            # __________________________________ Open any Website  __________________________________________
            elif 'go to website' in self.query:
                speak('which website do you want to visit....')
                website_name = self.takeCommand().lower()
                print(website_name)
                any_website_opener(website_name)

            # __________________________________ Open YouTube __________________________________________
            elif 'youtube search' in self.query:
                speak("OK sIR , This Is What I found For Your Search!")
                query = self.query.replace("jarvis", "")
                query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                speak("Done Sir!")

            # __________________________________  YouTube Automation __________________________________________
            elif 'youtube tool' in self.query:
                youtubeAuto(self)

            # __________________________________  Chrome Automation __________________________________________
            elif 'chrome automation' in self.query:
                chromeAuto(self)

            # __________________________________ Google Search Anything ___________________________________________
            elif 'google search' in self.query:
                speak("This Is What I Found For Your Search Sir!")
                query = self.query.replace("jarvis", "")
                query = self.query.replace("google search", "")
                kit.search(query)

            # __________________________________ Dictionary ___________________________________________
            elif 'dictionary' in self.query:
                word_search_dictionary(self)

            # __________________________________ Wifi Password ___________________________________________
            elif 'wifi password' in self.query:
                speak("Sir Before processing, it's illegal")
                checking_connected_wifi_pwd()

            # __________________________________ Checking PNR Status ___________________________________________
            elif 'pnr status' in self.query or 'show me pnr status' in self.query:
                checking_pnr_status()

            # __________________________________ Switching Window  __________________________________________
            elif 'switch window' in self.query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')

            # __________________________________ Showing Disk Usage  __________________________________________
            elif 'show me disk usage' in self.query or 'disk usage' in self.query:
                total_disk_usage()

            # __________________________________ Checking Internet Speed  __________________________________________
            elif 'show me internet speed' in self.query or 'internet speed' in self.query:
                speak("Checking........")
                stest = speedtest.Speedtest()
                s_download = stest.download()
                s_upload = stest.upload()
                speak(
                    f'we have {round(s_download, 2)} bit per second downloading speed and {round(s_upload, 2)} bit per second uploading speed')


            # __________________________________ Checking world Covid 19 Data  __________________________________________
            elif 'show me coronavirus data of world' in self.query:
                # calling the get_info method
                speak('Checking Covid-19 data of World...')
                checking_Worldometer()
            # __________________________________Checking India Covid-19 data ___________________________________________
            elif 'show me coronavirus data of india' in self.query:
                try:
                    # Error listening timed out while waiting for phrase to start
                    speak('which type of data you want to see... state wise or district wise')
                    select_data = self.takeCommand().lower()
                    if 'state wise' in select_data:
                        speak('Checking Covid-19 data of India for all state ...')
                        calling_all_state_wise()
                    elif 'district wise' in select_data:
                        speak('Checking Covid-19 data of India for every state ...')
                        # storing the url in the form of string
                        url = "https://api.covid19india.org/state_district_wise.json"
                        calling_every_state_wise(url)
                except Exception as exc:
                    print(exc)
            # __________________________________Checking live cricket score ___________________________________________
            elif 'show me cricket score' in self.query or 'tell me about cricket score' in self.query or 'check cricket score' in self.query:
                speak('Checking live cricket score............')
                checking_cricket_live_score()

            # __________________________________Checking stock market ___________________________________________
            elif 'show me stock market' in self.query:
                speak('Checking stock market............')
                checking_stocks_market()

            # __________________________________Checking gold prices ___________________________________________
            elif 'show me gold price' in self.query:
                speak('Checking gold price............')
                checking_gold_prices()

            # __________________________________Checking Sliver prices ___________________________________________
            elif 'show me sliver price' in self.query:
                speak('Checking sliver price............')
                checking_sliver_prices()

            # __________________________________Checking cryptocurrency prices ___________________________________________
            elif 'show me cryptocurrency price' in self.query:
                speak('Checking cryptocurrency price............')
                checking_bitcoin_prices()

            # __________________________________Checking cryptocurrency prices ___________________________________________
            elif 'show me ifsc code' in self.query:
                speak("please enter vaild ifsc code....")
                ifsc_code = input("Enter Here.....  ")
                checking_ifsc_code(ifsc_code)

            # __________________________________ Checking Petrol Pricing  __________________________________________
            elif 'show me petrol price' in self.query:
                speak('Checking petrol price')
                checking_petrol_prices()
            # __________________________________Checking Diesel Price __________________________________________
            elif 'show me diesel price' in self.query:
                speak('Checking diesel price')
                checking_diesel_prices()
            # __________________________________Checking CNG Gas Price __________________________________________
            elif 'show me cng gas price' in self.query:
                speak('Checking CNG Gas price')
                checking_cng_prices()
            # __________________________________Checking LPG Gas Price __________________________________________
            elif 'show me lpg gas price' in self.query:
                speak('Checking LPG Gas price')
                checking_lpg_prices()

            # __________________________________Checking Zip Code __________________________________________
            elif 'show me zip code' in self.query or 'show me pin code' in self.query:
                speak("Please enter valid zipcode...")
                # Zipocde input
                zipcode = input("Enter here...  ")
                checking_zip_code(zipcode)

            # __________________________________Checking Daily Horoscope __________________________________________

            elif 'show me daily horoscope' in self.query:
                speak('Checking daily horoscope...')
                print("Daily Horoscope. \n")
                print(
                    "enter your Zodiac sign number:\n",
                    "1. Aries\n",
                    "2. Taurus\n",
                    "3. Gemini\n",
                    "4. Cancer\n",
                    "5. Leo\n",
                    "6. Virgo\n",
                    "7. Libra\n",
                    "8. Scorpio\n",
                    "9. Sagittarius\n",
                    "10. Capricorn\n",
                    "11. Aquarius\n",
                    "12. Pisces\n",
                )
                zodiac_sign = int(input("number> ").strip())
                print("choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
                day = input("enter the day> ")
                horoscope_text = horoscope(zodiac_sign, day)
                print(horoscope_text)

            # __________________________________ Checking Movies Rating __________________________________________
            elif 'show me movies rating' in self.query or 'movies rating' in self.query:
                speak('tell me which moives rating do you want see ')
                userInput = input(('Enter Movie/Tv series name : '))
                print()
                speak('Checking please wait.........')
                url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q=' + userInput + '&s=all'

                html = requests.get(url)
                soup = BeautifulSoup(html.text, 'lxml')

                for td in soup.findAll('td', {'class': 'result_text'}):
                    link = td.find('a')['href']
                    movieUrl = 'http://www.imdb.com' + link
                    break

                name = getTitle(movieUrl)
                getInfo(movieUrl, userInput)

            # __________________________________ Checking Weather  __________________________________________
            elif 'show me weather' in self.query:
                weather(self)

            # __________________________________ Checking Domain Name  __________________________________________
            elif 'show me domain name' in self.query or 'check website domain' in self.query:
                speak('please provide me  domain name like......http://www.example.com')
                domain_url = input("enter here.....   ")
                checking_domain_name(domain_url)

                domain_url = input("please provide  domain(website) name......   ")

            # __________________________________ Organising FIle System __________________________________________
            elif 'manage files' in self.query or 'manage data' in self.query:

                EXT_VIDEO_LIST = ['FLV', 'WMV', 'MOV', 'MP4', 'MPEG', '3GP', 'MKV', 'AVI']
                EXT_IMAGE_LIST = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
                EXT_DOCUMENT_LIST = ['DOC', 'DOCX', 'PPT', 'PPTX', 'PAGES', 'PDF', 'ODT', 'ODP', 'XLSX', 'XLS', 'ODS',
                                     'TXT', 'IN',
                                     'OUT', 'MD']
                EXT_MUSIC_LIST = ['MP3', 'WAV', 'WMA', 'MKA', 'AAC', 'MID', 'RA', 'RAM', 'RM', 'OGG']
                EXT_CODE_LIST = ['CPP', 'RB', 'PY', 'HTML', 'CSS', 'JS']
                EXT_EXECUTABLE_LIST = ['LNK', 'DEB', 'EXE', 'SH', 'BUNDLE']
                EXT_COMPRESSED_LIST = ['RAR', 'JAR', 'ZIP', 'TAR', 'MAR', 'ISO', 'LZ', '7ZIP', 'TGZ', 'GZ', 'BZ2']

                # Taking the location of the Folder to Arrange
                try:
                    destLocation = str(sys.argv[1])
                except IndexError:
                    speak("Enter the Path of directory")
                    destLocation = str(input('Enter here...... : '))

                # When we make a folder that already exist then WindowsError happen
                # Changing directory may give WindowsError
                def ChangeDirectory(dir):
                    try:
                        os.chdir(dir)
                    except WindowsError:
                        print('Error! Cannot change the Directory')
                        print('Enter a valid directory!')
                        ChangeDirectory(str(input('Enter the Path of directory: ')))

                ChangeDirectory(destLocation)

                def Organize(dirs, name):
                    try:
                        os.mkdir(name)
                        print('{} Folder Created'.format(name))
                    except WindowsError:
                        print('{} Folder Exist'.format(name))

                    src = '{}\\{}'.format(destLocation, dirs)
                    dest = '{}\{}'.format(destLocation, name)

                    os.chdir(dest)
                    shutil.move(src, '{}\\{}'.format(dest, dirs))

                    print(os.getcwd())
                    os.chdir(destLocation)

                TYPES_LIST = ['Video', 'Images', 'Documents', 'Music', 'Codes', 'Executables', 'Compressed']
                for dirs in os.listdir(os.getcwd()):
                    if 1:
                        for name, extensions_list in zip(TYPES_LIST,
                                                         [EXT_VIDEO_LIST, EXT_IMAGE_LIST, EXT_DOCUMENT_LIST,
                                                          EXT_MUSIC_LIST,
                                                          EXT_CODE_LIST, EXT_EXECUTABLE_LIST, EXT_COMPRESSED_LIST]):
                            if dirs.split('.')[-1].upper() in extensions_list:
                                Organize(dirs, name)
                    else:
                        if dirs not in TYPES_LIST:
                            Organize(dirs, 'Folders')
                speak("task completed..")
                print('Done Arranging Files and Folder in your specified directory')




            # __________________________________How to Wiki ___________________________________________
            elif 'how to mod activate' in self.query:
                speak("Ok sir, How to do mode is activated...")
                while True:
                    speak("tell me what you want to know")
                    search_query_how = self.takeCommand()
                    try:
                        if 'exit' in search_query_how or 'close' in search_query_how or 'close now' in search_query_how or 'deactivate' in search_query_how:
                            speak("Ok sir, How to do mode deactivated")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(search_query_how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as ex:
                        speak("Sorry sir, I am not able to find this")


            # __________________________________Bitcoin Roll ___________________________________________
            elif 'bitcoin roll' in self.query:
                import freebitcoin

                freebitcoin.bitcoinRoll()

            # __________________________________Twitter Bot ___________________________________________
            elif 'can you tweet' in self.query:
                speak('Sure sir, what should i tweet')
                tweetCommand = self.takeCommand().lower()
                import TwitterBot

                tweet = tweetCommand
                TwitterBot.tweetBot(tweet)

            # __________________________________ Closing Notepad ___________________________________
            elif 'close notepad' in self.query:
                speak('Ok sir, CLosing Notepad...')
                os.system('taskkill /f /im notepad.exe')

            # __________________________________ Set An Alarm ___________________________________
            elif 'set alarm' in self.query:
                speak('sir please, tell me the time to set alarm,  for example, set alarm to 5.30am')
                tt = self.takeCommand().lower()  # set alarm to 5:30 am.
                tt = tt.replace('set alarm to ', "")  # 5:30 am.
                tt.replace(",", "")  # 5:30 am
                tt = tt.upper()  # 5:30 AM
                MyAlarm.alram(tt)

            # __________________________________ Joke ___________________________________
            elif 'tell me joke' in self.query:
                speak(pyjokes.get_joke())
            # __________________________________ Search Anything ___________________________________
            elif 'search' in self.query or 'play' in self.query:
                query = self.query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)
                speak(query)

            # __________________________________ battery usage ___________________________________
            elif 'how much power we have ' in self.query or 'how much power left' in self.query or 'battery' in self.query:
                battery_power()

            # __________________________________ cpu and battery usage ___________________________________
            elif 'cpu and battery' in self.query or 'battery' in self.query or 'cpu' in self.query:
                cpu()

            # __________________________________ Shut Down System ___________________________________
            elif 'shutdown the system' in self.query:
                speak('processing,Your system is on its way to shut down')
                os.system('shutdown /s /t 5')

            # __________________________________ Restart System ___________________________________
            elif 'restart the system' in self.query:
                speak('processing,Your system is on its way to restarting')
                os.system('shutdown /r /t 5')

            # __________________________________ Sleep System ___________________________________
            elif 'sleep the system' in self.query:
                speak('processing,Your system is on its way to Sleeping')
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

            # __________________________________ Empty Recycle Bin ___________________________________
            elif 'clean recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            # __________________________________ Change Background ___________________________________
            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "H:\\wallpaper",
                                                           0)
                speak("Background changed succesfully")

            # __________________________________ Reading News ___________________________________
            elif 'news' in self.query:
                speak('please wait sir, fetching latest news')
                news()
            # __________________________________ Lock Window ___________________________________
            elif 'lock the system' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            #  __________________________________Open Cmd_______________________________________________
            elif 'open command prompt' in self.query:
                speak('opening command prompt')
                os.system('start cmd')

            # __________________________________Open Camera ____________________________________________
            elif 'open camera' in self.query:
                speak('opening web camera')
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            # __________________________________ Music Player __________________________________________
            elif ' play music' in self.query or 'play song' in self.query or 'stop music' in self.query or 'next' in self.query or 'pause music' in self.query or 'previous' in self.query:
                if 'play music' in self.query or 'play song' in self.query:
                    speak('Searching Music')
                    music_dir = 'H:\\music'
                    songs = os.listdir(music_dir)
                    # for random songs
                    # rd = random.choice(songs)
                    # Play only Mp3 Songs
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))

                if 'stop music' in self.query:
                    print('stop')
                elif 'next' in self.query:
                    print('next')
                elif 'previous' in self.query:
                    print('previous')
                elif 'pause' in self.query:
                    print('previous')

            # __________________________________ Volume Up __________________________________________
            elif 'volume up' in self.query:
                speak('ok volume up')
                pyautogui.press("volumeup")

            # __________________________________ Volume Down __________________________________________
            elif 'volume down' in self.query:
                speak('ok volume Down')
                pyautogui.press("volumedown")

            # __________________________________ Volume Up __________________________________________
            elif 'volume mute' in self.query or 'mute' in self.query:
                speak('ok volume mute')
                pyautogui.press("volumemute")



            # __________________________________ IP Addresses __________________________________________
            elif 'what is my ip address' in self.query:
                speak('Checking Your Ip Address')
                ip = get('https://api.ipify.org').text
                speak(f'Sir Your Ip Address is {ip}')

            # _______________________ To Find Location Using IP Address __________________________________
            elif 'where i am' in self.query or 'where we are' in self.query:
                speak('Wait Sir, Let me Check')
                try:
                    check_ip = get('https://api.ipify.org').text
                    print(check_ip)
                    url = 'https://get.geojs.io/v1/ip/geo/' + check_ip + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f'Sir i am not sure but i think we are in {city} city of {state} state in {country} country')
                except Exception as ex:
                    speak('Sorry Sir, Due to network issue i am not able to find to accurate location')
                    print(ex)

            # __________________________________ Check Instagram Profile _________________________________________
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak('Sir, Please enter instagram username correctly')
                username = input('Enter username here....')
                webbrowser.open(f'https://www.instagram.com/{username}')
                speak(f'Sir, here is the profile of the user {username}')
                time.sleep(5)
                speak('Sir, Would you like to download profile picture of this account')
                downPic = self.takeCommand().lower()
                if 'yes' in downPic:
                    mod = instaloader.Instaloader()  # pip install Instaloader
                    mod.download_profile(username, profile_pic_only=True)
                    speak(
                        'Sir,Profile Picture download Successfully and save in main folder. Now i am ready to next command')
                elif 'no' in downPic:
                    pass
                else:
                    pass

            # __________________________________ Taking Screenshot ____________________________________________
            elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                speak('Sir, Tell me the name for this screenshot file')
                screenshotFile = self.takeCommand().lower()
                speak('Sir, Please hold the screen for few seconds.., I am taking screenshot')
                time.sleep(5)
                img = pyautogui.screenshot()
                img.save(f'{screenshotFile}.png')
                speak('Sir,i am done , the screenshot saved in main folder. now i am ready for next command')

            # __________________________________ Whatsapp _______________________________________________
            # elif 'send whatsapp message' in self.query:
            #     try:
            #         speak('Opening Whatsapp')
            #         speak('Sir what should i send....')
            #         self.whatmsg = self.takeCommand().lower()
            #         kit.sendwhatmsg('+919950532198', f'{self.whatmsg}', 2, 25)
            #     except Exception:
            #         # raise InternetException("NO INTERNET - Whatsapp needs active internet connection")
            #         speak('Sorry Sir, Internet Connection Problem...')
            #
            # # __________________________________ Play Specific Video on uTube ____________________________
            # elif 'play song on youtube ' in self.query:
            #     speak('Searching Song on Youtube')
            #     """Will play video on following topic, takes about 10 to 15 seconds to load"""
            #     kit.playonyt('see you again')

            # __________________________________ Send Email _______________________________________________
            elif 'send email' in self.query:
                sendEmail(self.query)

            # __________________________________ To Read pdf file _______________________________________________
            elif 'read pdf' in self.query:
                pdf_reader()

            # __________________________________ To Hide files and Folders _______________________________________________
            elif 'hide all files' in self.query or 'hide this folder' in self.query or 'hidden this folder' in self.query or 'visible to everyone' in self.query:
                hide_files_folders(self)

            # __________________________________ waiting ________________________________________________
            elif 'wait' in self.query:
                speak('Ok Sir, I think you are thinking something new for me...')
                speak('I am sleeping for 5 seconds')
                time.sleep(5)

            # __________________________________ greeting ________________________________________________
            elif 'hello' in self.query or 'hey' in self.query:
                speak('hello sir, may i help you with something')

            elif 'how are you' in self.query:
                speak('I am fine sir..What about you...')

            elif 'good' in self.query or 'also fine' in self.query or 'fine' in self.query or 'very well' in self.query or 'well good' in self.query:
                speak("that's great to hear from you")

            elif 'thank you' in self.query or 'thanks' in self.query:
                speak("it's my pleasure sir")

            # __________________________________ jarvis features ________________________________________________
            elif "tell me your powers" in self.query or "features" in self.query:
                features = ''' i can help to do lot many things like..
                        i can tell you the current time and date,
                        i can tell you the current weather,
                        i can tell you battery and cpu usage,
                        i can create the reminder list,
                        i can take screenshots,
                        i can send email to your boss or family or your friend,
                        i can shut down or logout or hibernate your system,
                        i can tell you non funny jokes,
                        i can open any website,
                        i can search the thing on wikipedia,
                        i can change my voice from male to female and vice-versa
                        And yes one more thing, My boss is working on this system to add more features...,
                        tell me what can i do for you??
                        '''
                print(features)
                speak(features)
            # __________________________________ Help Command ________________________________________________
            elif "help" in self.query:
                pass
            # __________________________________ Start Application ________________________________________________
            elif 'start' in self.query:
                os.system('explorer C://{}'.format(self.query.replace('start', '')))

            # __________________________________ Create New Reminder ________________________________________________

            elif 'create a reminder list' in self.query or 'reminder' in self.query:
                speak("What is the reminder?")
                data = self.takeCommand().lower()
                speak("You said to remember that" + data)
                try:
                    reminder_file = open("note//remember.txt", 'a')
                    reminder_file.write('\n')
                    reminder_file.write(data)
                    reminder_file.close()
                except Exception as e:
                    speak(e)

            # __________________________________ reading reminder list ________________________________________________

            elif 'do you know anything' in self.query or 'remember' in self.query:
                try:
                    reminder_file = open("note//remember.txt", 'r')
                    speak("You said me to remember that: " + reminder_file.read())
                except Exception as e:
                    speak(e)
            # __________________________________ Search Using wolframalpha _____________________________________________
            elif "what is" in self.query or "who is" in self.query or "where is" in self.query or "why we" in self.query:

                # Use the same API key
                # that we have generated earlier
                appId = "xxxxxx-xxxxxxxxxx"
                client = wolframalpha.Client(appId)
                res = client.query(self.query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            # __________________________________ Wikipedia _____________________________________________
            elif 'wikipedia' in self.query or 'what' in self.query or 'who' in self.query or 'when' in self.query or 'where' in self.query:
                query = self.query
                searching_wiki(query.lower())

            # __________________________________ Calender of Any Year _____________________________________________
            elif 'show me calender' in self.query:
                speak('which year do you want to see calender')
                query = self.takeCommand().lower()
                year = int(query)
                # input the year
                #  year=int(input("Enter year: "))

                # printing the calendar
                print("The calenar is...")
                print(calendar.calendar(year))

            # __________________________________ Exit ________________________________________________
            elif 'you can sleep' in self.query or 'sleep now' in self.query or 'you need a break' in self.query:
                # speak('Thanks for using me Sir.. Have a good day..')
                speak('okay sir, i am going to sleep you can call me anytime')
                break
                # break while and return main loop

            # __________________________________ If Query Nothing _____________________________________________
            elif self.query == 'none':
                continue
            # __________________________________ Calculations _____________________________________________
            elif 'calculations' in self.query or 'can you some calculate' in self.query:
                speak('tell me what you want to calculate enter your questions')
                try:
                    question = input('Question: ')
                    speak('choose number 1 and 2')
                    print('---------------------------------------------------------------')
                    print('Choose 1. --------------Only Answer-------------')
                    print('Choose 2. --------------Full Description-------------')
                    print('---------------------------------------------------------------')

                    choose = int(input('enter your choise \n'))
                    if choose == 1:
                        # App id obtained by the above steps
                        # write your wolframalpha app_id here
                        app_id = "HVL5LL-89PY69U3AY"
                        # Instance of wolf ram alpha
                        # client class
                        client = wolframalpha.Client(app_id)

                        # Stores the response from
                        # wolf ram alpha
                        res = client.query(question)

                        # Includes only text from the response
                        answer = next(res.results).text

                        speak('Your answer is...')
                        print(answer)

                    elif choose == 2:
                        import wolbot
                        wolbot.wol(question)
                    else:
                        print('Choose correct Number')
                except Exception as e:
                    print(e)


# speak('Sir, Do you have any another work?')


# Class Object
startExecution = MainThread()


# --------------------------------------------------------------------------------------------------------------------------------
class MainFile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_assistance_gui()
        self.ui.setupUi(self)
        self.setFixedSize(789, 600)
        # self.ui.pushButton.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close)
        self.startTask()

    def startTask(self):
        # print("Hello Sir")
        self.ui.movie = QtGui.QMovie("jarvis_images/speech.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("jarvis_images/heart.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("jarvis_images/initialse.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("jarvis_images/rat.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("jarvis_images/2voice_recognition_process_by_gleb.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("jarvis_images/datetime.jpg")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        # Time
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        # Calling Object of mainThread Class
        startExecution.start()
        print("At the end")

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
main_file = MainFile()
main_file.show()
exit(app.exec_())
