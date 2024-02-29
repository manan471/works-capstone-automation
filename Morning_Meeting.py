import select
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


class Morning_Meeting_Page():
    def __init__(self, driver):
        self.driver = driver
        self.click_morning_meeting = "(//div[@class = 'MuiListItemIcon-root css-loou8w'])[1]"
        self.start_morning_meeting = "//a[text()='Start Morning Meeting']"
        self.attendance_comment = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq'])[1]"
        self.click_savenextbtn = "//button[text() = 'Save & Next']"
        self.detect_attendance = "(//div[text() = 'Attendance'])[1]"
        self.detect_kpi = "(//div[text() = 'KPIs'])[1]"
        self.click_kpi_viewbtn = "//tr[1]/td[11]/div[1]/button[1]"
        self.kpi_comment = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq'])[1]"
        self.crossbtn = "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-edgeEnd MuiIconButton-sizeSmall css-cmu32z']"
        self.detectnew_sale = "//div[@class = 'MuiGrid-root css-k3glbs']"
    def DelectNSP_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detectnew_sale))):
            return True
        else:
            return False

    def EnterAttendance_Comment(self):
        self.driver.find_element(by=By.XPATH, value=self.attendance_comment).send_keys("Late SignIn due to Traffic")
        time.sleep(2)

    def ClickKPISectionBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.kpi_comment).send_keys("Good Target achieve")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.click_kpi_viewbtn).clickl()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.crossbtn).clickl()
        time.sleep(1)




    def DelectKPIs_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_kpi))):
            return True
        else:
            return False

    def ClickSaveNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_savenextbtn).click()
        time.sleep(3)

    def ClickMorning_MeetingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_morning_meeting).click()
        time.sleep(2)

    def DelectAttendance_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_attendance))):
            return True
        else:
            return False


    def ClickStart_MeetingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.start_morning_meeting).click()
        time.sleep(2)




