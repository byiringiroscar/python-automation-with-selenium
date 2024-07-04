from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.get_element(By.CLASS_NAME, "gLFyf")



time.sleep(10)

driver.quit()