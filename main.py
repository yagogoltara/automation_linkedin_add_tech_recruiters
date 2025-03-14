from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

USER_EMAIL=os.getenv("USER_EMAIL")
PASS=os.getenv("PASS")

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")
login_by_email = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/a')
login_by_email.click()

user_input = driver.find_element(by=By.ID, value="username").send_keys(USER_EMAIL)
pass_input = driver.find_element(by=By.ID, value="password").send_keys(PASS)

sleep(5)
driver.close()
