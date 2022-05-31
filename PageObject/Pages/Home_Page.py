import sys
sys.path.insert(0,"C:\\Users\\kylem\\OneDrive\\Documents\\pythonProjects\\kylepom\\")
import os
# uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By

class Home(object):
    def __init__(self, driver): #important to initiate driver for each page object:
        self.driver = driver
        self.logo = driver.find_element(By.CLASS_NAME, 'lnXdpd')
        self.search_text = driver.find_element(By.NAME, 'q')
        self.submit = driver.find_element(By.NAME, 'btnK')

    def getSearchText(self):
        return self.search_text

    def getSubmit(self):
        return self.submit

    def getWebPageLogo(self):
        return self.logo