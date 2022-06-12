import sys
sys.path.insert(0,"C:\\Users\\kylem\\OneDrive\\Documents\\playerzero_python")
import os
from selenium.webdriver.common.by import By

class Lambda(object):
    def __init__ (self, driver):
        self.driver = driver
        self.lambda_home = driver.find_element(By.XPATH, '//*[@href="https://www.lambdatest.com"]')
        self.platform = driver.find_element(By.XPATH, '//*[@href="https://www.lambdatest.com/feature"]')
        self.enterprise = driver.find_element(By.XPATH, '//*[@href="https://www.lambdatest.com/enterprise"]')
        self.pricing = driver.find_element(By.XPATH, '//*[@href="https://www.lambdatest.com/pricing"]')
        self.login = driver.find_element(By.XPATH, '//*[@href="https://accounts.lambdatest.com/login"]')
        self.free_testing = driver.find_element(By.XPATH, '//*[@href="https://accounts.lambdatest.com/register"]')
        self.online_browser_testing = driver.find_element(By.CLASS_NAME, 'ml-26')
    

    def get_home(self):
        return self.lambda_home

    def get_platform(self):
        return self.platform

    def get_enterprise(self):
        return self.enterprise

    def get_resources(self):
        return self.resources

    def get_developers(self):
        return self.developers

    def get_pricing(self):
        return self.pricing

    def get_login(self):
        return self.login
    
    def get_free_testing(self):
        return self.free_testing

    def get_contact_us(self):
        return self.contact_us

    def get_book_demo(self):
        return self.book_demo