import time

# connect webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

# initialize the browser driver
browser = webdriver.Chrome()

# sleep
time.sleep(2)

# open site by link
browser.get(link)

value1 = "first_name"
value2 = "last_name"
value3 = "form-control.city"
value4 = "country"

# find elevent by css selector and enter information in fields
input1 = browser.find_element_by_name(value1)
input1.send_keys("Ivan")
input2 = browser.find_element_by_name(value2)
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name(value3)
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id(value4)
input4.send_keys("Russia")
button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
button.click()