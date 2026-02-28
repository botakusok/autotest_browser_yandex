from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://ya.ru")
time.sleep(5)
browser.quit()