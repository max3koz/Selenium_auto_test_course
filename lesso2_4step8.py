import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.implicitly_wait(15)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
cost = WebDriverWait(browser, 15).\
        until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book"))).click()

# find value x in text
x_find = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_find.text

# calculate function with value x
x_el = calc(x)

# enter value of the function cal with x = x_el to text field
value = "//*[@id='answer']"
browser.find_element_by_xpath(value).send_keys(x_el)

# click button Send
browser.find_element_by_xpath("//*[@id='solve']").click()
