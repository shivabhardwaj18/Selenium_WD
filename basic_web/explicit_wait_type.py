from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

from utilities.handy_wrappers import HandyWrappers

class ExplicitWaitType:

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def waitForElement(self, locator, locatorType, timeout=10, pollFrequency=1):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Waiting for maximum " + str(timeout) + " seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotInteractableException
                                 ])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("Element appeared on webpage")

        except:
            print("Element not appeared on webpage")

        return element
