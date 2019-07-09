import time
import math

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

# open link
browser = webdriver.Chrome()
browser.get(link)

# find picture with Box
button = browser.find_element_by_xpath("/html/body/form/div/div/button")
button.click()

# get to next window
window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

# find value x in text
x_find = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_find.text

# calculete x with function calc
x = calc(x)

# enter value of the function cal with x to text field
value = "//*[@id='answer']"
element = browser.find_element_by_xpath(value)
element.send_keys(x)

# click button Send
send = browser.find_element_by_xpath("/html/body/form/div/div/button")
send.click()