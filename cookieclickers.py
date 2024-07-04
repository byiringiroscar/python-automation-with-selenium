from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)



driver.get("https://orteil.dashnet.org/cookieclicker/")


search_bar = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "langSelectButton"))
)

choose_lang = driver.find_element(By.CLASS_NAME, "langSelectButton")
choose_lang.click()


cookie_id = "bigCookie"

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()


time.sleep(5)

driver.quit()
