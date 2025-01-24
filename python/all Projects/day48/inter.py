
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Chrome_driver_path = "C:/Users/muaza gazet/Desktop/devolopment/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(service=Service(Chrome_driver_path))

driver.get("https://www.wikipedia.org")


article_count = driver.find_element(By.CSS_SELECTOR, ".central-featured-lang a")


print(article_count.text)

driver.quit()
