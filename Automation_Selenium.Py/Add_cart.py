import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()  
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(1)

# driver.find_element(By)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()


item_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
for button in item_buttons:
    button.click()
    time.sleep(1)


driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(1)


driver.find_element(By.ID, "checkout").click()
time.sleep(1)


driver.find_element(By.ID, "first-name").send_keys("Gunarakulan")
driver.find_element(By.ID, "last-name").send_keys("Gunaretnam")
driver.find_element(By.ID, "postal-code").send_keys("3456754321345")
time.sleep(1)



driver.find_element(By.ID, "continue").click()
time.sleep(1)


driver.find_element(By.ID, "finish").click()
time.sleep(1)


driver.find_element(By.ID, "back-to-products").click()



driver.quit()