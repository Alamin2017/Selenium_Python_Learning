import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
time.sleep(5)
driver.quit()
