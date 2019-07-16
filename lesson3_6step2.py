import pytest
import time
import math

from selenium import webdriver

links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"
        ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

   # browser.find_element_by_class_name("textarea ember-auto-resize ember-view")


@pytest.mark.parametrize('pageLink', links)
def test_guest_should_see_login_link(browser, pageLink):

    browser.get(pageLink)

    element = browser.find_element_by_class_name('ember-auto-resize')
    element.send_keys(str(math.log(int(time.time()))))

    element = browser.find_element_by_class_name('submit-submission')
    element.click()

    element = browser.find_element_by_class_name('smart-hints__hint')
    value1 = element.text
    browser.implicitly_wait(10)
    time.sleep(5)

    if value1 != "Correct!":
        print(" ======= " + browser.find_element_by_class_name('smart-hints__hint').text)







