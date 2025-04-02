from selenium import webdriver
from LeatherLand_Pages.home import homePage
from LeatherLand_Pages.logIn import LogInPage
from LeatherLand_Pages.trending import Trending
from LeatherLand_Pages.filter import FilterPage
from LeatherLand_Pages.productDetails import ProductDetails
from LeatherLand_Pages.check_Out_Page import OrderCheckOutPage
from pages.scrollControl import ScrollControl
from LeatherLand_Pages.cash_On_Delivery import cashOnDelivery
from LeatherLand_Pages.confirm_order import ConfirmOrder
from LeatherLand_Pages.go_home import GoHome
from LeatherLand_Pages.card_details import CardDetails

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
        cash_method=cashOnDelivery(driver)
        order_confirm=ConfirmOrder(driver)
        Go_to_My_Home=GoHome(driver)
        card_details=CardDetails(driver)

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

        # cash_method.click_cash_on_delivery()
        # order_confirm.proceed_to_payment()
        card_details.click_card()
        card_details.fill_card_details()
        scroll.scroll_by_1000px()
        card_details.proceed_to_pay()
        # Go_to_My_Home.go_home()


    except Exception as e:
        print(f"An error occurred : {e}")
    finally:
        driver.quit()
        print("Browser Closed")
