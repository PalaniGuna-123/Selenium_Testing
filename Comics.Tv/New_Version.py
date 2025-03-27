from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def Wait_and_click(driver,locater,timeout=15):
    element=WebDriverWait(driver,timeout).until(
        EC.element_to_be_clickable(locater)
    )
    element.click()
def wait_and_Clear_send_keys(driver, locator, keys, timeout=15):
    """Wait for an element to be visible and send keys."""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    element.clear()
    element.send_keys(keys)
    


#step 2 
driver=webdriver.Chrome()
try:

    url="http://localhost:4000/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)

#step3

    element_to_hover=driver.find_element(By.XPATH,'//*[@id="search-bar"]')
    actions=ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    print('step 2 is Success')
    time.sleep(2)

    # driver.execute_script("window.scrollBy(0,1000);")
    # print("Scroll Success")

#step 4
    Wait_and_click(driver,(By.XPATH,'//div[@class="movie-gallery"]//div[1]//button[1]'))
    time.sleep(2)
    Wait_and_click(driver,(By.XPATH,"//button[normalize-space()='OK']"))

#     Wait_and_click(driver,(By.XPATH,"//div[2]//button[1]"))
#     Wait_and_click(driver(By.XPATH,"//button[normalize-space()='OK']"))
# #step 05 

    Wait_and_click(driver,(By.XPATH,"//span[normalize-space()='Avengers Infinity War']"))
    time.sleep(2)
    element_to_hover = driver.find_element(By.XPATH, "//a[@class='watch-now-btn']")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(3)
    Wait_and_click(driver,(By.XPATH,"//a[@class='watch-now-btn']"))
    time.sleep(1)
    Wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(5)
    Wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(2)

    driver.back()

#step 06

    Wait_and_click(driver,(By.XPATH,"//a[normalize-space()='WATCHLIST']"))
    time.sleep(3)

    Wait_and_click(driver,(By.XPATH,"//div[@id='movie-1']//button[@class='remove-from-watchlist-btn'][normalize-space()='Remove']"))
    time.sleep(2)
    Wait_and_click(driver,(By.XPATH,"//button[normalize-space()='OK']"))
    time.sleep(2)

    Wait_and_click(driver,(By.XPATH,"//a[normalize-space()='HOME']"))
    time.sleep(3)

#step 06 LOops to Click Multiple Movie Buttons

# //div[@class='movie-gallery']//div[1]//button[1]
# //div[2]//button[1]
# //div[3]//button[1]
    for i in range(1,16):
        locater = f"//div[@class='movie-gallery']//div[{i}]//button[1]"
        locate = '/html/body/div/div/div[6]/button[1]'
        Wait_and_click(driver, (By.XPATH, locater))
        Wait_and_click(driver, (By.XPATH, locate))
        time.sleep(1)
#step 07

    Wait_and_click(driver,(By.XPATH,"//a[normalize-space()='WATCHLIST']"))
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(3)

    driver.execute_script("window.scrollBy(0,-1000)")
    time.sleep(2)

#Step 08

    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='search-bar']"),"The Bat")
    time.sleep(3)
    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='search-bar']"),"Spider")
    time.sleep(4)
    Wait_and_click(driver,(By.XPATH,"//a[normalize-space()='HOME']"))
    time.sleep(1)
    Wait_and_click(driver,(By.XPATH,"//div[2]//button[1]"))
    time.sleep(4)
    Wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))
    
    driver.execute_script("window.scrollBy(0, -1000);")
    print("Scrolled up by 1000 pixels")
    time.sleep(2)   
    Wait_and_click(driver,(By.XPATH,"//div[10]//button[1]"))
    time.sleep(2)
    Wait_and_click(driver,(By.XPATH,'/html/body/div/div/div[6]/button[1]'))
    time.sleep(1)
    wait_and_Clear_send_keys(driver,(By.XPATH,"//input[@id='search-bar']"),"Avengers")
    time.sleep(8)
    Wait_and_click(driver,(By.XPATH,"//span[normalize-space()='Avengers Infinity War']"))
    time.sleep(6)
    print("finally")
    Wait_and_click(driver,(By.XPATH,"//a[@class='watch-now-btn']"))
    time.sleep(5)
    Wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(2)
    Wait_and_click(driver,(By.XPATH,"//video[@id='video']"))
    time.sleep(2)
    Wait_and_click(driver,(By.XPATH,"//a[normalize-space()='HOME']"))
    
    time.sleep(3)
    driver.save_screenshot("screenshot.png")




except Exception as e:
    print(f"An error occurred :{e}")
finally:
    driver.quit()
    print("Browser Closed")