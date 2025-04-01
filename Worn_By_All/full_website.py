from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

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
def wait_and_Clear_send_keys(driver, locator, keys, timeout=15):
    """Wait for an element to be visible and send keys."""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    element.clear()
    element.send_keys(keys)

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    url = 'https://wornbyall.netlify.app/'
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='Shop Now']"))
    time.sleep(3)
    
    driver.execute_script("window.scrollBy(0, 3000);")
    print("Scrolled down by 1000 pixels")
    time.sleep(4)
    driver.execute_script("window.scrollBy(0, -3000);")
    print("Scrolled up by 1000 pixels")
    time.sleep(4)
    driver.back()

    wait_and_click(driver,(By.XPATH,"//button[@id='loginSignupButton']"))
    time.sleep(1)
    # wait_and_click(driver,(By.XPATH,"//button[normalize-space()='Login']"))
    # time.sleep(1)
    wait_and_send_keys(driver,(By.XPATH,"//input[@id='signup-username']"),"Alex")
    wait_and_send_keys(driver,(By.XPATH,"//input[@id='signup-email']"),"guna1117734@gmail.com")
    time.sleep(1)

    wait_and_send_keys(driver,(By.XPATH,"//input[@id='signup-password']"),"Guna@?2004")
    time.sleep(1)
    wait_and_send_keys(driver,(By.XPATH,"//input[@id='signup-confirm-password']"),"Guna@?2004")

    wait_and_click(driver,(By.CSS_SELECTOR,"button[onclick='handleSignup()']"))
    time.sleep(2)
    # wait_and_click(driver,(By.XPATH,'//*[@id="popup-ok-button"]'))
    # time.sleep(3)

    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='Men']"))
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,"//body/main[@id='categories-container']/div[1]/button[1]"))
    time.sleep(2)
    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='searchBar']"),"pink")
    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='searchBar']"),"Gray")
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,"//body/div[@id='productGrid']/div[1]/button[1]"))

    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//body/div[@id='productGrid']/div[2]/button[1]"))

    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//a[@href='/pages/html/cartpage']//i[@class='fa-solid fa-cart-shopping']"))
    wait_and_click(driver,(By.XPATH,"//body/main/section[@id='cartItems']/div[2]/div[1]/button[1]"))
    time.sleep(3)
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")


