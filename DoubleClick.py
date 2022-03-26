from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
doubleclick=driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
actions=ActionChains(driver)
actions.double_click(doubleclick).perform()

