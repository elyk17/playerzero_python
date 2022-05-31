import sys
sys.path.insert(0,"C:\\Users\\kylem\\OneDrive\\Documents\\pythonProjects\\kylepom\\")
import os
from selenium.webdriver.common.by import By

class Results(object):
    def __init__(self, driver):
        self.driver = driver
        self.first_result = driver.find_element(By.CLASS_NAME, "yuRUbf")

        def get_first_result(self):
            return self.first_result