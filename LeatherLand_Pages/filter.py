from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.FILTER_OPTION = (By.XPATH, "//i[@class='bx bx-filter-alt filter-icon']")
        self.FILTER = (By.XPATH, "//div[@class='ascending-order']")
        self.CLICK_PRODUCT = (By.XPATH,"//a[normalize-space()='School Shoes Girls 5yr Black']")

    def filter_product(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FILTER_OPTION)).click()
        print("Choose Filter option")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FILTER)).click()
        print("Filter option clicked successfully")

    def click_product(self):
        product = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLICK_PRODUCT))
        product.click()
        print("Product clicked successfully")
