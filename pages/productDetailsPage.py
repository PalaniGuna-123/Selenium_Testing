from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductDetailsPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ADD_TO_CART_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#product-addtocart-button')
        self.MINICART_WRAPPER_SELECTOR = (By.CSS_SELECTOR, '.minicart-wrapper')
        self.MINICART_ITEM_SELECTOR = (By.CSS_SELECTOR, '.minicart-items .product-item')

    def add_to_product_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON_SELECTOR).click()
        self.driver.implicitly_wait(3)
        print("Product added to cart.")

    def verify_product_cart(self):
        self.driver.find_element(*self.MINICART_WRAPPER_SELECTOR).click()
        print("Product verified in cart.")
        return self.driver.find_element(*self.MINICART_ITEM_SELECTOR)
