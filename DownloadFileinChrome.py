import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

driver.find_element(By.ID, "textbox").send_keys("testNG file text")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()
time.sleep(3)
driver.find_element(By.ID, "pdfbox").send_keys("testNG pdf file ")
driver.find_element(By.ID, "createPdf").click()
driver.find_element(By.ID, "pdf-link-to-download").click()
