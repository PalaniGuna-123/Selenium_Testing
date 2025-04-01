from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LogInPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.CLICK_SIGN_IN = (By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
        self.FIELD_SIGN_IN = (By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
        self.FILL_LOGIN_FORM = {
            'LogInEmail': (By.XPATH, "//input[@id='email']"),
            'Password': (By.XPATH, "//fieldset[@class='fieldset login']//input[@id='pass']")
        }

    def click_sign_in(self):
        self.driver.find_element(*self.CLICK_SIGN_IN).click()

    def fill_login_form(self):
        self.driver.find_element(*self.FILL_LOGIN_FORM['LogInEmail']).send_keys("guna.dev@gmail.com")
        self.driver.find_element(*self.FILL_LOGIN_FORM['Password']).send_keys("Guna@?2004")

    def field_sign_in(self):
        self.driver.find_element(*self.FIELD_SIGN_IN).click()
        time.sleep(4)
        print("Sign In successful.")
