import sys
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append('PYTHONPROJECTS/kylepom/')
sys.path.insert(0,"C:\\Users\\kylem\\OneDrive\\Documents\\pythonProjects\\kylepom\\")

import unittest
from time import sleep
from TestBase.WebDriverSetup import WebDriverSetup
from PageObject.Pages.Home_Page import Home
from PageObject.Pages.Results_Page import Results
from PageObject.Pages.lambda_home import Lambda

class Google_Search(WebDriverSetup):
    def test_GoogleSearch(self):
        driver = self.driver
        self.driver.get("http://www.google.com")
        self.driver.set_page_load_timeout(30)

        #Create an instance of the class so that you can make use of the methods in the class
        home = Home(driver)
        home.search_text.send_keys("LambdaTest")
        sleep(2)
        home.search_text.submit()
        sleep(2)
        result = Results(driver)
        result.first_result.click()
        sleep(2)
        lamb = Lambda(driver)
        lamb.platform.click()
        Hover = ActionChains(driver).move_to_element(lamb.online_browser_testing)
        Hover.click()
        sleep(10)
        assert(driver.current_url == "https://www.lambdatest.com/online-browser-testing")
        lamb.lambda_home.click()
        sleep(10)
        assert(driver.current_url == "https://www.lambdatest.com/")
        sleep(10000)
        lamb.enterprise.click()
        assert(driver.current_url == "https://www.lambdatest.com/enterprise")
        sleep(2)
        lamb.home.click()
        sleep(2)
        lamb.pricing.click()
        assert(driver.current_url == "https://www.lambdatest.com/pricing")
        sleep(2)


if __name__ == "__main__":
    unittest.main()

