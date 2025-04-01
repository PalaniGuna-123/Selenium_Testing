from selenium import webdriver
import time

class ScrollControl:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def scroll_by_1000px(self):
        if self.driver:
            time.sleep(2)  
            self.driver.execute_script("window.scrollBy(0, 1000);")
            print('Scrolled down 1000px')
        else:
            print("Driver is undefined. Cannot scroll.")