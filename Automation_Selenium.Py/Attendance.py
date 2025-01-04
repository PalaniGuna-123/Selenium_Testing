from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Edge()  

try:
   
    driver.get("edge://settings/profiles")
    driver.maximize_window()
    print("Step 1: Opened Edge profile settings successfully.")

    actions = ActionChains(driver)
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='sign-in-button']/span"))
    )
    #actions.double_click(sign_in_button).perform()

    sign_in_button.click()
    print("Step 2: Clicked on 'Sign In' button.")

    
    print("Waiting for sign-in to complete. Please sign in manually if prompted...")
    time.sleep(9)  
    
    driver.execute_script("window.open('https://fssamanagement.netlify.app/', '_blank');")
    print("Step 3: Opened a new window with the specified website.")

    old_window = driver.current_window_handle
    new_window = driver.window_handles[-1]
    driver.switch_to.window(old_window)
    driver.close()  
    print("Step 4: Closed the old window.")

    driver.switch_to.window(new_window)
    print("Step 5: Switched to the new window and ready to interact.")
     
    log_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "login"))  
    )
    log_button.click()
    print("Step 6: Clicked the 'Login with Google' button.")
    time.sleep(1)

    # Handle the Google Login Pop-up
    WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])  
    print("Step 7: Switched to Google login window.")
    time.sleep(8)
    email_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys("guna.palani@fssa.freshworks.com")  
    email_field.send_keys(Keys.ENTER)
    print("Step 8: Entered email address and submitted.")
    time.sleep(30)
    
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    extend=driver.find_element(By.XPATH,'//*[@id="sidebar"]/div/div/button/i')
    extend.click()
    time.sleep(3)


except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(1)
    driver.quit()
    print("Browser closed.")
