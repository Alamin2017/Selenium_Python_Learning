import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.webdriver import WebDriver

# s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
from selenium.webdriver.support.select import Select

s = Service("D:\Soft\Python_Selenium\Edge\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(3)
createaccount=driver.find_element(By.XPATH,"//a[text()='Create New Account']")
createaccount.click()

driver.find_element(By.XPATH,"//*[@name='firstname']").send_keys("Alamin")
driver.find_element(By.XPATH,"//*[@name='lastname']").send_keys("Ahmed")
driver.find_element(By.XPATH,"//*[@name='reg_email__']").send_keys("01746642952")
driver.find_element(By.XPATH,"//input[@name='reg_passwd__']").send_keys("alamin12")

date=driver.find_element(By.XPATH,"//select[@name='birthday_day']")
drp = Select(date)
drp.select_by_visible_text("24")

month=driver.find_element(By.XPATH,"//select[@name='birthday_month']")
drp1 = Select(month)
drp1.select_by_visible_text("May")

year=driver.find_element(By.XPATH,"//select[@name='birthday_year']")
drp2 = Select(year)
drp2.select_by_visible_text("1995")




