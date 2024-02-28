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
from Page_Lead import Lead_Page
from Page_inventorySection import Inventory_Page
from Page_Report import Report_Page


class WorksApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://worksapp.propsure.rocks/")
        cls.driver.implicitly_wait(10)
    def test_Worksapp_A(self):

        driver = self.driver
        report = Report_Page(driver)
        login = Login_Page(driver)
        login.EnterEmail("manan.abbasi@staging.rocks")
        login.EnterPassword('12345678')
        login.ClickLoginBtn()
        time.sleep(4)
        report.Click_Report()
        report.Click_BCMReport()
        report.Click_SelectUser()
        report.ClickSubmitBtn()
        time.sleep(10)
