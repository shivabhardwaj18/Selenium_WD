from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element(By.XPATH, "//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a").click()
        # Find departing field
        departingField = driver.find_element(By.ID, "d1-btn")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        dateToSelect = driver.find_element(By.XPATH,
                                           "((//div[@class='uitk-date-picker-month'])[2]//button[text()='30']")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "http://www.expedia.ca"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        #time.sleep(3)
        #driver.find_element(By.ID, "close").click()


        # Click flights tab
        driver.find_element(By.XPATH, "//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a").click()
        # Click departing field
        departingField = driver.find_element(By.ID, "d1-btn")
        departingField.click()
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        calMonth = driver.find_element(By.XPATH, "(//div[@class='uitk-date-picker-month'])[1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")




        for date in allValidDates:
            if date.get_attribute("data-day") == "24":
                date.click()
                time.sleep(20)
                break


ff = CalendarSelection()
ff.test2()