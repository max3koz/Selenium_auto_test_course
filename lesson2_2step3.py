import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(a, b):
  return str(a + b)

link = "http://suninjuly.github.io/selects1.html"

# open link http://suninjuly.github.io/math.html.
browser = webdriver.Chrome()
browser.get(link)

# find numbers for calculate sum
find_a = browser.find_element_by_xpath('//*[@id="num1"]')
a = find_a.text
find_b = browser.find_element_by_xpath('//*[@id="num2"]')
b = find_b.text

# summ of numbers a and b
sum = str(int(a) + int(b))

# find in the dropdown list by the value sum
# 1 varint
#select = Select(browser.find_element_by_class_name("custom-select"))
#select.select_by_value(sum)

# 2 variant
browser.find_element_by_id("dropdown").click()
browser.find_element_by_css_selector("[value='" + sum + "']").click()

# click button Send
send = browser.find_element_by_css_selector("body > div > form > button")
send.click()

