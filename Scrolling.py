from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
driver.get('https://getflags.net/')
driver.maximize_window()
# driver.execute_script("window.scrollBy(0,2000)")

flag = driver.find_element(By.XPATH,"//img[@title='State flag of Japan']")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
