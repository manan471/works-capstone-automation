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


class DataBank_Page():
    def __init__(self, driver):
        self.driver = driver
        self.click_data_bank = "//img[@alt='Data Bank']"
        self.click_filter = "//div[@class = 'MuiBox-root css-troior']"
        self.click_addbtn = "//span[text() = 'Add']"
        self.fname =  "first_name"
        self.lname = "last_name"
        self.phone = "phone"
        self.click_save_btn = "(//span[@class = 'MuiBox-root css-whh5e5'])[2]"
        self.click_databanklisting = "(//div[@class = 'MuiBox-root css-16u8gzp'])[1]"
        self.detect_databank = "//div[@class = 'MuiBox-root css-18ja1pm']"



    def ClickDataBankListing(self):
        self.driver.find_element(by=By.XPATH,value= self.click_databanklisting).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="(//div[@class = 'MuiBox-root css-0'])[5]").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="(//span[@class = 'MuiBox-root css-whh5e5'])[2]").click()
        time.sleep(2)



    def ClickDataBank(self):
        self.driver.find_element(by=By.XPATH,value= self.click_data_bank).click()
        time.sleep(1)

    def ClickFilter(self):
        self.driver.find_element(by=By.XPATH, value=self.click_filter).click()
        time.sleep(1)

    def ClickAddBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_addbtn).click()
        time.sleep(1)

    def EnterFName(self,fname):
        self.driver.find_element(by=By.NAME, value=self.fname).send_keys(fname)
        time.sleep(1)

    def EnterLname(self,lname):
        self.driver.find_element(by=By.NAME, value=self.lname).send_keys(lname)
        time.sleep(1)

    def EnterPhone(self,phone_number):
        self.driver.find_element(by=By.NAME, value=self.phone).send_keys(phone_number)
        time.sleep(2)


    def ClickSaveBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_save_btn).click()
        time.sleep(1)


    def DelectDataBank(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_databank))):
            return True
        else:
            return False




