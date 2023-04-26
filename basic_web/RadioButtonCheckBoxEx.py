import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class RadioButtonAndCheckbox:

    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        bmwRadioButton = driver.find_element(By.ID, "bmwradio")
        bmwRadioButton.click()

        time.sleep(2)
        benzRadioButton = driver.find_element(By.ID, "benzradio")
        benzRadioButton.click()

        time.sleep(2)
        bmwCheckbox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)
        benzCheckbox = driver.find_element(By.ID, "benzcheck")
        benzCheckbox.click()

        print("BMW Radio button selected: " + str(bmwRadioButton.is_selected()))
        print("Benz Radio button selected: " + str(benzRadioButton.is_selected()))
        print("BMW Checkbox selected: " + str(bmwCheckbox.is_selected()))
        print("Benz checkbox selected: " + str(benzCheckbox.is_selected()))

cc = RadioButtonAndCheckbox()
cc.test()

