import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
driver.maximize_window()
user_ele = driver.find_element(By.XPATH, "//input[@id='email']")
pwd_ele = driver.find_element(By.XPATH, "//input[@id='pass']")
user_ele.clear()
pwd_ele.clear()
time.sleep(3)
user_ele.send_keys("alamincse12@gmail.com")
pwd_ele.send_keys("123088")
driver.find_element(By.NAME, "login").click()

print("Login successfully done")
