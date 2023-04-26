
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC


class ExplicitDemo1:

    def test(self):
        baseURL = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.execute_script("window.location='https://courses.letskodeit.com/';")

        #driver.find_element(By.XPATH, "//a[text()='Sign in']").click()

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
        ])

        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sign In']")))
        element.click()

        #time.sleep(2)
        driver.quit()

cc = ExplicitDemo1()
cc.test()