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
        self.click_filter = "(//div[@class = 'MuiBox-root css-0'])[4]"
        self.click_addbtn = "//span[text() = 'Add']"
        self.fname =  "first_name"
        self.lname = "last_name"
        self.phone = "phone"
        self.click_save_btn = "//button[text() = 'Save']"
        self.click_databanklisting = "(//div[@class = 'MuiBox-root css-4rvh5i'])[1]"



    def ClickDataBankListing(self):
        self.driver.find_element(by=By.XPATH,value= self.click_databanklisting).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//div[@class = 'MuiBox-root css-0'])[6]").click()
        time.sleep(2)


    def ClickDataBank(self):
        self.driver.find_element(by=By.XPATH,value= self.click_data_bank).click()
        time.sleep(2)

    def ClickFilter(self):
        self.driver.find_element(by=By.XPATH, value=self.click_filter).click()
        time.sleep(2)

    def ClickAddBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_addbtn).click()
        time.sleep(2)

    def EnterFName(self):
        self.driver.find_element(by=By.NAME, value=self.fname).send_keys("Manan")
        time.sleep(2)

    def EnterLname(self):
        self.driver.find_element(by=By.NAME, value=self.lname).send_keys("Test")
        time.sleep(2)

    def EnterPhone(self):
        self.driver.find_element(by=By.NAME, value=self.phone).send_keys("3105889183")
        time.sleep(2)


    def ClickSaveBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_save_btn).click()
        time.sleep(2)



