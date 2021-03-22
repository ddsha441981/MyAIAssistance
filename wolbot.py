from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def wol(question):
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.maximize_window()
    driver.get('https://www.wolframalpha.com/')
    search_xpath = '//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/div/div/input'
    buttonXpath = '//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/button'
    time.sleep(2)

    driver.find_element_by_xpath(search_xpath).send_keys(question)
    driver.find_element_by_xpath(buttonXpath).click()
    time.sleep(5000000)