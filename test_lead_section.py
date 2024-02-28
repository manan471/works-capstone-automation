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
from page_Login import Login_Page
from Page_Lead import Lead_Page



class WorksApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://worksapp.com.pk/")
        cls.driver.implicitly_wait(10)

    def test_Worksapp_A(self):
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        login.EnterEmail("manan@worksapp.com.pk")
        login.EnterPassword("12345678")
        login.ClickLoginBtn()
        time.sleep(4)
        lead.ClickAddBtn()
        lead.ClickAddLeadBtn()
        time.sleep(2)
        firstname = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        lastname = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        time.sleep(3)
        lead.EnterFName(firstname)
        lead.EnterLName(lastname)
        for i in range(10):
            phone = str(random.randint(1, 9))
            lead.EnterPhoneNo(phone)
            lead.ClickCity()
            time.sleep(1)
            lead.ClickProject()
            # lead.ClickProductType()
            # lead.ClickCampaignSource()
            # lead.ClickCampaign()
            lead.EnterValue("5000")
            lead.ClickSaveBtn()
            self.check = lead.VarifyAddLead()
            if self.check == True:
                print("Test_03  :Verify WorksApp Lead has been Create successfully")
            else:
                self.assertFalse(True, msg="Test_03: Verify WorksAppWorksApp Lead has not been Create")
            time.sleep(3)

    def test_Worksapp_B(self):
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        self.driver.refresh()
        for i in range(20):
            lead.ClickAddBtn()
            lead.ClickAddLeadBtn()
            time.sleep(2)
            firstname = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            lastname = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            time.sleep(3)
            lead.EnterFName(firstname)
            lead.EnterLName(lastname)
            for i in range(10):
                phone = str(random.randint(1, 9))
                lead.EnterPhoneNo(phone)
            lead.ClickCity()
            time.sleep(1)
            lead.ClickProject()
            # lead.ClickProductType()
            # lead.ClickCampaignSource()
            # lead.ClickCampaign()
            lead.EnterValue("5000")
            lead.ClickSaveBtn()
            self.check = lead.VarifyAddLead()
            if self.check == True:
                print("Test_03  :Verify WorksApp Lead has been Create successfully")
            else:
                self.assertFalse(True, msg="Test_03: Verify WorksAppWorksApp Lead has not been Create")
            time.sleep(3)














