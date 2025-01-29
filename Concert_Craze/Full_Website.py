from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Utility functions for reusable actions
def wait_and_click(driver, locator, timeout=15):
    """Wait for an element to be clickable and click."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()

def wait_and_send_keys(driver, locator, keys, timeout=15):
    """Wait for an element to be visible and send keys."""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    element.send_keys(keys)

def select_dropdown_option(driver, dropdown_locator, option_locator, timeout=15):
    """Select an option from a dropdown."""
    wait_and_click(driver, dropdown_locator)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(option_locator))
    wait_and_click(driver, option_locator)

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    url = 'https://concertcraze.netlify.app/'
    driver.get(url)
    driver.maximize_window()
    print("Step 1: Navigate to the concert website.")

    # Corrected: Pass locator as a tuple
    wait_and_click(driver, (By.XPATH, '//*[@id="hamburger"]')) 
    time.sleep(2)
    wait_and_click(driver, (By.XPATH, '//*[@id="loginLink"]'))  
    print("Step 2: Click the hamburger menu and go to the login page.")
    time.sleep(2)
    wait_and_send_keys(driver,(By.XPATH,'//*[@id="email"]'),"sridharsridhar34254@gmail.com")
    time.sleep(1)

    wait_and_send_keys(driver,(By.XPATH,'//*[@id="password"]'),"Guna@?2004")
    time.sleep(1)

    wait_and_click(driver,(By.XPATH,'//*[@id="login-form"]/button'))
    print("Step 3: Enter login credentials (email and password).")
    time.sleep(2)


    wait_and_click(driver,(By.XPATH,'//*[@id="searchBox"]'))
    time.sleep(2)
    print("Step 4: Search for 'Vijay Antony' in the search box and click the search button.")

    select_dropdown_option(driver,(By.XPATH,'//*[@id="genreFilter"]'),(By.XPATH,'//*[@id="genreFilter"]/option[2]'))
    time.sleep(2)
    select_dropdown_option(driver,(By.XPATH,'//*[@id="genreFilter"]/option[2]'),(By.XPATH,'//*[@id="genreFilter"]/option[3]'))
    time.sleep(2)
    select_dropdown_option(driver,(By.XPATH,'//*[@id="genreFilter"]/option[3]'),(By.XPATH,'//*[@id="genreFilter"]/option[4]'))
    time.sleep(2)
    select_dropdown_option(driver,(By.XPATH,'//*[@id="genreFilter"]/option[4]'),(By.XPATH,'//*[@id="genreFilter"]/option[1]'))
    time.sleep(3)
    print("Step 5: Select genre options from the dropdown multiple times.")
    wait_and_send_keys(driver,(By.XPATH,"//input[@id='searchBox']"),"Rockstar")
    
    wait_and_click(driver,(By.XPATH,"//button[@id='searchBtn']"))
    time.sleep(3)
    wait_and_click(driver,(By.XPATH,"//a[@class='btn btn-primary book-ticket']"))
    time.sleep(3)
    print("Step 6: Book a ticket by selecting ticket categories and adding tickets to the cart.")

    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    print("Step 7: Scroll down the page using JavaScript to view more content.")
    time.sleep(3)
    wait_and_click(driver,(By.CSS_SELECTOR,'#purchase'))
    time.sleep(2)
    select_dropdown_option(driver,(By.XPATH,"//select[@id='ticketCategory']"),(By.XPATH,'//*[@id="ticketCategory"]/option[2]'))
    time.sleep(1)
    select_dropdown_option(driver,(By.XPATH,'//*[@id="ticketCategory"]/option[2]'),(By.XPATH,'//*[@id="ticketCategory"]/option[3]'))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//button[@id='addTicket']"))
    time.sleep(1)
    element_to_right_click =wait_and_click(driver,(By.XPATH,"//button[@id='addTicket']"))

    actions = ActionChains(driver)


    actions.double_click(element_to_right_click).perform()
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//button[@id='removeTicket']"))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//button[@id='payNow']"))
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 500);")
    print("Scrolled down by 1000 pixels")
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//button[@id='confirmPayment']"))
    time.sleep(8)
    alert = driver.switch_to.alert


    print("Alert text:", alert.text)

    # Accept the alert (click OK)
    alert.accept()
    time.sleep(7)
    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='My Tickets']"))
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 400);")
    print("Scrolled down by 1000 pixels")
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='Explore']"))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//button[@id='viewBtn']"))
    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 2000 pixels")
    time.sleep(1)
    wait_and_send_keys(driver,(By.XPATH,"//input[@id='name']"),"GUNA VISION")
    wait_and_send_keys(driver,(By.XPATH,"//input[@id='email']"),"sridharsridhar34254@gmail.com")
    driver.execute_script("window.scrollBy(0, 500);")
    print("Scrolled down by 2000 pixels")
    print("Step 8: Enter user details in the form and submit.")
   

    wait_and_send_keys(driver,(By.XPATH,"//textarea[@id='message']"),"Innovative Music Composition: Vijay Antony is known for his ability to compose music that complements the mood and narrative of a film. His compositions often blend different genres, incorporating traditional Tamil sounds with modern elements, making his music stand out. He is known for his ability to create memorable melodies that resonate with audiences.")
    wait_and_click(driver,(By.XPATH,"//button[@id='footerSubBtn']"))
    time.sleep(4)
    driver.back()
    time.sleep(4)
    wait_and_click(driver,(By.XPATH,"//button[@id='hamburger']"))
    time.sleep(4)
    wait_and_click(driver,(By.XPATH,"//button[@id='popupLogoutButton']"))
    time.sleep(5)
    print("Step 9: Logout by clicking on the hamburger menu and the logout button.")



except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")


