from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("http://ya.ru")
time.sleep(5)
element = browser.find_element(By.ID, "js-button").click()
time.sleep(5)
element = browser.find_element(By.CSS_SELECTOR, "button.DistributionButtonClose.Button_size_m").click()
time.sleep(5)
browser.quit()

