from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://www.amazon.com/')
driver.maximize_window()

cookies=driver.get_cookies()
print(len(cookies))


cookie={'name':'mycookie','value':'12334567'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))


driver.delete_cookie('mycookie')

cookies=driver.get_cookies()
print(len(cookies))
