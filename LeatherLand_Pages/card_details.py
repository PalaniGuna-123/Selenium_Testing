from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_and_clear_send_keys(driver, locator, keys, timeout=15):
    """Wait for an element to be visible, clear it, and send keys."""
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(keys)

class CardDetails:
    def __init__(self,driver):
        self.driver=driver
        self.CLICK_CARD=(By.XPATH,"//label[@for='card']")
        self.CARD_FORM={
            'name':(By.ID,"cardholder-name"),
            'number':(By.ID,"card-number"),
            'Expiry Date':(By.ID,"expiry-date"),
            'CVV':(By.ID,"cvv")
        }
        self.PAY_NOW=(By.XPATH,"//button[@id='proceed-to-payment']")
        self.TRACK_ORDER=(By.XPATH,"//button[@class='button track-order']")

    def click_card(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CLICK_CARD)).click()
        print("click debit card option")
    
    def fill_card_details(self):
       wait_and_clear_send_keys(self.driver,self.CARD_FORM['name'],"Guna Palani")
       wait_and_clear_send_keys(self.driver,self.CARD_FORM['number'],"1234 5678 9101 1213")
       wait_and_clear_send_keys(self.driver,self.CARD_FORM['Expiry Date'],"08/29")
       wait_and_clear_send_keys(self.driver,self.CARD_FORM['CVV'],"754")
       print("finished card credentials")
    
    def proceed_to_pay(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.PAY_NOW)).click()
        print("proceed to pay the debit card details")
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.TRACK_ORDER)).click()
        print("Track Order successfully")



        