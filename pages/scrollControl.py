from selenium import webdriver
import time

class ScrollControl:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def scroll_by_1000px(self):
        if self.driver:
            time.sleep(2)  
            self.driver.execute_script("window.scrollBy(1000, 1000);")
            print('Scrolled down 10000px')
        else:
            print("Driver is undefined. Cannot scroll.")