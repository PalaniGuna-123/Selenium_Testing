from selenium import webdriver
from LeatherLand_Pages.home import homePage
from LeatherLand_Pages.logIn import LogInPage
from LeatherLand_Pages.trending import Trending
from LeatherLand_Pages.filter import FilterPage
from LeatherLand_Pages.productDetails import ProductDetails
from LeatherLand_Pages.check_Out_Page import OrderCheckOutPage
from pages.scrollControl import ScrollControl

if __name__ == "__main__":
    driver =webdriver.Chrome()
    try:
        Land_Home_Page =homePage(driver)
        Login_Page=LogInPage(driver)
        Trending_Page=Trending(driver)
        filterPage=FilterPage(driver)
        stock=ProductDetails(driver)
        order=OrderCheckOutPage(driver)
        scroll=ScrollControl(driver)

        Land_Home_Page.navigate_to_web()
        Login_Page.go_to_log_in_page()
        Login_Page.fill_log_in_page()

        Trending_Page.navigate_trending()
        Trending_Page.navigate_shoes()

        filterPage.filter_product()
        filterPage.click_product()

        stock.change_img_one()
        stock.change_size()

        order.add_quantity()
        scroll.scroll_by_1000px()
        order.edit_address()
        order.fill_address_form()
        order.click_save_address()


    except Exception as e:
        print(f"An error occurred : {e}")
    finally:
        driver.quit()
        print("Browser Closed")
