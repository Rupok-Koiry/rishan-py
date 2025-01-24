from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from time import sleep

# Facebook credentials
FB_EMAIL = "koiryrishan1@gmail.com"
FB_PASSWORD = "RISHAN2@12"

# Path to ChromeDriver
chrome_driver_path = "C:/users/muaza gazet/Desktop/R I S H A N/devolopment/chromedriver-win64/chromedriver.exe"

# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Tinder
driver.get("http://www.tinder.com")
sleep(2)

# Click "Log in" button
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[text()="Log in"]'))
    )
    login_button.click()
except TimeoutException:
    print("Login button not found.")
    driver.quit()
    exit()

# Select "Log in with Facebook"
try:
    fb_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[text()="Log in with Facebook"]'))
    )
    fb_login_button.click()
except TimeoutException:
    print("Facebook login button not found.")
    driver.quit()
    exit()

# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Enter Facebook credentials
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    password_input = driver.find_element(By.ID, 'pass')
    email_input.send_keys(FB_EMAIL)
    password_input.send_keys(FB_PASSWORD)
    password_input.send_keys(Keys.ENTER)
except TimeoutException:
    print("Facebook login form not found.")
    driver.quit()
    exit()

# Switch back to Tinder window
driver.switch_to.window(base_window)
sleep(5)

# Handle popups
try:
    allow_location = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Allow"]'))
    )
    allow_location.click()
except TimeoutException:
    print("Allow location popup not found.")

try:
    notifications_popup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Not interested"]'))
    )
    notifications_popup.click()
except TimeoutException:
    print("Notifications popup not found.")

try:
    cookies_popup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="I accept"]'))
    )
    cookies_popup.click()
except TimeoutException:
    print("Cookies popup not found.")

# Start swiping
for _ in range(100):
    sleep(1)
    try:
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Like"]'))
        )
        like_button.click()
        print("Swiped right.")
    except TimeoutException:
        print("Like button not found. Skipping.")
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            print("Match popup not found.")

# Close the browser
driver.quit()
