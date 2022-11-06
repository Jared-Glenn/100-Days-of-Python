from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import security
import time

LINKEDIN_EMAIL = security.LINKEDIN_EMAIL
LINKEDIN_PASSWORD = security.LINKEDIN_PASSWORD

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/")

signin = driver.find_element(by="link text", value="Sign in")
signin.click()

username = driver.find_element(by="id", value="username")
username.send_keys(LINKEDIN_EMAIL)
password = driver.find_element(by="id", value="password")
password.send_keys(LINKEDIN_PASSWORD)
signin = driver.find_element(by="tag name", value="button")
signin.click()


# Python Jobs
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3318515038&f_"
           "AL=true&f_E=2%2C3%2C4&f_JT=F&f_TPR=r86400&f_WT=2&geoId=103644278&"
           "keywords=Python&location=United%20States&refresh=true")

time.sleep(2)

driver.save_screenshot("python_jobs.png")

jobs = driver.find_elements(by="css selector", value=".job-card-list")

for i in range(4):
    count = 1
    job = jobs[i]
    job.click()
    time.sleep(1)
    easy_apply = driver.find_element(by="css selector", value="div.jobs-apply-button--top-card")
    easy_apply.click()
    time.sleep(1)
    for _ in range(10):
        count +=1
        time.sleep(1)
        main_button = driver.find_element(by="class name", value="artdeco-button--primary")
        if main_button.text == "Next":
            main_button.click()
        elif main_button.text == "Review":
            main_button.click()
        else:
            cancel = driver.find_element(by="css selector", value="button.artdeco-modal__dismiss")
            cancel.click()
            time.sleep(1)
            discard = driver.find_element(by="css selector", value="button.artdeco-button--secondary")
            discard.click()
            break
    if count >= 10:
        cancel = driver.find_element(by="css selector", value="button.artdeco-modal__dismiss")
        cancel.click()
        time.sleep(1)
        discard = driver.find_element(by="css selector", value="button.artdeco-button--secondary")
        discard.click()

# Web Dev Jobs
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3338782410&f_"
           "AL=true&f_E=2%2C3%2C4&f_JT=F&f_TPR=r86400&f_WT=2&geoId=103644278&"
           "keywords=javascript%20developer&location=United%20States&refresh=true")

time.sleep(2)

driver.save_screenshot("webdev_jobs.png")

jobs = driver.find_elements(by="css selector", value=".job-card-list")

for i in range(4):
    count = 1
    job = jobs[i]
    job.click()
    time.sleep(1)
    easy_apply = driver.find_element(by="css selector", value="div.jobs-apply-button--top-card")
    easy_apply.click()
    time.sleep(1)
    for _ in range(10):
        count +=1
        time.sleep(1)
        main_button = driver.find_element(by="class name", value="artdeco-button--primary")
        if main_button.text == "Next":
            main_button.click()
        elif main_button.text == "Review":
            main_button.click()
        else:
            cancel = driver.find_element(by="css selector", value="button.artdeco-modal__dismiss")
            cancel.click()
            time.sleep(1)
            discard = driver.find_element(by="css selector", value="button.artdeco-button--secondary")
            discard.click()
            break
    if count >= 10:
        cancel = driver.find_element(by="css selector", value="button.artdeco-modal__dismiss")
        cancel.click()
        time.sleep(1)
        discard = driver.find_element(by="css selector", value="button.artdeco-button--secondary")
        discard.click()

# Data Scientist
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3327499254&f_AL=true&f_"
           "E=2%2C3%2C4&f_JT=F&f_TPR=r86400&f_WT=2&geoId=103644278&keywords=Data%20Scientist&"
           "location=United%20States&refresh=true")

time.sleep(2)

driver.save_screenshot("data_science_jobs.png")

jobs = driver.find_elements(by="css selector", value=".job-card-list")

for i in range(4):
    count = 1
    job = jobs[i]
    job.click()
    time.sleep(1)
    easy_apply = driver.find_element(by="css selector", value="div.jobs-apply-button--top-card")
    easy_apply.click()
    time.sleep(1)
    for _ in range(10):
        count +=1
        time.sleep(1)
        main_button = driver.find_element(by="class name", value="artdeco-button--primary")
        if main_button.text == "Next":
            main_button.click()
        elif main_button.text == "Review":
            main_button.click()
        else:
            cancel = driver.find_element(by="css selector", value="button.artdeco-modal__dismiss")
            cancel.click()
            time.sleep(1)
            discard = driver.find_element(by="css selector", value="button.artdeco-button--secondary")
            discard.click()
            break
    if count >= 10:
        cancel = driver.find_element(by="css selector", value="button.artdeco-modal__dismiss")
        cancel.click()
        time.sleep(1)
        discard = driver.find_element(by="css selector", value="button.artdeco-button--secondary")
        discard.click()



# driver.quit()


# driver.find_element(by="link text", value="")