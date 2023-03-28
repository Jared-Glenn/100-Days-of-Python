from selenium import webdriver
import time
from jump_brain import JumpBrain



driver = webdriver.Chrome()
jumpbrain = JumpBrain()

driver.get("https://elgoog.im/t-rex/")

time.sleep(2)

jumpbrain.jump()

for x in range(1000):
    jumpbrain.timeToJump()
    if x%10 == 0:
        y = x/10
        jumpbrain.screenshot(y)

time.sleep(2) 
