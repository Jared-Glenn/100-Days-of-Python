from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FormFiller():
    def __init__(self, list):
        self.driver = webdriver.Chrome()
        self.listings = list

    def fill_form(self):
        time.sleep(5)
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfVj1me8HVYE_"
                        "oUVzEeHH2KNRxB4f-nYiYrNaJhRNBK1sot9Q/viewform?usp=sf_link")


        for listing in self.listings:
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/"
                                                                                      "div/div[2]/div[1]/div/div/"
                                                                                      "div[2]/div/div[1]/div/div[1]/"
                                                                                      "input")))

            address = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/"
                                                        "div/div[2]/div[1]/div/div/"
                                                        "div[2]/div/div[1]/div/div[1]/"
                                                        "input")
            address.send_keys(listing["address"])
            time.sleep(1)

            price = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/" \
                                                                       "div[2]/div/div/div[2]/" \
                                                                       "div/div[1]/div/div[1]/input")
            price.send_keys(listing["price"])
            time.sleep(1)

            link = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/"
                                                      "div/div[2]/div/div[1]/div/div[1]/input")
            link.send_keys(listing["link"])
            time.sleep(1)

            submit = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
            submit.click()
            time.sleep(1)

            another = self.driver.find_element(By.LINK_TEXT, "Submit another response")
            another.click()