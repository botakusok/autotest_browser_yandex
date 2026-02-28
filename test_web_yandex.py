from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.get("http://ya.ru")
time.sleep(5)
element = browser.find_element(By.CLASS_NAME, "gdNaxmEdBjnJz-cection__item-icon").click()
time.sleep(5)
browser.quit()