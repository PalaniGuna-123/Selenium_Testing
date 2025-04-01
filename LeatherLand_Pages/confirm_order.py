from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmOrder:
    def __init__(self,driver):
        self.driver=driver
        self.CONFIRM_ORDER=(By.ID,"proceed-to-payment")
    def proceed_to_payment(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CONFIRM_ORDER)).click()
        print("proceed to payment successfully")
    