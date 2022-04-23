import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
#python -m pytest test_orangehrm.py --alluredir="C:\Users\User\PycharmProjects\SeleniumPython\allurereportsdemo\reports"

#cmd command line for generating report
#allure serve C:\Users\User\PycharmProjects\SeleniumPython\allurereportsdemo\reports

#python -m pytest allurereportsdemo\test_orangehrm.py
@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver=webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element(By.XPATH,"//div[@id='divLogo']/img").is_displayed()
        if status==True:
            assert True
        else:
            assert False

        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping test..later i will implement")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver=webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(3)
        self.driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)

        act_title=self.driver.title

        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)

            self.driver.close()
            assert False








