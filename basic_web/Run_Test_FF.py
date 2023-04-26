import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service

class RunFFTests():

    def test(self):
        driver = webdriver.Chrome()
        # Open provided URL
        driver.get("https://www.letskodeit.com")
        time.sleep(5)


run_tests = RunFFTests()
run_tests.test()