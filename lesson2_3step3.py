import time
import math

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

# open link
browser = webdriver.Chrome()
browser.get(link)

# find picture with Box
button_alert = browser.find_element_by_xpath("/html/body/form/div/div/button")
button_alert.click()

alert = browser.switch_to.alert
alert.accept()

# find value x in text
x_find = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_find.text

# calculete x with function calc
x = calc(x)

# enter value of the function cal with x = x_el to text field
value = "//*[@id='answer']"
element = browser.find_element_by_xpath(value)
element.send_keys(x)

# click button Send
send = browser.find_element_by_xpath("/html/body/form/div/div/button")
send.click()