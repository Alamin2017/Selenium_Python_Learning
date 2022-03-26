from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/Windows.html')
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()

print(driver.current_window_handle)

handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Selenium":
        driver.close()


driver.quit()
