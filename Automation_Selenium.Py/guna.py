from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Edge()  # Ensure you have the correct WebDriver for Edge

try:
    # Step 1: Open the target website directly
    driver.get("https://fssamanagement.netlify.app/")  # Directly open the website
    driver.maximize_window()
    print("Step 1: Opened the target website successfully.")

    # Step 2: Click the login button on the main page
    log_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login"))  # Replace "login" with the actual button ID
    )
    log_button.click()
    print("Step 2: Clicked the 'Login with Google' button.")
    time.sleep(3)

    # Step 3: Handle the Google Login Pop-up
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])  # Switch to Google login window
    print("Step 3: Switched to Google login window.")

    # Step 4: Enter email address in the Google login form
    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys("guna.palani@fssa.freshworks.com")  # Replace with your email
    email_field.send_keys(Keys.ENTER)
    print("Step 4: Entered email address and submitted.")

    # Step 5: Handle any further Google login steps (like password or verification)
    time.sleep(7)  # Adjust based on actual Google login flow

except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(10)  # Add time to observe the results
    driver.quit()
    print("Browser closed.")
