import time

from selenium import webdriver
from basic_web.explicit_wait_type import ExplicitWaitType


class ExplicitDemo2:

    def test(self):
        baseURL = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)


        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="//a[text()='Sign In']", locatorType="xpath")

        element.click()

        time.sleep(2)

cc = ExplicitDemo2()
cc.test()