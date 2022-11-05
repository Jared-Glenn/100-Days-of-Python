from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # For id, use "css selector" with a value of "#idname
#
# stats = driver.find_element(by="xpath", value="/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
#
# # stats.click()
#
# all_portals = driver.find_element(by="link text", value="November 5")
#
# # all_portals.click()
#
# search = driver.find_element(by="name", value="search")

# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(by="name", value="fName")
fName.send_keys("Jacob")

lName = driver.find_element(by="name", value="lName")
lName.send_keys("Marley")

email = driver.find_element(by="name", value="email")
email.send_keys("jacobmarley@scrooge.com")

signup = driver.find_element(by="tag name", value="button")
signup.click()








# driver.quit()

