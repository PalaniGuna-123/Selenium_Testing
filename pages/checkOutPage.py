from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//span[@class='counter-number']")
        self.PROCEED = (By.XPATH, "//button[@id='top-cart-btn-checkout']")
        self.FLAT_RATE_SHIPPING_METHOD = (By.XPATH, "//input[@name='ko_unique_1']")
        self.GO_TO_NEXT_STEP_BUTTON = (By.XPATH, "//span[normalize-space()='Next']")
        self.SHIPPING_FORM_SELECTOR = {
            'email': (By.XPATH, "//div[@class='control _with-tooltip']//input[@id='customer-email']"),
            'firstName': (By.NAME, 'firstname'),
            'lastName': (By.NAME, 'lastname'),
            'company': (By.NAME, 'company'),
            'street': (By.NAME, 'street[0]'),
            'country': (By.NAME, 'country_id'),
            'region': (By.NAME, 'region_id'),
            'city': (By.NAME, 'city'),
            'postCode': (By.NAME, 'postcode'),
            'telephone': (By.NAME, 'telephone')
        }
        self.PLACE_ORDER_BUTTON = (By.XPATH, "//span[normalize-space()='Place Order']")
        self.CHECKOUT_SUCCESS_BLOCK = (By.CSS_SELECTOR, '.checkout-success')

    def proceed(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PROCEED)).click()

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PROCEED_TO_CHECKOUT_BUTTON)).click()

    def fill_shipping_form(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['email'])).send_keys("guna.dev@gmail.com")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['firstName'])).send_keys("Guna")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['lastName'])).send_keys("Vision")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['company'])).send_keys("Any Company")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['street'])).send_keys("1234 Elm St")

            # Select country from dropdown using Select
            country_dropdown = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SHIPPING_FORM_SELECTOR['country'])))
            country_dropdown.select_by_index(1)

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['city'])).send_keys("Springfield")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['postCode'])).send_keys("12345")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SHIPPING_FORM_SELECTOR['telephone'])).send_keys("123-456-789")
            print("Shipping Form Filled Successfully")
        except Exception as e:
            print(f"Error filling shipping form: {e}")

    def select_flat_rate_shipping_method(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FLAT_RATE_SHIPPING_METHOD)).click()
            print("Flat Rate Shipping Method Selected")
        except Exception as e:
            print(f"Error selecting shipping method: {e}")

    def proceed_to_payment_step(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.GO_TO_NEXT_STEP_BUTTON)).click()
            print("Proceeded to Payment Step")
        except Exception as e:
            print(f"Error proceeding to payment step: {e}")

    def place_order(self):
        try:
            place_order_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLACE_ORDER_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", place_order_button)
            time.sleep(1)  # Small delay to ensure visibility
            self.driver.execute_script("arguments[0].click();", place_order_button)
            print("Order Placed Successfully")
        except Exception as e:
            print(f"Error placing order: {e}")

    def is_checkout_success(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CHECKOUT_SUCCESS_BLOCK))
        except Exception as e:
            print(f"Error verifying checkout success: {e}")
            return False
