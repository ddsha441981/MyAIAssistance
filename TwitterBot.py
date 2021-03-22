from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import config

def tweetBot(tweet):
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    email = config.twitterUsername
    password = config.twitterPassword
    # tweet = 'this is demo tweet'
    driver.maximize_window()
    # driver.webdriver.chrome(options = options)

    driver.get('https://www.twitter.com//login')
    email_xPath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    pass_xPath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    login_xPath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'
    time.sleep(2)

    driver.find_element_by_xpath(email_xPath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(pass_xPath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(login_xPath).click()

    # Tweet Button
    tweet_xPath = '/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]'
    message_xPath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
    post_xPath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'
    time.sleep(5)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(tweet_xPath).click()
    time.sleep(0.5)
    driver.find_element_by_xpath(message_xPath).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element_by_xpath(post_xPath).click()
    time.sleep(2)



# driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[3]/div/div/a[1]/span").click()
# time.sleep()