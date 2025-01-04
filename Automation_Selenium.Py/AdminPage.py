from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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

# Initialize the WebDriver
driver = webdriver.Edge()

try:
    # Step 1: Open Edge profile settings
    driver.get("edge://settings/profiles")
    driver.maximize_window()
    print("Step 1: Opened Edge profile settings successfully.")

    # Step 2: Click 'Sign In'
    wait_and_click(driver, (By.XPATH, "//*[@id='sign-in-button']/span"))
    print("Step 2: Clicked on 'Sign In' button.")

    # Step 3: Open a new window and switch to it
    driver.execute_script("window.open('https://fssamanagement.netlify.app/', '_blank');")
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
    old_window = driver.current_window_handle  # Save old window
    new_window = [handle for handle in driver.window_handles if handle != old_window][0]
    driver.switch_to.window(new_window)
    print("Step 3: Switched to the new window.")

    # Step 4: Click the "Login with Google" button
    wait_and_click(driver, (By.ID, "login"))
    print("Step 4: Clicked 'Login with Google' button.")

    # Step 5: Handle Google login
    WebDriverWait(driver, 20).until(lambda d: len(d.window_handles) == 3)
    google_window = [handle for handle in driver.window_handles if handle != new_window and handle != old_window][0]
    driver.switch_to.window(google_window)
    wait_and_send_keys(driver, (By.XPATH, "//input[@type='email']"), "guna.palani@fssa.freshworks.com")
    wait_and_click(driver, (By.XPATH, "//span[text()='Next']"))
    print("Step 5: Google login completed.")
    driver.switch_to.window(new_window)

    # Step 6: Open the Admin page
    wait_and_click(driver, (By.XPATH, "//*[@id='setting']/a/i"))
    print("Step 6: Opened Admin page.")

    # Step 7: Add a new member
    wait_and_click(driver, (By.ID, "addMember"))
    wait_and_send_keys(driver, (By.ID, "newMemberUserName"), "App user")
    wait_and_send_keys(driver, (By.ID, "newMemberEmail"), "palanigomadhi@gmail.com")
    select_dropdown_option(driver, (By.ID, "newMemberRole"), (By.XPATH, "//a[text()='Tech coach']"))
    select_dropdown_option(driver, (By.ID, "newMemberClass"), (By.XPATH, "//a[text()='Class A']"))
    wait_and_click(driver, (By.ID, "confirmNewMember"))
    print("Step 7: Added a new member successfully.")

    # Step 8: Edit member details
    member_xpath = "//*[@id='membersList']/div[5]/div[2]/button/i"
    wait_and_click(driver, (By.XPATH, member_xpath))
    select_dropdown_option(driver, (By.XPATH, "//*[@id='editMemberRole']"), (By.XPATH, "//*[@id='forEditRole']/div/a[2]"))
    select_dropdown_option(driver, (By.ID, "editMemberClass"), (By.XPATH, "//*[@id='forEditClass']/div/a[2]"))
    wait_and_click(driver, (By.ID, "confirmEditMemberData"))
    print("Step 8: Edited member details successfully.")

  
    # Step 09: Remove a member
    wait_and_click(driver, (By.XPATH, member_xpath))
    wait_and_click(driver, (By.ID, "deleteMember"))
    wait_and_click(driver, (By.ID, "deleteYes"))
    print("Step 9: Member removed successfully.")

    #Navigate the attendance page
    wait_and_click(driver,(By.XPATH,'//*[@id="sidebar"]/div/div/button/i'))
    wait_and_click(driver,(By.XPATH,'//*[@id="home"]/span'))
    print('step 10: home page clicked successfully')
    # time.sleep(5)

    #choose class functionality
    wait_and_click(driver,(By.ID,'changeClass'))
    wait_and_click(driver,(By.XPATH,'//*[@id="showClassesForLead"]/div[2]/button[2]'))
    print('step 11: Choose B class successfully')
    # time.sleep(9)

    wait_and_click(driver,(By.XPATH,'//*[@id="sidebar"]/div/div/button/i'))
    # time.sleep(9)
    


    #wait_and_click(driver,10(By.XPATH,''))
    wait_and_click(driver,(By.XPATH,'//*[@id="monthlyReport"]'))
    print("Step 12: Month updated page navigated successfully.")
    time.sleep(10)

    wait_and_click(driver,(By.ID,'new'))
    print('step 13: New month clicked successfully')
    # time.sleep(4)

    wait_and_send_keys(driver, (By.ID, "newMonth"), "February 2025")
    wait_and_click(driver,(By.ID,'confirm'))
    driver.refresh()
    # time.sleep(10)
    print('step 14: New month updated successfully')

    wait_and_click(driver,(By.XPATH,'//*[@id="attendance"]/i'))
    print('open successfully')

    wait_and_click(driver,(By.XPATH,'/html/body/div[5]/div[1]/p'))
    print('step 15: Clicked Attendance')
    time.sleep(10)

    wait_and_click(driver,(By.XPATH,'//*[@id="infoLogo"]/i'))
    time.sleep(12)
    wait_and_click(driver,(By.XPATH,'//*[@id="closePopupBtnForCount"]'))
    print('closePup up button successfully')

    # element=wait_and_click(driver,(By.XPATH,'//*[@id="attendanceTable"]/div[1]/div/div/div/table/tbody/tr[1]/td[4]'))
    # actions = ActionChains(driver)
    # actions.double_click(element).perform()
    # print("Double-click performed successfully.")

    # wait=wait_and_click(driver,(By.XPATH,'//*[@id="attendanceTable"]/div[6]/textarea'))


   
    # dropdown=Select(wait)
    # dropdown.select_by_index(1)
    # time.sleep(10)

    # wait_and_click(driver,(By.XPATH,'//*[@id="ht_73c422c5d49fcca3"]/div[1]/div/div/div/table/tbody/tr[1]/td'))
    # print('keys entered successfully')
    # time.sleep(10)





 

    
   

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")
