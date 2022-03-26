import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

source=driver.find_element(By.XPATH, "//div[@id='draggable']")
target=driver.find_element(By.XPATH, "//div[@id='droppable']")

actions =ActionChains(driver)
actions.drag_and_drop(source,target).perform()
