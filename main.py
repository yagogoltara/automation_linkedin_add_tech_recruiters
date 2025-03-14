from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")
login_by_email = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/a')
login_by_email.click()


sleep(5)
driver.close()
