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
    
# Switch to the Google login window
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait for the second window to open
    print("Window handles before switching:", driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])  # Switch to the Google login window
    print("Switched to window:", driver.current_window_handle)

# Wait for the email input field to appear
    email_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys("guna.palani@fssa.freshworks.com")
    email_field.send_keys(Keys.ENTER)
    print("Step 4: Entered email address and submitted.")

# Wait for login to complete (you can use a specific element that shows after login)
    WebDriverWait(driver, 90).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/h2/img"))  # Replace with an actual element visible after login
    )
    print("Login completed.")

# Expand settings
    expend = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='setting']/a/i"))
    )
    expend.click()
    print("Step 5: Expanded settings.")

except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(1)
    driver.quit()
    print("Browser closed.")
