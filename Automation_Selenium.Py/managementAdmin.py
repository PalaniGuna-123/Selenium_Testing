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
    
    expend=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='setting']/a/i"))
    )
    expend.click()
    print("step 9: Admin page clicked successfully")
    time.sleep(4)
    #----------Admin page testing-----------#
    add_member=WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.ID,"addMember"))
    )
    add_member.click()
    time.sleep(1)
    driver.find_element(By.ID, "newMemberUserName").send_keys("App user")
    driver.find_element(By.ID, "newMemberEmail").send_keys("palanigomadhi@gmail.com")
    role_dropdown_button = driver.find_element(By.ID, "newMemberRole")  
    role_dropdown_button.click()  
    tech_coach_option = driver.find_element(By.XPATH, "//a[text()='Tech coach']")  
    tech_coach_option.click()
   
    time.sleep(1)

   
    class_dropdown_button = driver.find_element(By.ID, "newMemberClass")  # Locate the dropdown button
    class_dropdown_button.click()  # Open the dropdown

    class_a_option = driver.find_element(By.XPATH, "//a[text()='Class A']")  # Locate the "Class A" option
    class_a_option.click()  # Click on the option

    print("Successfully selected 'Tech coach' and 'Class A'!")
    time.sleep(1)

    button=driver.find_element(By.ID,"confirmNewMember")
    button.click()
    print("step 10: submitted successfully")
    time.sleep(15)
    location="//*[@id='membersList']/div[5]/div[2]/button"

    #-------Edit member---------
    edit_icon=driver.find_element(By.XPATH,location)
    edit_icon.click()
    time.sleep(1)
    edit_drop=driver.find_element(By.XPATH,"//*[@id='editMemberRole']")
    edit_drop.click()
    time.sleep(1)

    edit_role=driver.find_element(By.XPATH,"//*[@id='forEditRole']/div/a[2]")
    edit_role.click()
    time.sleep(1)
    edit_mem=driver.find_element(By.ID,"editMemberClass")
    edit_mem.click()
    time.sleep(1)
    edit_class=driver.find_element(By.XPATH,"//*[@id='forEditClass']/div/a[2]")
    edit_class.click()
    time.sleep(1)
    edit_submit=driver.find_element(By.ID,"confirmEditMemberData")
    edit_submit.click()
    time.sleep(9)
    print("Step 11: successfully")
    #repeat loop

    edit_ico=driver.find_element(By.XPATH,location) 
    edit_ico.click()
    time.sleep(8)
    classC=driver.find_element(By.ID,"editMemberClass")
    classC.click()
    time.sleep(4)
    class_sec=driver.find_element(By.XPATH,"//*[@id='forEditClass']/div/a[3]")
    class_sec.click()
    time.sleep(4)
    edit_submits=driver.find_element(By.ID,"confirmEditMemberData")
    edit_submits.click()
    print("step 12: change member role authority")
    time.sleep(9)
    #repeat check
    edit_ic=driver.find_element(By.XPATH,location) 
    edit_ic.click()
    time.sleep(2)
    edit_dro=driver.find_element(By.XPATH,'//*[@id="editMemberRole"]')
    edit_dro.click()
    time.sleep(2)
    edit_rle=driver.find_element(By.XPATH,"//*[@id='forEditRole']/div/a[3]")
    edit_rle.click()
    time.sleep(2)
    edit_mit=driver.find_element(By.ID,"confirmEditMemberData")
    edit_mit.click()
    print('step 13: promoted head coach ')
    time.sleep(10)

    #Add management
    edit_icons=driver.find_element(By.XPATH,location) 
    edit_icons.click()
    time.sleep(2)
    edit_drops=driver.find_element(By.XPATH,'//*[@id="editMemberRole"]')
    edit_drops.click()
    time.sleep(8)

    edit_roles=driver.find_element(By.XPATH,"//*[@id='forEditRole']/div/a[4]")
    edit_roles.click()
    time.sleep(1)
    edit_it=driver.find_element(By.ID,"confirmEditMemberData")
    edit_it.click()
    print('step 14: promoted admin')
    time.sleep(10)

    #check cancel functionality
    edit_n=driver.find_element(By.XPATH,location) 
    edit_n.click()
    time.sleep(2)
    edit_p=driver.find_element(By.XPATH,'//*[@id="editMemberRole"]')
    edit_p.click()
    time.sleep(1)

    edit_roless=driver.find_element(By.XPATH,"//*[@id='forEditRole']/div/a[2]")
    edit_roless.click()
    time.sleep(1)
    edit_t=driver.find_element(By.ID,"cancelEditMemberData")
    edit_t.click()
    print("step 15: cancel successfully")
    time.sleep(10)

    #remove member functionality
    edit_on=driver.find_element(By.XPATH,location) 
    edit_on.click()
    time.sleep(2)
    target_element = driver.find_element(By.ID, "changeProfileButton")
    actions.move_to_element(target_element).perform()
    time.sleep(5)
    element = driver.find_element(By.XPATH, "//*[@id='showMembers']/p")
    actions.move_to_element(element).perform()
    time.sleep(4)
    elements = driver.find_element(By.XPATH, "//*[@id='logout']/p")
    actions.move_to_element(elements).perform()
    time.sleep(4)
    dele = driver.find_element(By.XPATH,' //*[@id="deleteMember"]')
    actions.move_to_element(dele).perform()
    time.sleep(4)
    edit_s=driver.find_element(By.XPATH,' //*[@id="deleteMember"]')
    edit_s.click()
    print('deletebutton clicked successfully')
    time.sleep(5)
    check=driver.find_element(By.ID,"deleteYes")
    check.click()
    print('step 16: delete member successfully')
    time.sleep(10)
    extend=driver.find_element(By.XPATH,'//*[@id="sidebar"]/div/div/button/i')
    extend.click()
    time.sleep(3)
except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(1)
    driver.quit()
    print("Browser closed.")
