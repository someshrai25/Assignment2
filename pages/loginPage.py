from selenium.webdriver.common.by import By
import datetime
import os
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    #Locators
    username = "//input[@name='username']"
    password = "//input[@name='password']"
    login_btn = "//button[@type='submit']"


    def enterUsername(self, username):
        self.driver.find_element(By.XPATH, self.username).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def clickCTA(self):
        self.driver.find_element(By.XPATH, self.login_btn).click()

    def login(self, username="", password=""):
        time.sleep(2)
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickCTA()
        time.sleep(5)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_name = os.path.join("C:\\Users\\somesh.rai_infobeans\\PycharmProjects\\Assignment2\\screenshot",
                                   f"screenshot_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")


