# Selenium_Testing
This is my selenium testing code
# Selenium Automation Script - Concert Craze

## Introduction
This project automates the process of signing up, searching for a concert, booking tickets, and logging out on the Concert Craze website. It uses **Python** and the **Selenium WebDriver** library to interact with the website and perform end-to-end testing of the user journey.

## Features
- Generates 100 unique email addresses for testing sign-ups.
- Automates the following workflow:
  - Sign Up
  - Search for a concert
  - Book tickets
  - Enter ticket details (first name, last name, email, phone number)
  - Confirm payment
  - View booking details
  - Logout

## Prerequisites
- Python 3.7 or later installed on your system.
- Google Chrome browser installed.
- ChromeDriver compatible with your Chrome browser version.
- Basic knowledge of Python and Selenium.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/concert-craze-automation.git
   cd concert-craze-automation
   ```

2. Install the required Python libraries:
   ```bash
   pip install selenium
   ```

3. Download the appropriate version of ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
   - Ensure it matches your Chrome browser version.
   - Add ChromeDriver to your system's PATH.

## Usage
1. Open the `concert_craze_automation.py` file and ensure the `driver.get()` URL matches the Concert Craze website.

2. Run the script:
   ```bash
   python concert_craze_automation.py
   ```

3. The script will:
   - Open the Concert Craze website.
   - Sign up a user using a randomly generated email address.
   - Search for a concert by entering a keyword (e.g., "Anirudh").
   - Book tickets and fill in the required details.
   - Confirm the payment process and log out.

## Code Overview
### Email Generation
The script generates unique email addresses using the `random` module:
```python
import random

def generate_email():
    return f"GunaGuna{random.randint(100000, 999999)}@example.com"

emails = [generate_email() for _ in range(100)]
```

### Selenium Workflow
1. **Sign Up**
   ```python
   driver.find_element(By.ID, "username").send_keys("Guna_Palani")
   driver.find_element(By.ID, "email").send_keys(email)
   driver.find_element(By.ID, "password").send_keys("Test@1234")
   driver.find_element(By.ID, "confirm-password").send_keys("Test@1234")
   ```
2. **Search for a Concert**
   ```python
   driver.find_element(By.ID, "searchBox").send_keys("Anirudh")
   ```
3. **Book Tickets**
   ```python
   driver.find_element(By.ID, "addTicket").click()
   driver.find_element(By.XPATH, "//*[@id='ticketsContainer']/div/div[1]/div[1]/input").send_keys("Guna")
   ```
4. **Confirm Payment**
   ```python
   driver.find_element(By.ID, "confirmPayment").click()
   ```
5. **Logout**
   ```python
   driver.find_element(By.ID, "logoutButton").click()
   ```

### Handling Alerts
The script handles alerts using:
```python
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()
```

### Scrolling
Scrolls the page to view elements:
```python
driver.execute_script("window.scrollBy(0, 1000);")
```

### Full Code
```python
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
    submit_search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='searchBtn']"))
    )
    submit_search_button.click()
    print("Search button clicked successfully!")

    click_book_to = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#resultsContainer > div > div > div.col-md-8 > div > a"))
    )
    click_book_to.click()
    time.sleep(2)
    print("Book button clicked successfully")

    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    time.sleep(2)

    purchase_ticket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "purchase"))
    )
    purchase_ticket.click()
    print("Purchase ticket clicked successfully")
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    time.sleep(2)

    add_ticket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "addTicket"))
    )
    add_ticket.click()
    print("Add ticket clicked successfully")
    time.sleep(2)

    ticket_user = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ticketsContainer']/div/div[1]/div[1]/input"))
    )
    ticket_user.click()
    print("User name input button clicked successfully")
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='ticketsContainer']/div/div[1]/div[1]/input").send_keys("Guna")

    last_name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ticketsContainer']/div/div[1]/div[2]/input"))
    )
    last_name.click()
    print("Last name clicked successfully")
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='ticketsContainer']/div/div[1]/div[2]/input").send_keys("Vision")

    email_name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ticketsContainer']/div/div[2]/input"))
    )
    email_name.click()
    driver.find_element(By.XPATH, "//*[@id='ticketsContainer']/div/div[2]/input").send_keys(email)
    time.sleep(2)
    print("Email entered successfully")

    phone_num = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ticketsContainer']/div/div[3]/input"))
    )
    phone_num.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='ticketsContainer']/div/div[3]/input").send_keys(1234567890)

    print("Phone number clicked successfully")

    conform_ticket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "payNow"))
    )
    conform_ticket.click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    time.sleep(2)

    conform_ticket_f = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "confirmPayment"))
    )
    conform_ticket_f.click()

    time.sleep(1)
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Switch to the alert and click OK
    alert.accept()
    print("Clicked OK on the alert")
    time.sleep(3)

    view_more = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "viewBtn"))
    )
    view_more.click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 1000);")
    print("Scrolled down by 1000 pixels")
    time.sleep(2)

    log_out = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logoutButton"))
    )
    log_out.click()
    time.sleep(2)
    print("Log out button clicked successfully")

    driver.quit()
```

## Customization
- Update the `searchBox` input value to test different concerts.
- Modify ticket details as required.

## Known Issues
- Ensure stable internet connectivity for the website to load correctly.
- Adjust wait times (`WebDriverWait` and `time.sleep`) based on your system performance.

## Disclaimer
This script is designed for testing purposes only. Use it responsibly and ensure you have permission to test on the target website.

## Author
Guna Palani

Feel free to contribute by submitting issues or pull requests!

