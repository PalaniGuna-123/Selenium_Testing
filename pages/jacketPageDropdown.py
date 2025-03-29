from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class JacketPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.DROPDOWN = (By.XPATH, "//div[@class='page-wrapper']//div[2]//div[3]//select[1]")

    def select_option_from_dropdown(self):
        dropdown_element = self.driver.find_element(*self.DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_index(2)
        print("Option with index 2 selected from dropdown.")
