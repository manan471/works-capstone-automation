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
        self.click_kpi_viewbtn = "(//td[@class = 'MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft MuiTableCell-sizeMedium css-12u4bxb'])[11]"
        self.kpi_comment = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq'])[1]"
        self.crossbtn = "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-edgeEnd MuiIconButton-sizeSmall css-cmu32z']"
        self.detectnew_sale = "//div[@class = 'MuiGrid-root css-k3glbs']"
        self.newsale_comment = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq'])[9]"
        self.detect_pending = "//div[@class = 'MuiGrid-root css-k3glbs']"
        self.recovery_comment = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq'])[3]"
        self.detect_recovery = "//div[@class = 'MuiGrid-root css-k3glbs']"
        self.pending_comment = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq'])[3]"
        self.detect_review = "(//div[@class = 'MuiGrid-root css-k3glbs'])[1]"
        self.finishbtn = "//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textInherit MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorInherit MuiButton-root MuiButton-text MuiButton-textInherit MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorInherit css-1xdrykt']"


    def Click_FinishBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.finishbtn).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-18muvbq']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-1jq3me9']").click()

    def DelectReview_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_review))):
            return True
        else:
            return False


    def EnterRecovery_Comment(self):
        self.driver.find_element(by=By.XPATH, value=self.recovery_comment).send_keys("Late SignIn due to Traffic")
        time.sleep(1)



    def EnterPending_Comment(self):
        self.driver.find_element(by=By.XPATH, value=self.pending_comment).send_keys("Late SignIn due to Traffic")
        time.sleep(1)


    def DelectRecovery_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_recovery))):
            return True
        else:
            return False



    def EnterPending_Comment(self):
        self.driver.find_element(by=By.XPATH, value=self.pending_comment).send_keys("Late SignIn due to Traffic")
        time.sleep(1)



    def DelectPanding_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_pending))):
            return True
        else:
            return False

    def EnterNewSale_Comment(self):
        self.driver.find_element(by=By.XPATH, value=self.newsale_comment).send_keys("Late SignIn due to Traffic")
        time.sleep(1)

    def DelectNSP_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detectnew_sale))):
            return True
        else:
            return False

    def EnterAttendance_Comment(self):
        self.driver.find_element(by=By.XPATH, value=self.attendance_comment).send_keys("Late SignIn due to Traffic")
        time.sleep(1)

    def ClickKPISectionBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.kpi_comment).send_keys("Good Target achieve")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.click_kpi_viewbtn).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.crossbtn).click()
        time.sleep(1)




    def DelectKPIs_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_kpi))):
            return True
        else:
            return False

    def ClickSaveNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_savenextbtn).click()
        time.sleep(1)

    def ClickMorning_MeetingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_morning_meeting).click()
        time.sleep(1)

    def DelectAttendance_Section(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_attendance))):
            return True
        else:
            return False


    def ClickStart_MeetingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.start_morning_meeting).click()
        time.sleep(1)




