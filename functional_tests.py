from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

lista = [['paracetamol', 'tramadol', 'pain'],
         ['paracetamol', 'brintellix', 'pain'],
         ['euthyrox', 'brintellix', 'pain'],
         ['paracetamol', 'tramadol', 'pain'],
         ['euthyrox', 'pradaxa', 'diabetic']]

driver = webdriver.Chrome(executable_path='C:\Testfiles\chromedriver.exe')

for i, x in enumerate(lista):
    driver.switch_to.window(driver.window_handles[i])
    driver.get('http://127.0.0.1:5000/')
    driver.find_element_by_id("content1").send_keys(x[0])
    driver.find_element_by_id("content2").send_keys(x[1])
    driver.find_element_by_id("content3").send_keys(x[2])
    driver.find_element_by_tag_name("button").click()
    if i+1 < len(lista):
        driver.execute_script("window.open('');")
    else:
        pass


