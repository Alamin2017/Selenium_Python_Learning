from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

rows=len(driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr"))
print(rows)
col=len(driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr[1]/th"))
print(col)
