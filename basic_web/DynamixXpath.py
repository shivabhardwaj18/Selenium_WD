import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login -> Lecture "How to click and type on a web element"
        driver.find_element(By.LINK_TEXT, "SIGN IN").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("shivabhardwaj.ca@gmail.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("!Code12345")
        driver.find_element(By.ID, "login").click()
        time.sleep(2)

        # Search for courses -> You don't need to search the course
        # You can select it without searching also
        driver.find_element(By.XPATH, '//a[contains(text(),"ALL COURSES")]').click()
        time.sleep(2)


        _course = "//div[contains(@class, 'zen-course-title')]//h4[contains(text(), '{0}') ]"
        _js_course = _course.format("Complete Test Automation Bundle")

        courseElement = driver.find_element(By.XPATH, _js_course)
        courseElement.click()
        time.sleep(5)

ff = DynamicXPathFormat()
ff.test()