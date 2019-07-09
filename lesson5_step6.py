import time

# connect webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize the browser driver
browser = webdriver.Chrome()

# sleep
time.sleep(2)

# create link
link = "http://suninjuly.github.io/huge_form.html"

# open site by link
browser.get(link)

# find elements by value
value = "/html/body/div/form/div[1]/input"
elements = browser.find_elements_by_xpath(value)
print(elements)

# filling the form
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_xpath("/html/body/div/form/button")
button.click()


