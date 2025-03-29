from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//span[@class='counter-number']")
        self.PROCEED = (By.XPATH, "//button[@id='top-cart-btn-checkout']")
        self.FLAT_RATE_SHIPPING_METHOD = (By.CSS_SELECTOR, '#label_method_flatrate_flatrate')
        self.GO_TO_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.button.action.continue.primary')
        self.SHIPPING_FORM_SELECTOR = {
            'email': (By.XPATH, "//div[@class='control _with-tooltip']//input[@id='customer-email']"),
            'firstName': (By.CSS_SELECTOR, 'input[name="firstname"]'),
            'lastName': (By.CSS_SELECTOR, 'input[name="lastname"]'),
            'company': (By.CSS_SELECTOR, 'input[name="company"]'),
            'street': (By.CSS_SELECTOR, 'input[name="street[0]"]'),
            'country': (By.CSS_SELECTOR, 'select[name="country_id"]'),
            'region': (By.CSS_SELECTOR, 'select[name="region_id"]'),
            'city': (By.CSS_SELECTOR, 'input[name="city"]'),
            'postCode': (By.CSS_SELECTOR, 'input[name="postcode"]'),
            'telephone': (By.CSS_SELECTOR, 'input[name="telephone"]')
        }
        self.PLACE_ORDER_BUTTON = (By.XPATH, "//span[normalize-space()='Place Order']")
        self.CHECKOUT_SUCCESS_BLOCK = (By.CSS_SELECTOR, '.checkout-success')

    def proceed(self):
        self.driver.find_element(*self.PROCEED).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON).click()

    def fill_shipping_form(self):
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['email']).send_keys("guna.dev@gmail.com")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['firstName']).send_keys("Guna")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['lastName']).send_keys("Vision")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['company']).send_keys("Any Company")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['street']).send_keys("1234 Elm St")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['country']).click()
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['city']).send_keys("Springfield")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['postCode']).send_keys("12345")
        self.driver.find_element(*self.SHIPPING_FORM_SELECTOR['telephone']).send_keys("123-456-789")

    def select_flat_rate_shipping_method(self):
        self.driver.find_element(*self.FLAT_RATE_SHIPPING_METHOD).click()

    def proceed_to_payment_step(self):
        self.driver.find_element(*self.GO_TO_NEXT_STEP_BUTTON).click()

    def place_order(self):
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()

    def is_checkout_success(self):
        return self.driver.find_element(*self.CHECKOUT_SUCCESS_BLOCK)
