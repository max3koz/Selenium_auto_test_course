import math
import time

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# find numbers for calculate sum
number = browser.find_element_by_xpath('//*[@id="input_value"]').text
print(number)

# calulate numer x
rez = calc(int(number))

# scroll page and add resault
button = browser.find_element_by_id("answer")
button.send_keys(rez)

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# mark checkbox
checkbox = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
checkbox.click()

# case radiobutton
radiobutton = browser.find_element_by_xpath("//*[@id='robotsRule']")
radiobutton.click()

# click button Send
send = browser.find_element_by_css_selector("body > div > form > button")
send.click()