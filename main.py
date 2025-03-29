from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.homePage import HomePage
from pages.searchPage import SearchPage
from pages.productListingPage import ProductListingPage
from pages.productDetailsPage import ProductDetailsPage
from pages.checkOutPage import CheckoutPage
from pages.logInPage import LogInPage
from pages.navigateWomenProducts import WomenPage
from pages.jacketPageDropdown import JacketPage
from pages.cartPage import CartPage
from pages.scrollControl import ScrollControl
from pages.reviewPage import ReviewPage

SEARCH_TERM = "bag"

if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        home_page = HomePage(driver)
        search_page = SearchPage(driver)
        product_listing_page = ProductListingPage(driver)
        product_details_page = ProductDetailsPage(driver)
        checkout_page = CheckoutPage(driver)
        login_page = LogInPage(driver)
        navigate_women_page = WomenPage(driver)
        jacket_page = JacketPage(driver)
        cart_page = CartPage(driver)
        scroll = ScrollControl(driver)
        review = ReviewPage(driver)

        # Perform actions
        home_page.navigate_to_web()
        search_page.search_product(SEARCH_TERM)
        product_listing_page.select_first_product()
        product_details_page.add_to_product_cart()
        product_details_page.verify_product_cart()
        checkout_page.proceed_to_checkout()
        checkout_page.proceed()
        checkout_page.fill_shipping_form()
        checkout_page.select_flat_rate_shipping_method()
        checkout_page.proceed_to_payment_step()
        checkout_page.place_order()
        login_page.click_sign_in()
        login_page.fill_login_form()
        login_page.field_sign_in()

        # Navigate to Women's Jackets Page
        navigate_women_page.go_to_jackets_page()
        jacket_page.select_option_from_dropdown()
        cart_page.add_all_items_to_cart()
        scroll.scroll_by_1000px()
        review.review_details()
        review.fill_review_form()
        print("Test completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")
