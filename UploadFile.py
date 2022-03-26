from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.switch_to.frame("frame-one1434677811")
upload=driver.find_element(By.ID, "RESULT_FileUpload-10")
upload.location_once_scrolled_into_view
upload.send_keys("F:\Govt_job_Others\Al-Amin.jpg")
print("IMG photo uploaded properly")
