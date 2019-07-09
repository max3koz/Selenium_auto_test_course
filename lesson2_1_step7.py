import time
import math

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

# open link http://suninjuly.github.io/math.html.
browser = webdriver.Chrome()
browser.get(link)

# find picture with Box
x_find = browser.find_element_by_xpath("//*[@id='treasure']")
number_x = x_find.get_attribute('valuex')
print(number_x)

# calculete x with function calc
x = calc(number_x)

# enter value of the function cal with x = x_el to text field
value = "//*[@id='answer']"
element = browser.find_element_by_xpath(value)
element.send_keys(x)

# mark checkbox
checkbox = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
checkbox.click()

# case radiobutton
radiobutton = browser.find_element_by_xpath("//*[@id='robotsRule']")
radiobutton.click()

time.sleep(3)

# click button Send
send = browser.find_element_by_css_selector("body > div > form > div > div > button")
send.click()