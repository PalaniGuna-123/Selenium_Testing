from selenium import webdriver
from selenium.webdriver.common.by import By

class LogInPage:
    def __init__(self,driver: webdriver.Chrome):
        self.driver=driver
        self.GO_TO_LOGIN_PAGE =(By.XPATH,"//a[@id='signIn']")
        self.LOG_IN_CREDENTIALS={
            'email' : (By.XPATH,"//input[@id='username']"),
            'password':(By.ID,"password")
        }
        self.CLICK_LOG_IN=(By.ID,"signInButton")

    def go_to_log_in_page(self):
        self.driver.find_element(*self.GO_TO_LOGIN_PAGE).click()
    
    def fill_log_in_page(self):
        self.driver.find_element(*self.LOG_IN_CREDENTIALS['email']).send_keys("kani@gmail.com")
        self.driver.find_element(*self.LOG_IN_CREDENTIALS['password']).send_keys("Kani@?2003")
        self.driver.find_element(*self.CLICK_LOG_IN).click()
        print("Log in successfully")