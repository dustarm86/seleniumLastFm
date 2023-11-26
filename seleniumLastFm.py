import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://www.last.fm/user/dustArm421")
get_title = browser.title
assert "dustArm421’s Music Profile | Last.fm" in browser.title == get_title
time.sleep(5)
topArtist1 = browser.find_element("xpath", "/html/body/div[6]/div[2]/div[5]/div[3]/div/div[1]/section[3]/div/ol/li[1]/div/a").click()
time.sleep(3)
browser.quit()