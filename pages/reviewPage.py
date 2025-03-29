from selenium import webdriver
from selenium.webdriver.common.by import By

class ReviewPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.MORE_DETAILS = (By.XPATH, "//a[@id='tab-label-additional-title']")
        self.REVIEW_PAGE = (By.XPATH, "//a[@id='tab-label-reviews-title']")
        self.REVIEW_FORM = {
            'rating': (By.CSS_SELECTOR, '#Rating_3_label'),
            'nick': (By.XPATH, "//input[@id='nickname_field']"),
            'summary': (By.XPATH, "//input[@id='summary_field']"),
            'review': (By.XPATH, "//textarea[@id='review_field']")
        }
        self.REVIEW_SUBMIT = (By.XPATH, "//span[normalize-space()='Submit Review']")
        self.WISH_LIST = (By.XPATH, "//div[@class='product-addto-links']//span[contains(text(),'Add to Wish List')]")

    def review_details(self):
        self.driver.find_element(*self.MORE_DETAILS).click()
        self.driver.find_element(*self.REVIEW_PAGE).click()

    def fill_review_form(self):
        self.driver.find_element(*self.REVIEW_FORM['nick']).send_keys("Devil")
        self.driver.find_element(*self.REVIEW_FORM['summary']).send_keys("Comfortable and Warm")
        self.driver.find_element(*self.REVIEW_FORM['review']).send_keys(
            "This jacket is super cozy and warm. I love wearing it on cold days, especially when I'm outdoors. The material feels soft and it keeps me warm without being too bulky. The only downside is that the sleeves are a bit too long for me. Other than that, it’s a great purchase!"
        )
        self.driver.find_element(*self.WISH_LIST).click()
        self.driver.back()

        print("Review form submitted and added to Wish List.")
