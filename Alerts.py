import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#s = Service('D:\Soft\Python_Selenium\Browser\chromedriver.exe')
#driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.find_element(By.XPATH, "//button[normalize-space()='Click Me']").click()
alert_obj=driver.switch_to.alert
#alert_obj.accept()
alert_obj.dismiss()
