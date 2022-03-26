import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
#driver.save_screenshot("D:\Soft\Python_Selenium\Browser\lamin.png")
driver.get_screenshot_as_file("D:\Soft\Python_Selenium\Browser\lamin.png")