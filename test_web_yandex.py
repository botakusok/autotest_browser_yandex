from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("http://ya.ru")
time.sleep(5)
element = browser.find_element(By.ID, "js-button").click()
time.sleep(5)
element2 = browser.find_element(By.CSS_SELECTOR, "button.DistributionButtonClose.Button_size_m").click()
time.sleep(10)
alice_click = browser.find_element(By.CSS_SELECTOR, "[style*='url(https://yastatic.net/s3/home/slices_section/alice_fancy_1.png)']").click()
time.sleep(5)
browser.quit()

