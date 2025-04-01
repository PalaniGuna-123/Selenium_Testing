from selenium import webdriver

class homePage:
    def __init__(self,driver:webdriver.Chrome):
        self.driver =driver

    def navigate_to_web(self,url="http://leatherland.netlify.app/"):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"navigated to {url} and set window size correctly.")