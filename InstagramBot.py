# Author: Deendayal Kumawat
"""
Date: 05/02/21
Descriptions: AI Assistance(Jarvis)
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import config

def instaGramBot(myInstaPost):
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    instaEmail = config.instagram_email
    instaPassword = config.instagram_password

    driver.maximize_window()
    driver.get('https://www.instagram.com/')
    myInstaPost = ''

    emailinsta_xPath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    passwordinsta_xPath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    logininsta_xPath = '//*[@id="loginForm"]/div/div[3]'
    time.sleep(2)

    driver.find_element_by_xpath(emailinsta_xPath).send_keys(instaEmail)
    time.sleep(0.5)
    driver.find_element_by_xpath(passwordinsta_xPath).send_keys(instaPassword)
    time.sleep(0.5)
    driver.find_element_by_xpath(logininsta_xPath).click()
    time.sleep(2)

