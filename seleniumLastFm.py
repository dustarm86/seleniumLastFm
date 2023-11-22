import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.last.fm/user/dustArm421")
get_title = browser.title
assert "dustArm421’s Music Profile | Last.fm" in browser.title == get_title
#print(get_title)
time.sleep(3)
browser.quit()