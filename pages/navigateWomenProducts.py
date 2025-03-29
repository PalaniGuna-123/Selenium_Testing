from selenium import webdriver
from selenium.webdriver.common.by import By

class WomenPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.WOMEN_MENU_ITEM = (By.XPATH, "//a[contains(text(),'Women')]")
        self.JACKETS_LINK = (By.XPATH, "//a[contains(text(),'Jackets')]")

    def go_to_jackets_page(self):
        self.driver.find_element(*self.WOMEN_MENU_ITEM).click()
        self.driver.find_element(*self.JACKETS_LINK).click()
        print("Navigated to Jackets Page.")
