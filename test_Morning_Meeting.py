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

from Morning_Meeting import Morning_Meeting_Page
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
        time.sleep(2)
        login.EnterEmail('saif@gmail.com')
        login.EnterPassword('12345678')
        time.sleep(2)
        self.check = login.ClickLoginBtn()
        if self.check == True:
            self.assertFalse(True, msg="Test_01:Verify WorksApp login failed with valid email & password")
        else:
            print("Test_01: Verify WorksApp login Successfully with valid email & password")

    def test_Worksapp_B(self):
        driver = self.driver
        login = Login_Page(driver)
        meeting = Morning_Meeting_Page(driver)
        time.sleep(2)
        meeting.ClickMorning_MeetingBtn()
        time.sleep(2)
        # meeting.ClickStart_MeetingBtn()
        time.sleep(2)
        self.check = meeting.DelectAttendance_Section()
        if self.check == True:
            print("Test_02: Verify WorksApp meeting Attendance Section has been Display Successfully")
        else:
            self.assertFalse(True, msg="Test_02:Verify WorksApp meeting Attendance Section has not been Display Successfully")

    def test_Worksapp_C(self):
        driver = self.driver
        login = Login_Page(driver)
        meeting = Morning_Meeting_Page(driver)
        time.sleep(2)
        meeting.EnterAttendance_Comment()
        time.sleep(2)
        meeting.ClickSaveNextBtn()
        time.sleep(2)
        self.check = meeting.DelectKPIs_Section()
        if self.check == True:
            print("Test_03: Verify WorksApp meeting KFI Section has been Display Successfully")
        else:
            self.assertFalse(True, msg="Test_03:Verify WorksApp meeting KFI Section has not been Display Successfully")
        time.sleep(4)

    def test_Worksapp_D(self):
        driver = self.driver
        login = Login_Page(driver)
        meeting = Morning_Meeting_Page(driver)
        meeting.ClickKPISectionBtn()
        time.sleep(2)
        meeting.ClickSaveNextBtn()
        time.sleep(2)
        self.check = meeting.DelectNSP_Section()
        if self.check == True:
            print("Test_04: Verify WorksApp meeting NSP Section has been Display Successfully")
        else:
            self.assertFalse(True, msg="Test_04:'Verify WorksApp meeting' NSP Section has not been Display Successfully")
        time.sleep(5)





        #
        # meeting.ClickSaveNextBtn()
        # self.check =meeting.DelectAttendance_Section()
        # if self.check == True:
        #     self.assertFalse(True, msg="Test_02:Verify WorksApp meeting Attendance Section has been Display Successfully")
        # else:
        #     print("Test_02: Verify WorksApp meeting Attendance Section has not been Display Successfully")
        #





