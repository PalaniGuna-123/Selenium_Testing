from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()  

try:
    # Step 1: Open Edge profile settings
    driver.get("edge://settings/profiles")
    driver.maximize_window()
    print("Step 1: Opened Edge profile settings successfully.")

    # Step 2: Wait for the "Sign In" button to appear and click it
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='sign-in-button']/span"))
    )
    sign_in_button.click()
    print("Step 2: Clicked on 'Sign In' button.")

    # Step 3: Wait for sign-in process to complete
    print("Waiting for sign-in to complete. Please sign in manually if prompted...")
    time.sleep(9)  

    # Step 4: Open a new window and load the website
    driver.execute_script("window.open('https://fssamanagement.netlify.app/', '_blank');")
    print("Step 3: Opened a new window with the specified website.")

    # Step 5: Close the old window and switch to the new one
    old_window = driver.current_window_handle
    new_window = driver.window_handles[-1]
    driver.switch_to.window(old_window)
    driver.close()  # Close the old window
    print("Step 4: Closed the old window.")

    driver.switch_to.window(new_window)
    print("Step 5: Switched to the new window and ready to interact.")
     # Step 2: Click the login button on the main page
    log_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "login"))  
    )
    log_button.click()
    print("Step 2: Clicked the 'Login with Google' button.")
    time.sleep(1)

    # Step 3: Handle the Google Login Pop-up
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])  
    print("Step 3: Switched to Google login window.")
    time.sleep(1)
    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys("guna.palani@fssa.freshworks.com")  
    email_field.send_keys(Keys.ENTER)
    print("Step 4: Entered email address and submitted.")
    time.sleep(90)
except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(10)
    driver.quit()
    print("Browser closed.")
