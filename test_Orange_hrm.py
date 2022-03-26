from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_HomePage(self,driver):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title=="OrangeHRM"
    def test_login(self,setup):
        self.driver.find_element(By.ID,"txtUsername").clear().send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").clear().send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        assert self.driver.title=="OrangeHRM"


