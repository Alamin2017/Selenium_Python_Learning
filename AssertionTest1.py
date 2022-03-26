import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver.get("http://www.google.com")
        titleofwebpage= self.driver.title
        #self.assertEqual("Google",titleofwebpage,"webpage title is not same")
        self.assertNotEqual("Google123", titleofwebpage, "webpage title is not same")


if __name__ == "__main__":
    unittest.main()
