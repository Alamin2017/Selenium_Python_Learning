from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"HasCapabilities").click()