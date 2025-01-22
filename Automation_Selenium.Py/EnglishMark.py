from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Edge()

try:
    # Step 1: Open Edge profile settings
    driver.get("edge://settings/profiles")
    driver.maximize_window()
    print("Step 1: Opened Edge profile settings successfully.")

    # Step 2: Click 'Sign In'
    sign_in_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='sign-in-button']/span"))
    )
    sign_in_button.click()
    print("Step 2: Clicked on 'Sign In' button.")

    # Step 3: Open a new window and switch to it
    driver.execute_script("window.open('https://fssamanagement.netlify.app/', '_blank');")
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
    old_window = driver.current_window_handle  # Save old window
    new_window = [handle for handle in driver.window_handles if handle != old_window][0]
    driver.switch_to.window(new_window)
    print("Step 3: Switched to the new window.")

    # Step 4: Click the "Login with Google" button
    login_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "login"))
    )
    login_button.click()
    print("Step 4: Clicked 'Login with Google' button.")

    # Step 5: Handle Google login
    WebDriverWait(driver, 20).until(lambda d: len(d.window_handles) == 3)
    google_window = [handle for handle in driver.window_handles if handle != new_window and handle != old_window][0]
    driver.switch_to.window(google_window)
    
    email_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_input.send_keys("guna.palani@fssa.freshworks.com")
    
    next_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
    )
    next_button.click()
    print("Step 5: Google login completed.")
    
    driver.switch_to.window(new_window)
    time.sleep(10)

    # home_button = WebDriverWait(driver, 15).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="home"]/span'))
    # )
    # home_button.click()
    # print('Step 10: Home page clicked successfully')

    # Choose class functionality
    change_class_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'changeClass'))
    )
    change_class_button.click()
    time.sleep(2)
    
    choose_class_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="showClassesForLead"]/div[2]/button[2]'))
    )
    choose_class_button.click()
    print('Step 11: Choose B class successfully')
    time.sleep(2)

    sidebar_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div/div/button/i'))
    )
    sidebar_button.click()
    time.sleep(2)
    
    class_option_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='lni lni-book']"))
    )
    class_option_button.click()
    print("Step 23: Class option clicked successfully")

    english_option_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='english']"))
    )
    english_option_button.click()
    time.sleep(2)
    print("Step 24: English option clicked successfully")

    february_option_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='February 2025']"))
    )
    february_option_button.click()
    time.sleep(2)
    print("Step 24: February clicked successfully")
    time.sleep(3)

    new_test_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='newTest']"))
    )
    new_test_button.click()
    time.sleep(2)
    print("Step 25: New Test clicked successfully")
    time.sleep(5)

    # dataset_name_input = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@id='datasetName']"))
    # )
    # dataset_name_input.send_keys("Communication English")
    # time.sleep(2)
    
    # total_marks_input = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@id='totalMarks']"))
    # )
    # total_marks_input.send_keys(100)
    # time.sleep(2)<td class="current highlight"></td>

    mark=WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='ht_clone_top handsontable']//span[@class='colHeader'][normalize-space()='Marks']"))
    )
    mark.send_keys(100)
    # marks=WebDriverWait(driver,15).until(
    #     EC.presence_of_element_located((By.XPATH,"//td[@class='current area highlight']"))
    # )
    # marks.send_keys(100)
    mark.send_keys(Keys.ENTER)
    mark.send_keys(Keys.ENTER,100)



    print('All steps completed successfully.')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")
