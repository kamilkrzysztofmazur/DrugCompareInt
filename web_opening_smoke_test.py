from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Testfiles\chromedriver.exe')
driver.get('http://127.0.0.1:5000/')
title = driver.title
print(title)
assert title == 'Home'
driver.quit()

