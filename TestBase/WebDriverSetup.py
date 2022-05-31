from pickle import APPEND
import unittest
from xml.dom.minidom import Document
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
from urllib3.exceptions import InsecureRequestWarning


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = Options()
        # options.binary_location = r'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
        options.binary_location = r'C:\\Program Files (x86)\\Google\\Chrome\Application\\chrome.exe'
        # self.driver = webdriver.Firefox(executable_path=r'C:\SeleniumDrivers\\geckodriver.exe', options=options)
        self.driver = webdriver.Chrome(executable_path='C:\SeleniumDrivers\\chromedriver.exe')
        self.driver.maximize_window()
        window = self.driver.window_handles[0]
        document  = Document()
        head = document.getElementsByTagName('head')
        script = document.createElement('script')
        setattr(script,"type", "text/javascript")
        setattr(script, 'src', "https://go.playerzero.ai/record/6274691b00fbad01561df689")
        window.append(script)


    def tearDown(self):
        if(self.driver != None):
            window = self.driver.window_handles[0]
            string = window.playerzero.session()
            print(string)
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()

