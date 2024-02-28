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
from page_imarat import Imarat_Page


class WorksApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://imaratdev.propsure.rocks/login")
        cls.driver.implicitly_wait(10)
    def test_Worksapp_A(self):
        driver = self.driver
        login = Login_Page(driver)
        driver = self.driver
        imarat = Imarat_Page(driver)
        imarat.EnterEmail("admin@propsure.rocks")
        imarat.EnterPassword("12345678")
        imarat.ClickloginBtn()
        imarat.ClickBooking()
        imarat.ClickAllBooking()
        imarat.ClickIconBtn()
        imarat.ClickEditBtn()
        imarat.EnterPaymentType()
        time.sleep(1)
        imarat.EnterPaymentMode()
        time.sleep(1)
        imarat.EnterOfficeLocation()
        time.sleep(1)
        imarat.EnterPayment()
        time.sleep(1)
        imarat.EnterBank()
        time.sleep(1)
        imarat.EnterTransactionDate()
        time.sleep(1)
        imarat.EnterTexAmount()
        time.sleep(2)
        imarat.ClickSaveBtn()
        time.sleep(3)
        imarat.ClickBooking()
        imarat.ClickAllBooking()


