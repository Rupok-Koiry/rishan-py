from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Chrome_driver_path = "C:/Users/muaza gazet/Desktop/devolopment/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(service=Service(Chrome_driver_path))

driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4098469952&discover=recommended%2Ctop-applicant%2Chiring-in-network&discoveryOrigin=JOBS_HOME_COMPETITIVE_ADVANTAGE_JOB_COLLECTIONS")
