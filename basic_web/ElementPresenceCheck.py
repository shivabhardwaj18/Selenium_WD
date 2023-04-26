from selenium import webdriver

from utilities.handy_wrappers import HandyWrappers


class ElementPresenceCheck:

    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        hw = HandyWrappers(driver)

        result = hw.isElementPresent("name")

        print(str(result))


cc = ElementPresenceCheck()
cc.test()