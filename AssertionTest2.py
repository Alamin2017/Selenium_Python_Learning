import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver.get("http://www.google.com")
        titleofwebpage= self.driver.title
        self.assertIsNotNone(titleofwebpage == 'Google123')


if __name__ == "__main__":
    unittest.main()
