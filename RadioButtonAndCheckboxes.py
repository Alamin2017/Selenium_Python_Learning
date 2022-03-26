import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
status = driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print("Before selected:", status)
driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()

status = driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print("After selected:", status)

driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()

driver.find_element(By.XPATH, "//label[normalize-space()='Saturday']").click()
