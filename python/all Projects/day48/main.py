from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(r"C:/Users/muaza gazet/Desktop/devolopment/chromedriver-win64/chromedriver.exe"))
driver.get("https://www.python.org")

events = {i: {'name': name.text, 'time': time.text} for i, (name, time) in enumerate(zip(
    driver.find_elements(By.CSS_SELECTOR, ".event-widget li a"),
    driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
))}

print(events)

driver.quit()
