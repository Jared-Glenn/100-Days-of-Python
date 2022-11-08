from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import security

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = security.INSTAGRAM_USERNAME
        self.password = security.INSTAGRAM_PASSWORD

    def login(self):
        self.driver.get("https://www.instagram.com/")

        time.sleep(2)

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(self.username)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password)
        time.sleep(1)
        login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/"
                                                   "div[1]/section/main/article/div[2]/div[1]/div[2]/"
                                                   "form/div/div[3]/button")
        login.click()

        time.sleep(7)
        self.driver.get("https://www.instagram.com/locke.photography/followers")

        time.sleep(1)

    def follow(self):

        pop_up_window = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "//div[@class='_aano']")))

        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                                       pop_up_window)
            time.sleep(1)


        follower_section = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/"
                                                              "div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        followers = follower_section.find_elements(By.TAG_NAME, "button")

        print(len(followers))

        for follower in followers:
            if follower.text == "Follow":
                follower.click()
                time.sleep(1)
            else:
                continue

        time.sleep(300)