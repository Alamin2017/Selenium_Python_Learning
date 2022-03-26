import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()

inputboxes=driver.find_elements(By.XPATH, '//input[@class="text_field"]')
print(len(inputboxes))

status=driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print(status)
time.sleep(3)

status=driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print(status)
time.sleep(3)

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Al')
time.sleep(3)
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('Amin')
time.sleep(3)
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys('01629674872')