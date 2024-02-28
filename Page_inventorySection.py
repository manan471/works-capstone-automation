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


class Inventory_Page():
    def __init__(self, driver):
        self.driver = driver
        self.click_inventorybtn = "(//div[@class='MuiButtonBase-root MuiListItemButton-root MuiListItemButton-gutters MuiListItemButton-root MuiListItemButton-gutters css-ygn1ae']//a)[5]"
        self.click_installment = "//p[text() = 'INSTALLMENT']"
        self.click_bestinvestment = "//p[text() = 'Best Investment']"
        self.click_rental = "//p[text() = 'Best Investment']"

    def ClickInventoryBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_inventorybtn).click()
        time.sleep(2)

    def ClickInstalllmentSection(self):
        self.driver.find_element(by=By.XPATH, value=self.click_installment).click()
        time.sleep(2)

    def ClickBestInvestment(self):
        self.driver.find_element(by=By.XPATH, value=self.click_bestinvestment).click()
        time.sleep(2)

    def ClickRental(self):
        self.driver.find_element(by=By.XPATH, value=self.click_rental).click()
        time.sleep(1)

