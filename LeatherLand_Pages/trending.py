from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Trending:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver 
        self.TRENDING = (By.LINK_TEXT, "Trending")
        self.NAVIGATE_SHOES = (By.LINK_TEXT, "View all")

    def navigate_trending(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TRENDING)).click()
        print("navigated trending page")
    
    def navigate_shoes(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NAVIGATE_SHOES)).click()
        print("navigated shoes page successfully")
