# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
# option = webdriver.FirefoxOptions()
# option.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# serv = Service("C:/Users/Jared/Documents/3. Programming/Tools/geckodriver.exe")
# driver = webdriver.Firefox(service=serv, options=option)
#
# driver.get("https://www.amazon.com/")


from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/dp/B01H5QZ5X8/?coliid=IROY8T4TZ1591&colid=1SKL8BAZVNVL3&psc=1&ref_=lv_ov_lig_dp_it")

price = driver.find_element(by="xpath", value='/html/body/div[1]/div[3]/div[9]/div[4]/div[4]/div[10]/div/div[1]/div[3]/div[1]/span[2]/span[1]')
print(price.text)


driver.quit()
















































