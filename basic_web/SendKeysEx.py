import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ClickAndSendKeys:

    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//*[@id='navbar-inverse-collapse']/div/div/a")
        loginLink.click()

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")

cc = ClickAndSendKeys()
cc.test()
