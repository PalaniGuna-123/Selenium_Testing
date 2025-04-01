from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_clear_send_keys(driver, locator, keys, timeout=15):
    """Wait for an element to be visible, clear it, and send keys."""
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(keys)

class OrderCheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.EDIT_ADDRESS = (By.ID, "edit-address")
        self.QUANTITY = (By.XPATH, "//button[normalize-space()='+']")
        self.SHIPPING_FORM = {
            'Door No': (By.ID, "doorno"),
            'Street': (By.ID, "street"),
            'City': (By.ID, "city"),
            'Pincode': (By.ID, "pincode"),
            "State": (By.ID, "state")
        }
        self.CLICK_ADDRESS = (By.ID, "save-btn")

    def edit_address(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.EDIT_ADDRESS)).click()
        print("Edit Address button clicked successfully")

    def add_quantity(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.QUANTITY)).click()
        print("Add quantity successfully")

    def fill_address_form(self):
        try:
            wait_and_clear_send_keys(self.driver, self.SHIPPING_FORM['Door No'], "132/6")
            wait_and_clear_send_keys(self.driver, self.SHIPPING_FORM['Street'], "Road Street")
            wait_and_clear_send_keys(self.driver, self.SHIPPING_FORM['City'], "Chennai")
            wait_and_clear_send_keys(self.driver, self.SHIPPING_FORM['Pincode'], "600001")
            wait_and_clear_send_keys(self.driver, self.SHIPPING_FORM['State'], "Tamil Nadu")

            print("Shipping Form Filled Successfully")

        except Exception as e:
            print(f"Error filling shipping form: {e}")

    def click_save_address(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLICK_ADDRESS)).click()
            print("Save Address button clicked")

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())  
            alert = self.driver.switch_to.alert  
            print(f"Alert Message: {alert.text}") 
            alert.accept()  
            print("Popup Alert Accepted Successfully")

        except Exception as e:
            print(f"Error clicking Save Address: {e}")
