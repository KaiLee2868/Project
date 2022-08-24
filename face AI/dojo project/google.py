from socket import AddressFamily
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import json
from test import Unit


driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp?hl=en&tab=ri&authuser=0&ogblm/")
elem = driver.find_element_by_name("q")
elem.send_keys("Jessica Biel")
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
time.sleep(3)
img_url=(driver.find_element_by_css_selector(".n3VNCb").get_attribute("src"))
urllib.request.urlretrieve(img_url,"star.jpg")
Unit.find_face()

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp?hl=en&tab=ri&authuser=0&ogblm/")
elem = driver.find_element_by_name("q")
elem.send_keys(Unit.result_face())
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
time.sleep(3)
img_url=(driver.find_element_by_css_selector(".n3VNCb").get_attribute("src"))
print(img_url)
urllib.request.urlretrieve(img_url,"result.jpg")




