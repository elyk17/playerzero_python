import sys
sys.path.append(sys.path[0] + "/....")
sys.path.insert(0,"C:\\Users\\kylem\\OneDrive\\Documents\\pythonProjects\\kylepom\\")
from TestBase.WebDriverSetup import WebDriverSetup
from PageObject.Pages.Home_Page import Home
import unittest
from selenium import webdriver

class Google_HomePage(WebDriverSetup):
    def test_Home_Page(self):
        driver = self.driver
        self.driver.set_page_load_timeout(30)

        web_page_title = "Google"

        try:
            if driver.title == web_page_title:
                print("Webpage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "Webpage failed to load")

        home_page = Home(driver)

if __name__ == "__main__":
    unittest.main()