import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class GetText:
    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "openwindow")
        print("Text is " + element.text)
        class_attribute = element.get_attribute("class")
        print("Class attribute is " + class_attribute)

cc = GetText()
cc.test()
