import unittest
from datetime import datetime
# import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import os
import openpyxl



class WorksApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://worksapp.propsure.rocks/")
        cls.driver.implicitly_wait(10)

    def test_Worksapp_A(self):
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="").send_keys("advisor@imarat.com")
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="").send_keys("12345678")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="").click()
        time.sleep(2)


