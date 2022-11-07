from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import defaultdict
from selenium.webdriver.common.keys import Keys
import time
import security
from random import randint
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options


FACEBOOK_EMAIL = security.FACEBOOK_EMAIL
FACEBOOK_PASSWORD = security.FACEBOOK_PASSWORD


driver = webdriver.Firefox()
driver.get("https://tinder.com/")


time.sleep(2)
login = driver.find_element(by="xpath", value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(2)
fb_login = driver.find_element(by="xpath", value='/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(1)
email = driver.find_element(by="name", value="email")
email.send_keys(FACEBOOK_EMAIL)
time.sleep(1)
password = driver.find_element(by="name", value="pass")
password.send_keys(FACEBOOK_PASSWORD)
time.sleep(1)
fb_login2 = driver.find_element(by="id", value="loginbutton")
fb_login2.click()

driver.switch_to.window(base_window)

# ALLOW
time.sleep(5)
allow = driver.find_element(by="xpath", value='/html/body/div[2]/main/div/div/div/div[3]/button[1]')
allow.click()

# NOT INTERESTED
time.sleep(3)
not_interested = driver.find_element(by="xpath", value='/html/body/div[2]/main/div/div/div/div[3]/button[2]')
not_interested.click()

# NO DARK MODE
exit = driver.find_element(by="xpath", value='/html/body/div[2]/main/div/div[2]/button')
exit.click()

i = 0
time.sleep(5)
# START NOPING
# while count < 6:
#     nope = driver.find_element(by="xpath", value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
#     nope.click()
#     count += 1
#     time.sleep(10)

while i < 99:
    try:
        photo_div = driver.find_element(by="xpath", value=
            'html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[1]')
        # finding contact photo element
        action = webdriver.ActionChains(driver=driver)
        # creates action object for webdriver
        action.drag_and_drop_by_offset(source=photo_div, xoffset=-200, yoffset=0).perform()
        # performs d&d action
        print("Sorry, I'm married.")
        time.sleep(3)  # function call to return random wait time
        i += 1
    except NoSuchElementException:
        print("Photo div not found")
        time.sleep(3)

# div.Bdc($c-ds-border-gamepad-nope-default) button.button
# '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'


# time.sleep(2)
# not_interested = driver.find_elements(by="tag name", value='div')
# for n in not_interested:
#     if n.text == "NOT INTERESTED":
#         n.click()
#         break
#
# time.sleep(2)
# no_thanks = driver.find_elements(by="tag name", value='div')
# for n in no_thanks:
#     if n.text == "NO THANKS":
#         n.click()
#         break