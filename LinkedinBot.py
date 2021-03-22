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

def linkedlinBot():
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    email = config.linkedlinEmail
    password = config.linkedinpassword
    # tweet = 'this is demo tweet'
    driver.maximize_window()
    # driver.webdriver.chrome(options = options)
    driver.get('https://www.linkedin.com/login')

    email_xPath = '//*[@id="username"]'
    password_xPath = '//*[@id="password"]'
    signIn_xPath = '/html/body/div/main/div[2]/div[1]/form/div[3]/button'
    time.sleep(2)

    driver.find_element_by_xpath(email_xPath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(password_xPath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(signIn_xPath).click()
    time.sleep(2)

    # After Login
    # Check Notification
    check_notification_xPath = '//*[@id="ember30"]'
    driver.find_element_by_xpath(check_notification_xPath).click()


