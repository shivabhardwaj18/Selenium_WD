import time

from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers


class Using_Wrappers:

    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(3)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()
        time.sleep(2)
cc = Using_Wrappers()
cc.test()
