import random
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Function to generate random email IDs
def generate_email():
    return f"GunaGuna{random.randint(100000, 999999)}@example.com"

emails = [generate_email() for _ in range(100)]

# Initialize the WebDriver
driver = webdriver.Chrome()

for i in range(100):
        email = emails[i]

    # Open the webpage
driver.get("https://concertcraze.netlify.app/")
driver.maximize_window()
time.sleep(2)

    # Click on the "Sign Up" button
signup_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "signBtn"))
    )
signup_button.click()
print("Sign Up button clicked successfully!")

    # Fill in the Sign Up form
driver.find_element(By.ID, "username").send_keys("Guna_Palani")
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "password").send_keys("Test@1234")
driver.find_element(By.ID, "confirm-password").send_keys("Test@1234")

    # Click the Sign Up submit button
signup_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
signup_submit_button.click()
print("Form submitted, waiting for response...")

    # Wait for the URL to change and check if navigation to home page is successful
WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchBox"))
    )
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "searchBox"))
)
search_box.click() 
time.sleep(4)
driver.find_element(By.XPATH, "//*[@id='searchBox']").send_keys("Anirudh")
submit_search_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH," //*[@id='searchBtn']"))
)
submit_search_button.click()
print("Search button clicked successfully!")


click_book_to=WebDriverWait(driver,4).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR,"#resultsContainer > div > div > div.col-md-8 > div > a"))
)
click_book_to.click()
time.sleep(2)
print("book button clicked successfully")

driver.execute_script("window.scrollBy(0, 1000);")
print("Scrolled down by 1000 pixels")
time.sleep(2)


purchase_ticket=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.ID,"purchase"))
)
purchase_ticket.click()
print("purchase ticket clicked successfully")
time.sleep(2)


driver.execute_script("window.scrollBy(0, 1000);")
print("Scrolled down by 1000 pixels")
time.sleep(2)

add_ticket=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.ID,"addTicket"))
)
add_ticket.click()
print("add ticket clicked successfully")
time.sleep(2)



ticket_user=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,"//*[@id='ticketsContainer']/div/div[1]/div[1]/input"))
)
ticket_user.click()
print("user name input button clicked successfully")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='ticketsContainer']/div/div[1]/div[1]/input").send_keys("Guna")




last_name=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,"//*[@id='ticketsContainer']/div/div[1]/div[2]/input"))
)
last_name.click()
print("last name clicked successfully")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='ticketsContainer']/div/div[1]/div[2]/input").send_keys("Vision")



email_name=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH,"//*[@id='ticketsContainer']/div/div[2]/input"))
)
email_name.click()
driver.find_element(By.XPATH,"//*[@id='ticketsContainer']/div/div[2]/input").send_keys(email)
time.sleep(2)
print("email entered  successfully")

phone_num=WebDriverWait(driver,10).until(
  EC.element_to_be_clickable((By.XPATH,"//*[@id='ticketsContainer']/div/div[3]/input"))
)
phone_num.click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='ticketsContainer']/div/div[3]/input").send_keys(1234567890)

print("phone num clicked successfully")

conform_ticket=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.ID,"payNow"))
)
conform_ticket.click()
time.sleep(2)


driver.execute_script("window.scrollBy(0, 1000);")
print("Scrolled down by 1000 pixels")
time.sleep(2)


conform_ticket_f=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.ID,"confirmPayment"))
)
conform_ticket_f.click()


time.sleep(1)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to the alert and click OK
alert.accept()
print("Clicked OK on the alert")
time.sleep(3)

view_more=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.ID,"viewBtn"))
)
view_more.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 1000);")
print("Scrolled down by 1000 pixels")
time.sleep(2)

log_out=WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.ID,"logoutButton"))
)
log_out.click()
time.sleep(2)
print("log out button clicked successfully")

driver.quit()


