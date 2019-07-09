from selenium import webdriver
import time

# Old Link
#link = "http://suninjuly.github.io/registration1.html"
# New Link
link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link)

# Код, который заполняет обязательные поля
value = "/html/body/div/form/div[1]/div[1]/input"
element = browser.find_element_by_xpath(value)
element.send_keys("Мой ответ")

value = "/html/body/div/form/div[1]/div[2]/input"
element = browser.find_element_by_xpath(value)
element.send_keys("Мой ответ")

value = "/html/body/div/form/div[1]/div[3]/input"
element = browser.find_element_by_xpath(value)
element.send_keys("Мой ответ")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(5)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
