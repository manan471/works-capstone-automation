import unittest

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


class Imaratportal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://worksapp.propsure.rocks/")

    def test_worksapp_A(self):
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value="email").send_keys("manan.abbasi@staging.rocks")
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="password").send_keys("12345678")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[text() = 'Login']").click()
        time.sleep(2)
        self.check = self.driver.current_url
        if "today" not in  self.check:
            print("Test_1:login Successful...")
        else:
            self.assertFalse(True, msg="login failed...")

    def test_worksapp_B(self):
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add Lead']").click()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="first_name").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="last_name").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="phone").send_keys(
            ''.join(random.choice(string.digits) for i in range(10)))
        time.sleep(3)
        try:
            self.driver.find_element(by=By.XPATH, value="//button[text() = 'Save']").click()
            print("Test_2: lead has been created successfully")
        except:
            self.assertFalse(True, msg="lead has not  been created")




    def test_worksapp_C(self):
        for i in range(10):
            self.driver.refresh()
            self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add']").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add Lead']").click()
            time.sleep(2)
            self.driver.find_element(by=By.NAME, value="first_name").send_keys(
                ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            time.sleep(2)
            self.driver.find_element(by=By.NAME, value="last_name").send_keys(
                ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            time.sleep(1)
            self.driver.find_element(by=By.NAME, value="phone").send_keys(
                ''.join(random.choice(string.digits) for i in range(10)))
            time.sleep(3)
            try:
                self.driver.find_element(by=By.XPATH, value="//button[text() = 'Save']").click()
                print("Test_3: lead has been created successfully")
            except:
                self.assertFalse(True, msg="lead has not  been created")



    def test_worksapp_D(self):
        self.driver.refresh()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add Client']").click()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="first_name").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="last_name").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="phone").send_keys(
            ''.join(random.choice(string.digits) for i in range(10)))
        try:
            self.driver.find_element(by=By.XPATH, value="//button[text() = 'Save']").click()
            print("Test_4: Client has been created successfully")
        except:
            self.assertFalse(True, msg="Client has not  been created")

    def test_worksapp_E(self):
        for i in range(1):
            self.driver.refresh()
            self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add']").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value="//p[text() = 'Add Client']").click()
            time.sleep(2)
            self.driver.find_element(by=By.NAME, value="first_name").send_keys(
                ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            time.sleep(2)
            self.driver.find_element(by=By.NAME, value="last_name").send_keys(
                ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            time.sleep(1)
            self.driver.find_element(by=By.NAME, value="phone").send_keys(
                ''.join(random.choice(string.digits) for i in range(10)))
            try:
                self.driver.find_element(by=By.XPATH, value="//button[text() = 'Save']").click()
                print("Test_5: Client has been created successfully")
            except:
                self.assertFalse(True, msg="Client has not  been created")


    def test_worksapp_F(self):
        for i in range(2):
            self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div/div/div/ul/li/div/div/img[1]").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value="(//td[@class = 'fc-timegrid-slot fc-timegrid-slot-lane fc-timegrid-slot-minor'])[2]").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value="//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1']").click()
            time.sleep(1)
            self.driver.find_element(by=By.XPATH,value="//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1']").send_keys(Keys.ARROW_DOWN+Keys.ENTER)
            time.sleep(5)
            try:
                try:
                    self.driver.find_element(by=By.XPATH, value="(//div[@class = 'css-1s9wqpj'])[1]").click()
                except:
                    time.sleep(2)
                # try:
                #     self.driver.find_element(by=By.XPATH, value="(//div[@class = 'css-1s9wqpj'])[2]").click()
                # except:
                #     time.sleep(2)
                # try:
                #     self.driver.find_element(by=By.XPATH, value="(//div[@class = 'css-1s9wqpj'])[3]").click()
                # except:
                #     time.sleep(2)
            except:
                time.sleep(2)
            self.driver.find_element(by=By.NAME, value="desc").send_keys("testing")
            time.sleep(1)
            self.driver.find_element(by=By.NAME, value="done").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value="//button[text() = 'Save']").click()
            time.sleep(10)








