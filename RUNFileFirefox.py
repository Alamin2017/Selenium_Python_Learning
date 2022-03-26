import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#s = Service('D:\Soft\Python_Selenium\Firefox\geckodriver.exe')
#driver = webdriver.Firefox(service=s)

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()
time.sleep(3)

