import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
class SearchEngineTest(unittest.TestCase):

    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver.get("http://www.google.com")
        print("Title of the page:"+self.driver.title)
        #s = Service('D:\Soft\Python_Selenium\Browser\chromedriver.exe')
        #self.driver = webdriver.Chrome(service=s)
        #self.driver.get("http://www.google.com")
        #print("Title of the page:" + self.driver.title)
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()


