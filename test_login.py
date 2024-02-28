import unittest
from datetime import datetime
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
from page_Login import Login_Page

class WorksApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://worksapp.propsure.rocks/")
        cls.driver.implicitly_wait(10)


    def test_Worksapp_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(4)
        login.EnterEmail('')
        login.EnterPassword('123456789')
        self.check = login.ClickLoginBtn()
        if self.check == True:
            self.assertFalse(True, msg="Test_01:Verify WorksApp login Successfully with invalid email")
        else:
            print("Test_01: Verify WorksApp login failed with invalid email")

    def test_Worksapp_B(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(1)
        login.EnterEmail('advisor@imarat.com')
        login.EnterPassword('')
        self.check = login.ClickLoginBtn()
        if self.check == True:
            self.assertFalse(True, msg="Test_02: Verify WorksApp login Successfully with invalid password")
        else:
            print("Test_02:Verify WorksApp login failed with invalid password")

    def test_Worksapp_C(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        login.EnterEmail('advisor@imarat.com')
        login.EnterPassword('123456789')
        login.ClickLoginBtn()
        self.check = login.DetectloginPage()
        if self.check == True:
            print("Test_03:Verify WorksApp login page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify WorksApp login failed")




