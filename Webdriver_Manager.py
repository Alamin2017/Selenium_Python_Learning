from selenium import webdriver

from selenium import webdriver

browser = "firefox"

if browser == "chrome":
    driver = webdriver.Chrome(executable_path='D:\Soft\Python_Selenium\Browser\chromedriver.exe')
elif browser == "firefox":
    driver = webdriver.Firefox(executable_path='D:\Soft\Python_Selenium\Firefox\geckodriver.exe')
elif browser == "edge":
    driver = webdriver.Edge(executable_path='D:\Soft\Python_Selenium\Edge\msedgedriver.exe')
else:
    print("please pass the correct browser name:" + browser)

driver.get("https://www.facebook.com/")
