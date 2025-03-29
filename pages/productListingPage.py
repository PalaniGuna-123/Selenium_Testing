from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductListingPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.FIRST_PRODUCT_SELECTOR = (By.XPATH, '//img[@alt="Voyage Yoga Bag"]')

    def select_first_product(self):
        try:
            first_product = self.driver.find_element(*self.FIRST_PRODUCT_SELECTOR)
            first_product.click()
            print("First product selected.")
        except Exception as e:
            print(f"Error: {e}")
            raise Exception("First product not found!")
