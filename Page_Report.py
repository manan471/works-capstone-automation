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


class Report_Page():
    def __init__(self, driver):
        self.driver = driver
        self.report = "//span[text() = 'Reports']"
        self.bcm_report = "(//button[@class = 'MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-11v4c96'])[1]"
        self.select_user = "//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1uvydh2']"
        self.submitbtn = "(//div[@class = 'MuiBox-root css-8weyt0'])[2]"
        self.downloadcsv = "//a[text() = 'Download CSV']"

    def Click_CSVDownload(self):
        self.driver.find_element(by=By.XPATH, value=self.downloadcsv).click()
        time.sleep(2)
    def Click_Report(self):
        self.driver.find_element(by=By.XPATH, value=self.report).click()
        time.sleep(2)

    def Click_BCMReport(self):
        self.driver.find_element(by=By.XPATH,value=self.bcm_report).click()
        time.sleep(2)
    def Click_SelectUser(self):
        self.driver.find_element(by=By.XPATH, value=self.select_user).send_keys(Keys.ARROW_DOWN + 'manan' + Keys.ENTER)
        time.sleep(2)

    def ClickSubmitBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.submitbtn).click()
        time.sleep(2)

