from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import security

class SpeedAndTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = None
        self.up = None
        self.username = security.TWITTER_USERNAME
        self.password = security.TWITTER_PASSWORD

    def get_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        start = self.driver.find_element(by="class name", value="js-start-test")
        start.click()

        time.sleep(3)

        WebDriverWait(self.driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.result-item-id div.result-data a")))

        download = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        upload = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.down = download.text
        self.up = upload.text

    def tweet(self):
        self.driver.get("https://twitter.com/")

        login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
        login.click()

        time.sleep(2)

        username = self.driver.find_element(By.TAG_NAME, "input")
        username.send_keys(self.username)
        time.sleep(1)
        next = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next.click()

        time.sleep(2)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password)
        time.sleep(2)
        finish = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        finish.click()

        time.sleep(2)

        WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div")))
        twitt = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div")
        twitt.click()
        print("found it!")
        time.sleep(1)
        try:
            maybe_later = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div/span/span")
            maybe_later.click()
        except:
            pass
        twitt_again = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        twitt_again.click()
        twitt_again.send_keys(f"Wow! This is so dang slow! {self.down} Mbps Download and {self.up} Mbps Upload! I'm furious!")

        tweet_that = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet_that.click()

        time.sleep(300)
