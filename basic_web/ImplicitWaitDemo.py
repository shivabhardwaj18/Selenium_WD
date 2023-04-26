import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ImplicitWait():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login -> Lecture "How to click and type on a web element"
        driver.find_element(By.LINK_TEXT, "SIGN IN").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("Shivaaaa")
        password = driver.find_element(By.ID, "password")
        password.send_keys("!Code12345")

cc = ImplicitWait()
cc.test()