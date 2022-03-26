import XLUtils
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://opensource-demo.orangehrmlive.com/')

path="D:\Soft\Python_Selenium\Browser\login1.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys(password)
    driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()






