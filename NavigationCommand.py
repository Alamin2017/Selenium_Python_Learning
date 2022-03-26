import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get("http://newtours.demoaut.com.cutestat.com/")
print(driver.title)

driver.get("https://www.pavantestingtools.com/")
print(driver.title)
time.sleep(3)
driver.back()
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(3)
print(driver.title)