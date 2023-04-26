import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownSelect:

    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Selected Benz using value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Selected Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Selected BMW using visible text")
        time.sleep(2)


cc = DropDownSelect()
cc.test()

