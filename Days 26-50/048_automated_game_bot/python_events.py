from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

times = [time.text for time in driver.find_elements(by="css selector", value="div.event-widget time")]
# time_elements = driver.find_elements(by="css selector", value="div.event-widget time")
# for time in time_elements:
#     times.append(time.text)

events = [event.text for event in driver.find_elements(by="css selector", value="div.event-widget ul.menu a")]
# event_elements = driver.find_elements(by="css selector", value="div.event-widget ul.menu a")
# for event in event_elements:
#     events.append(event.text)

event_calendar = {}
for i in range(len(events)):
    event_calendar[i] = {}
    event_calendar[i]["time"] = times[i]
    event_calendar[i]["name"] = events[i]

print(event_calendar)

driver.quit()
