import math
import os

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# Код, который заполняет обязательные поля
value = "/html/body/div/form/div/input[1]"
element = browser.find_element_by_xpath(value)
element.send_keys("Иван")

value = "/html/body/div/form/div/input[2]"
element = browser.find_element_by_xpath(value)
element.send_keys("Иванов")

value = "/html/body/div/form/div/input[3]"
element = browser.find_element_by_xpath(value)
element.send_keys("Иван@Иванов")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "get_karatetora.txt")
element = browser.find_element_by_xpath("//*[@id='file']")
element.send_keys(file_path)

# click button Send
send = browser.find_element_by_css_selector("body > div > form > button")
send.click()