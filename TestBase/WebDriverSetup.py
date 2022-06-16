import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import InsecureRequestWarning


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(InsecureRequestWarning)
        options = Options()
        # options.binary_location = r'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
        options.binary_location = r'C:\\Program Files (x86)\\Google\\Chrome\Application\\chrome.exe'
        # self.driver = webdriver.Firefox(executable_path=r'C:\SeleniumDrivers\\geckodriver.exe', options=options)
        self.driver = webdriver.Chrome(executable_path='C:\SeleniumDrivers\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'https://go.playerzero.ai/record/6274691b00fbad01561df689'})



    def tearDown(self):
        if(self.driver != None):
            
            self.driver.close()
            self.driver.quit()

