from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.SEARCH_INPUT_SELECTOR = (By.CSS_SELECTOR, '#search')
        self.SEARCH_RESULTS_SELECTOR = (By.CSS_SELECTOR, '.product-item')

    def search_product(self, search_term):
        self.driver.find_element(*self.SEARCH_INPUT_SELECTOR).send_keys(search_term)
        self.driver.find_element(*self.SEARCH_INPUT_SELECTOR).submit()
        self.driver.implicitly_wait(10)
        print("Search completed for:", search_term)

        results = self.driver.find_elements(*self.SEARCH_RESULTS_SELECTOR)
        if results:
            print(f"{len(results)} results found.")
        else:
            print("No results found.")
