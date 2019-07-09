import time
import math

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

# open link http://suninjuly.github.io/math.html.
browser = webdriver.Chrome()
browser.get(link)

# find value x in text
x_find = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_find.text

# calculate function with value x
x_el = calc(x)

# enter value of the function cal with x = x_el to text field
value = "//*[@id='answer']"
element = browser.find_element_by_xpath(value)
element.send_keys(x_el)

# mark checkbox
checkbox = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
checkbox.click()

# case radiobutton
radiobutton = browser.find_element_by_xpath("//*[@id='robotsRule']")
radiobutton.click()

time.sleep(3)

# click button Send
send = browser.find_element_by_css_selector("body > div > form > button")
send.click()

'''
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    browser.find_element_by_css_selector(selector).click()
'''