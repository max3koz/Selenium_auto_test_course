import time
import math

# connect webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize the browser driver
browser = webdriver.Chrome()

# sleep
time.sleep(2)

# create link
link = "http://suninjuly.github.io/find_link_text"

# open site by link
browser.get(link)

# count link number
link_number = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(link_number)

# get to link
#link_new = "http://suninjuly.github.io/find_link_text_redirect13.html"
link_new = browser.find_element_by_link_text(link_number)
print(link_new)
link_new.click()

# find elevent by css selector and enter information in fields
value1 = "first_name"
value2 = "last_name"
value3 = "form-control.city"
value4 = "country"

input1 = browser.find_element_by_name(value1)
input1.send_keys("Ivan")
input2 = browser.find_element_by_name(value2)
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name(value3)
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id(value4)
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()

