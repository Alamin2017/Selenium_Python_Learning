from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()

button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
actions=ActionChains(driver)
actions.context_click(button).perform()
