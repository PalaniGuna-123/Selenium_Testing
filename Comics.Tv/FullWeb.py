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
def wait_and_Clear_send_keys(driver, locator, keys, timeout=15):
    """Wait for an element to be visible and send keys."""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    element.clear()
    element.send_keys(keys)

def select_dropdown_option(driver, dropdown_locator, option_locator, timeout=15):
    """Select an option from a dropdown."""
    wait_and_click(driver, dropdown_locator)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(option_locator))
    wait_and_click(driver, option_locator)

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    url = 'http://localhost:4000'
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    element_to_hover = driver.find_element(By.XPATH, "//input[@id='search-bar']")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    print("step 1: search bar hovered successfully")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    wait_and_click(driver,(By.XPATH,"//div[10]//button[1]"))
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))
    print("step 2: click watch list")

    time.sleep(2)
    driver.execute_script("window.scrollBy(0, -2000);")
    print("Scrolled up by 1000 pixels")
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,"//div[2]//button[1]"))
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))


    wait_and_click(driver,(By.XPATH,"//span[normalize-space()='Avengers Infinity War']"))
    time.sleep(2)

    element_to_hover = driver.find_element(By.XPATH, "//a[@class='watch-now-btn']")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(3)
    wait_and_click(driver,(By.XPATH,"//a[@class='watch-now-btn']"))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(35)
    wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(2)

    driver.back()
    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='WATCHLIST']"))
    time.sleep(9)
    wait_and_click(driver,(By.XPATH,"//div[@id='movie-2']//button[@class='remove-from-watchlist-btn'][normalize-space()='Remove']"))
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]'))
    wait_and_click(driver,(By.XPATH,"//div[@id='movie-10']//button[@class='remove-from-watchlist-btn'][normalize-space()='Remove']"))
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]'))
    time.sleep(2)

    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='HOME']"))
    time.sleep(3)
    # wait_and_click(driver,(By.XPATH,"//div[@class='movie-gallery']//div[1]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[2]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[3]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[4]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[5]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[6]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[7]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[8]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[9]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[10]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[11]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[12]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[13]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[14]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # wait_and_click(driver,(By.XPATH,"//div[15]//button[1]"))
    # wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    # # wait_and_click(driver,(By.XPATH,"//div[16]//button[1]"))
    # #wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))

    for i in range(1, 16):  # Loop from 1 to 15 
        locater = f"//div[@class='movie-gallery']//div[{i}]//button[1]"
        locate = '/html/body/div/div/div[6]/button[1]'
        wait_and_click(driver, (By.XPATH, locater))
        wait_and_click(driver, (By.XPATH, locate))
        time.sleep(1)




    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='WATCHLIST']"))
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, -1000);")
    print("Scrolled up by 1000 pixels")
    time.sleep(2)

    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='search-bar']"),"The Batman")
    time.sleep(3)
    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='search-bar']"),"Spider")
    time.sleep(4)
    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='HOME']"))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//div[2]//button[1]"))
    time.sleep(4)
    wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))
    
    driver.execute_script("window.scrollBy(0, -1000);")
    print("Scrolled up by 1000 pixels")
    time.sleep(2)   
    wait_and_click(driver,(By.XPATH,"//div[10]//button[1]"))
    time.sleep(2)
    wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))
    time.sleep(1)
    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='search-bar']"),"Avengers")
    time.sleep(8)
    wait_and_click(driver,(By.XPATH,"//span[normalize-space()='Avengers Infinity War']"))
    time.sleep(6)
    print("finally")
    wait_and_click(driver,(By.XPATH,"//a[@class='watch-now-btn']"))
    time.sleep(5)
    wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(1)
    wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
  
    time.sleep(50)
    wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(4)


    wait_and_click(driver,(By.XPATH,"//a[normalize-space()='HOME']"))
    
    time.sleep(3)
    driver.save_screenshot("screenshot.png")





    


 


    




   

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")


