from selenium import webdriver
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ITEMS_XPATH = (By.XPATH, "//img[@alt='Ingrid Running Jacket']")
        self.CHANGE_IMAGE = (By.XPATH, "//div[@aria-label='Next']//div[@class='fotorama__arr__arr']")
        self.SIZE_XPATH_BASE = "//div[@id='option-label-size-143-item-"
        self.COLOR_XPATH_BASE = "//div[@id='option-label-color-93-item-"
        self.QUANTITY = (By.XPATH, "//input[@id='qty']")
        self.ADD_TO_COMPARE = (By.XPATH, "//div[@class='product-addto-links']//span[contains(text(),'Add to Compare')]")

    def change_image_multiple_times(self, times=4):
        for i in range(times):
            self.driver.find_element(*self.CHANGE_IMAGE).click()
            print(f"Changed image {i + 1} times.")

    def select_size(self, size_id):
        size_xpath = (By.XPATH, f"{self.SIZE_XPATH_BASE}{size_id}']")
        self.driver.find_element(*size_xpath).click()
        print(f"Selected size with ID: {size_id}")

    def select_multiple_sizes(self):
        sizes = [166, 167, 168, 169, 170]
        for size_id in sizes:
            self.select_size(size_id)

    def select_color(self, color_id):
        color_xpath = (By.XPATH, f"{self.COLOR_XPATH_BASE}{color_id}']")
        self.driver.find_element(*color_xpath).click()
        print(f"Selected color with ID: {color_id}")

    def select_multiple_colors(self):
        colors = [56, 58, 59]
        for color_id in colors:
            self.select_color(color_id)

    def add_all_items_to_cart(self):
        self.driver.find_element(*self.ITEMS_XPATH).click()
        self.change_image_multiple_times()
        self.select_multiple_sizes()
        self.select_multiple_colors()
        self.driver.find_element(*self.QUANTITY).clear()
        self.driver.find_element(*self.QUANTITY).send_keys('11')
        self.driver.find_element(*self.ADD_TO_COMPARE).click()
        print("Added all items to compare.")
