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

def fbAutoBot(myFbPost):
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    fbEmail = config.facebook_email
    fbPassword = config.facebook_password

    driver.maximize_window()
    driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')

    emailfb_xPath = '//*[@id="email"]'
    passwordfb_xPath = '//*[@id="pass"]'
    # loginfb_xPath = "//button[@id='loginbutton']"
    button = driver.find_element_by_xpath('//*[@id="loginbutton"]')

    driver.find_element_by_xpath(emailfb_xPath).send_keys(fbEmail)
    time.sleep(0.5)
    driver.find_element_by_xpath(passwordfb_xPath).send_keys(fbPassword)
    time.sleep(0.5)
    driver.implicitly_wait(10)
    button.click()
    # driver.find_element_by_id(loginfb_xPath).click()
    time.sleep(2)

    myFbPost =''