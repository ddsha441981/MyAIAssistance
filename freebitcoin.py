from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config

def mainRoll():
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    while True:
        driver.get("http://bitcoin.works")
        driver.maximize_window()
        time.sleep(2)

        driver.find_element_by_link_text("LOGIN").click()
        time.sleep(2)
        driver.find_element_by_id("login_form_btc_address").send_keys(config.username)
        driver.find_element_by_id("login_form_password").send_keys(config.password)
        driver.find_element_by_class_name("pushpad_deny_button").click()
        time.sleep(2)

        # Accept Cookies
        driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()
        time.sleep(5)
        # Login Access
        driver.find_element_by_id("login_button").click()
        time.sleep(4)
        # Deny Button Pop Up
        if driver.find_element_by_class_name("pushpad_deny_button") == True:

            driver.find_element_by_class_name("pushpad_deny_button").click()
            time.sleep(7)
        else:
            print('Pushpad deny button nothing found')
            pass

        # Scrolling Down Web Page Script
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        # Captcha code
        # driver.find_element_by_class_name('play_without_captcha_button center').click()
        # driver.find_element_by_id('play_without_captchas_button').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[8]/div[2]/div/div[1]/div[1]').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
        time.sleep(5)

        # # Roll Button
        driver.find_element_by_id("free_play_form_button").click()
        time.sleep(5)

        # Scrolling Up Web Page Script
        driver.execute_script("scrollBy(0,-1000)")
        time.sleep(3)

        # Multiple Bet
        driver.find_element_by_link_text('MULTIPLY BTC').click()
        time.sleep(10)

        # Scrolling Down Web Page Script
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        # Scrolling middle Web Page Script
        driver.execute_script("scrollBy(0,-1400)")
        time.sleep(3)

        # Manual Bet
        driver.find_element_by_id('manual_bet_on').click()
        time.sleep(5)

        # High Bet
        driver.find_element_by_id('double_your_btc_bet_hi_button').click()
        time.sleep(5)

        winners = driver.find_elements_by_class_name('bold center double_your_btc_bet_win_message')
        if winners == True:
            print('inside/////////////////////////////////////////////////////////////////////////////////')
            # High Bet
            driver.find_element_by_id('double_your_btc_bet_hi_button').click()
            time.sleep(5)
        elif driver.find_element_by_class_name('bold center double_your_btc_bet_lose_message') == True:
            pass
        else:
            pass

        # Close driver
        driver.quit()
    time.sleep(3610)

mainRoll()