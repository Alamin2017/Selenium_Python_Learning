from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()

admin=driver.find_element(By.XPATH, "//b[normalize-space()='Admin']")

actions=ActionChains(driver)
actions.move_to_element(admin).perform()

usermgs=driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")
actions.move_to_element(usermgs).perform()

user=driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")
actions.move_to_element(user).click().perform()
