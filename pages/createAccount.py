from selenium import webdriver
from selenium.webdriver.common.by import By

class CreateAccountPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.GO_TO_CREATE_ACCOUNT = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
        self.CREATE_FORM_SELECTOR = {
            'FirstName': (By.XPATH, "//input[@id='firstname']"),
            'LastName': (By.XPATH, "//input[@id='lastname']"),
            'emailId': (By.XPATH, "//input[@id='email_address']"),
            'password': (By.XPATH, '//*[@id="password"]'),
            'confirm_password': (By.XPATH, '//*[@id="password-confirmation"]'),
            'create_account': (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span')
        }

    def go_to_create_account(self):
        self.driver.find_element(*self.GO_TO_CREATE_ACCOUNT).click()

    def fill_create_account_form(self):
        self.driver.find_element(*self.CREATE_FORM_SELECTOR['FirstName']).send_keys("Guna")
        self.driver.find_element(*self.CREATE_FORM_SELECTOR['LastName']).send_keys("Vision")
        self.driver.find_element(*self.CREATE_FORM_SELECTOR['emailId']).send_keys("guna.dev@gmail.com")
        self.driver.find_element(*self.CREATE_FORM_SELECTOR['password']).send_keys("Guna@?2004")
        self.driver.find_element(*self.CREATE_FORM_SELECTOR['confirm_password']).send_keys("Guna@?2004")
        self.driver.find_element(*self.CREATE_FORM_SELECTOR['create_account']).click()
        print("Account created successfully!")
