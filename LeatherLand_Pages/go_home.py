from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoHome:
    def __init__(self,driver):
        self.driver=driver
        self.GO_HOME=(By.XPATH,"//button[@class='button go-home']")

    def go_home(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.GO_HOME)).click()
        print("Go to home")

