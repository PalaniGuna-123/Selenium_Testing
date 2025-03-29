from selenium import webdriver

class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def navigate_to_web(self, url='https://magento.softwaretestingboard.com/'):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Navigated to {url} and set window size.")
