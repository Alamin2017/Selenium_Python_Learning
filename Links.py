import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
links=driver.find_elements(By.TAG_NAME, "a")
print("Number of links present:",len(links))
for link in links:
    print(link.text)


driver.find_element(By.LINK_TEXT, "Blogger").click()

