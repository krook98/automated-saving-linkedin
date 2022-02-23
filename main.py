from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105076658&keywords=junior%20python%20developer&location=Warszawa%2C%20Woj.%20Mazowieckie%2C%20Polska"
chrome_driver = '/Users/kuba/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url)

login = driver.find_element_by_class_name("nav__button-secondary")
login.click()

# Auto login
id = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

# Enter your login data
id.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Save job offer
time.sleep(2)
all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in all_jobs:
    try:
        job.click()
        time.sleep(2)
        save = driver.find_element_by_class_name("jobs-save-button")
        save.click()
        time.sleep(2)
    except NoSuchElementException:
        continue

time.sleep(3)
driver.quit()


