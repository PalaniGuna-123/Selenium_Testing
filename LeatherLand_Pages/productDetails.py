from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetails:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.CHANGE_IMAGE = (By.XPATH, "//img[@class='thumbnail active']")
        self.CHANGE_SIZE=(By.XPATH,"//button[contains(@class,'size-btn')]")
        self.CLICK_BUY_NOW=(By.XPATH,"//button[@class='btn buy-now']")

    def change_img_one(self):
        img_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHANGE_IMAGE))
        self.driver.execute_script("arguments[0].click();", img_element)
        print("Image 1 changed successfully")
    
    def change_size(self):
        self.driver.find_element(*self.CHANGE_SIZE).click()
        print("change size 10 correctly")
        self.driver.find_element(*self.CLICK_BUY_NOW).click()
        print("Buy now button clicked successfully")

