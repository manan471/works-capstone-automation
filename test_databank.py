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
# import allure

from Morning_Meeting import Morning_Meeting_Page
from page_Login import Login_Page
from Page_DataBank import DataBank_Page


# py
class WorksApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://worksapp.propsure.rocks/")
        cls.driver.implicitly_wait(10)

    # @allure.story("worksapp login")
    # @allure.description("verify worksapp login...")
    def test_Worksapp_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(1)
        login.EnterEmail('mani.shah@gmail.com')
        login.EnterPassword('12345678')
        time.sleep(1)
        self.check = login.ClickLoginBtn()
        if self.check == True:
            self.assertFalse(True, msg="Test_01:Verify WorksApp login failed with valid email & password")
        else:
            print("Test_01: Verify WorksApp login Successfully with valid email & password")

    def test_Worksapp_B(self):
        driver = self.driver
        login = Login_Page(driver)
        databank = DataBank_Page(driver)
        databank.ClickDataBank()
        time.sleep(2)
        databank.ClickFilter()
        time.sleep(2)
        databank.ClickAddBtn()
        time.sleep(2)
        databank.EnterFName('manan')
        time.sleep(1)
        databank.EnterLname('Abbasi')
        time.sleep(1)
        databank.EnterPhone("3105889104")
        time.sleep(1)
        databank.ClickSaveBtn()
        time.sleep(2)
        databank.ClickDataBankListing()
        time.sleep(2)
        self.check = databank.DelectDataBank()
        if self.check == True:
            print("Test_02:Verify DataBank Create lead Successfully...")
        else:
            self.assertFalse(True, msg="Test_02:Verify DataBank Not Create lead Successfully...")


    def test_Worksapp_C(self):
        driver = self.driver
        login = Login_Page(driver)
        databank = DataBank_Page(driver)
        databank.ClickDataBankListing()
        time.sleep(5)


