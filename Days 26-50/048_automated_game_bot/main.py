from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

language = driver.find_element(by="xpath", value='//*[@id="langSelect-EN"]')
language.click()

time.sleep(3)

cookie = driver.find_element(by="id", value="bigCookie")

def buy_product():
    item = None
    upgrade = None
    store_items = driver.find_elements(by="css selector", value="#products div.enabled")
    store_upgrades = driver.find_elements(by="css selector", value="#upgrades div.enabled")
    item_num = len(store_items)
    if item_num != 0:
        item = store_items[item_num - 1]
    upgrade_num = len(store_upgrades)
    if upgrade_num != 0:
        upgrade = store_upgrades[upgrade_num - 1]
    if upgrade:
        upgrade.click()
    elif item:
        item.click()

def check_for_gold():
    try:
        golden_cookie = driver.find_element(by="class name", value="shimmer")
        golden_cookie.click()
    except:
        pass


looping = True
time_passing = 6
time_to_buy = time.time() + time_passing
game_over = time.time() + 300

while looping:
    cookie.click()
    if time.time() > time_to_buy:
        buy_product()
        check_for_gold()
        time_to_buy += time_passing
        if time.time() > game_over:
            cps = driver.find_element(by="id", value="cookiesPerSecond")
            print(f"Cookies {cps.text}")
            driver.save_screenshot("ss.png")
            driver.quit()

