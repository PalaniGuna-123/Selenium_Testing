from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class cashOnDelivery:
    def __init__(self,driver):
        self.driver=driver
        self.CASH_ON_DELIVERY=(By.XPATH,"//span[normalize-space()='Cash on delivery']")
    
    def click_cash_on_delivery(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CASH_ON_DELIVERY)).click()
        print("clicked Cash On delivery option successful")