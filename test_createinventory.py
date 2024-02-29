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
        cls.driver.get("http://imaratdev.propsure.rocks/")


    def test_search_imarat_A(self):

        self.driver.find_element(by=By.NAME, value="email").send_keys("admin@propsure.rocks")
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="password").send_keys("12345678")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//button[@type='submit'][@class='btn btn-success w-100']").click()
        time.sleep(2)
        # self.check = self.driver.current_url
        # if "dashboard" not in self.check:
        #     self.assertFalse(True, msg="login failed...")
        # else:
        #     print("Test_1:login Successful...")


    def test_search_imarat_B(self):
        time.sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value="Inventory").click()
        time.sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value="Create inventory").click()

    def test_search_imarat_C(self):
        time.sleep(1)
        self.Project = [1]
        Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_index(random.choice(self.Project))
        time.sleep(1)
        self.Floor = [1]
        Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
        time.sleep(1)
        self.Company = [0]
        Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="inventory_code").send_keys(''.join(random.choice(string.digits) for i in range(4)))
        time.sleep(2)
        self.Design = [1,2,3,4,5]
        Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
        time.sleep(1)
        self.View = [1,2,3,4,5]
        Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
        time.sleep(1)
        self.Inventory = [1,2,3,4,5]
        Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(2)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(5)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="tower").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)
        # self.Planning = [1]
        # Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
        # time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.ProductType = ['Only Rental']
        self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(random.choice(self.ProductType) + Keys.ENTER)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
        time.sleep(6)
        # self.check = self.driver.current_url
        # if "create" not in self.check:
        #     self.driver.back()
        #     time.sleep(1)
        #     print("Inventory Created With rental project")
        #
        # else:
        #     self.assertFalse(True, msg="Inventory not Created With rental project")

    def test_search_imarat_D(self):
        time.sleep(6)
        self.driver.find_element(by=By.LINK_TEXT, value="Inventory").click()
        time.sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value="Create inventory").click()



    def test_search_imarat_E(self):
        self.driver.refresh()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        self.Project = [2]
        Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_index(random.choice(self.Project))
        time.sleep(1)
        self.Floor = [1]
        Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
        time.sleep(1)
        self.Company = [0]
        Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="inventory_code").send_keys(''.join(random.choice(string.digits) for i in range(4)))
        time.sleep(2)
        self.Design = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
        time.sleep(1)
        self.View = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
        time.sleep(1)
        self.Inventory = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(
            random.choice(self.Inventory))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
            ''.join(random.choice(string.digits) for i in range(2)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
            ''.join(random.choice(string.digits) for i in range(5)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="tower").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)
        # self.Planning = [1]
        # Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.ProductType = ['Only Rental FG']
        self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
            random.choice(self.ProductType) + Keys.ENTER)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
        time.sleep(1)

    def test_search_imarat_F(self):
        time.sleep(6)
        self.driver.find_element(by=By.LINK_TEXT, value="Inventory").click()
        time.sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value="Create inventory").click()
    def test_search_imarat_G(self):
        self.driver.refresh()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        self.Project = [3]
        Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_index(random.choice(self.Project))
        time.sleep(1)
        self.Floor = [1]
        Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
        time.sleep(1)
        self.Company = [0]
        Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="inventory_code").send_keys(''.join(random.choice(string.digits) for i in range(4)))
        time.sleep(2)
        self.Design = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
        time.sleep(1)
        self.View = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
        time.sleep(1)
        self.Inventory = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(
            random.choice(self.Inventory))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
            ''.join(random.choice(string.digits) for i in range(2)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
            ''.join(random.choice(string.digits) for i in range(5)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="tower").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)
        # self.Planning = [1]
        # Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.ProductType = ['Only Rental 18%']
        self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
            random.choice(self.ProductType) + Keys.ENTER)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
        time.sleep(1)

    def test_search_imarat_H(self):
        time.sleep(6)
        self.driver.find_element(by=By.LINK_TEXT, value="Inventory").click()
        time.sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value="Create inventory").click()
    def test_search_imarat_I(self):
        self.driver.refresh()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        time.sleep(2)
        self.Project = [4]
        Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_index(random.choice(self.Project))
        time.sleep(1)
        self.Floor = [1]
        Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
        time.sleep(1)
        self.Company = [0]
        Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="inventory_code").send_keys(''.join(random.choice(string.digits) for i in range(4)))
        time.sleep(2)
        self.Design = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
        time.sleep(1)
        self.View = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
        time.sleep(1)
        self.Inventory = [1, 2, 3, 4, 5]
        Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(
            random.choice(self.Inventory))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
            ''.join(random.choice(string.digits) for i in range(2)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
            ''.join(random.choice(string.digits) for i in range(5)))
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="tower").send_keys(
            ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)
        # self.Planning = [1]
        # Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.ProductType = ['only rental 20%']
        self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
            random.choice(self.ProductType) + Keys.ENTER)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
        time.sleep(1)
def test_search_imarat_J(self):
    time.sleep(6)
    self.driver.find_element(by=By.LINK_TEXT, value="Inventory").click()
    time.sleep(2)
    self.driver.find_element(by=By.LINK_TEXT, value="Create inventory").click()
def test_search_imarat_K(self):
    self.driver.refresh()
    self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    time.sleep(2)
    self.Project = [5]
    Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_index(random.choice(self.Project))
    time.sleep(1)
    self.Floor = [1]
    Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    time.sleep(1)
    self.Company = [0]
    Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    time.sleep(1)
    self.driver.find_element(by=By.NAME, value="inventory_code").send_keys(
        ''.join(random.choice(string.digits) for i in range(4)))
    time.sleep(2)
    self.Design = [1, 2, 3, 4, 5]
    Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    time.sleep(1)
    self.View = [1, 2, 3, 4, 5]
    Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    time.sleep(1)
    self.Inventory = [1, 2, 3, 4, 5]
    Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(
        random.choice(self.Inventory))
    time.sleep(1)
    self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
        ''.join(random.choice(string.digits) for i in range(2)))
    time.sleep(1)
    self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
        ''.join(random.choice(string.digits) for i in range(5)))
    time.sleep(1)
    self.driver.find_element(by=By.NAME, value="tower").send_keys(
        ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    time.sleep(1)
    # self.Planning = [1]
    # Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))

    time.sleep(1)
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    self.ProductType = ['Only Rental 18%/RP 04/23 OR01']
    self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
        random.choice(self.ProductType) + Keys.ENTER)
    time.sleep(1)
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    self.driver.find_element(by=By.XPATH,
                             value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    time.sleep(1)

    # self.check = self.driver.current_url
        # if "create" not in self.check:
        #     self.driver.back()
        #     time.sleep(3)
        #     print("Inventory Created With only Appreciation14 project")
        #
        # else:
        #     self.assertFalse(True, msg="Inventory not Created With installment project")


    # @allure.story("Verify Inventory Creation With Invalid Design and other valid details")
    # def test_search_imarat_E(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Company = [0]
    #     #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     #time.sleep(2)
    #
    #     self.Design = [1, 2, 3, 4, 5]
    #     'Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))'
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(
    #         random.choice(self.Inventory))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
    #         ''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
    #         ''.join(random.choice(string.digits) for i in range(6)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(
    #         ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
    #         random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid Design")
    #
    #
    #     else:
    #         print("Inventory Not Created With Invalid Design")
    #
    # @allure.story("Verify Inventory Creation With Invalid View and other valid details")
    # def test_search_imarat_F(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Company = [0]
    #     #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     #time.sleep(2)
    #
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     'Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))'
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(
    #         random.choice(self.Inventory))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
    #         ''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
    #         ''.join(random.choice(string.digits) for i in range(5)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(
    #         ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
    #         random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid View")
    #
    #
    #         print("Inventory Not Created With Invalid View")
    #
    # @allure.story("Verify Inventory Creation With Invalid Inventory and other valid details")
    # def test_search_imarat_G(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Company = [0]
    #     #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     #time.sleep(2)
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     'Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))'
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(
    #         ''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(
    #         ''.join(random.choice(string.digits) for i in range(5)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(
    #         ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
    #         random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid Inventory")
    #
    #
    #     else:
    #         print("Inventory Not Created With Invalid Inventory")
    #
    # @allure.story("Verify Inventory Creation With Invalid Rate Per Sqft and other valid details")
    # def test_search_imarat_H(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Company = [0]
    #     #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     #time.sleep(2)
    #
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))
    #     time.sleep(2)
    #     'self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(2)))'
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(5)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(
    #         ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
    #         random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid rate_per_sq_ft")
    #
    #
    #     else:
    #         print("Inventory Not Created With Invalid rate_per_sq_ft")
    #
    # @allure.story("Verify Inventory Creation With Invalid Total Sqft and other valid details")
    # def test_search_imarat_I(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Company = [0]
    #     #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     #time.sleep(2)
    #
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     'self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(5)))'
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(
    #         ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
    #         random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid total_sq_ft")
    #
    #
    #     else:
    #         print("Inventory Not Created With Invalid total_sq_ft")
    #
    #
    # @unittest.SkipTest
    # @allure.story("Verify Inventory Creation With Invalid Company and other valid details")
    # def test_search_imarat_K(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(5)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Company = [1, 3, 4]
    #     'Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))'
    #     time.sleep(3)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field']").send_keys(
    #         random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid Company")
    #
    #
    #     else:
    #         print("Inventory Not Created With Invalid Company")
    #
    # @allure.story("Verify Inventory Creation With Invalid Product Type and other valid details")
    # def test_search_imarat_L(self):
    #     self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     # self.Company = [0]
    #     # #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     # #time.sleep(2)
    #
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(5)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     'self.driver.find_element(by=By.XPATH, value="//textarea[@class=select2-search__field]").send_keys(random.choice(self.ProductType) + Keys.ENTER)'
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(5)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         self.driver.back()
    #         time.sleep(8)
    #         self.assertFalse(True, msg="Inventory Created With Invalid Product Type")
    #
    #
    #     else:
    #         print("Inventory Not Created With Invalid Product Type")
    #
    # @allure.story("Verify Inventory Creation With all valid details")
    # def test_search_imarat_M(self):
    #     # self.driver.refresh()
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    #     time.sleep(15)
    #     self.Project = ["Golf Floras", "Mall of Imarat", "Multan Bavylon"]
    #     Select(self.driver.find_element(by=By.NAME, value="project_id")).select_by_visible_text(random.choice(self.Project))
    #     time.sleep(2)
    #     self.Floor = [1]
    #     Select(self.driver.find_element(by=By.NAME, value="floor_id")).select_by_index(random.choice(self.Floor))
    #     time.sleep(2)
    #     self.Company = [0]
    #     #Select(self.driver.find_element(by=By.NAME, value="owner_id")).select_by_index(random.choice(self.Company))
    #     #time.sleep(2)
    #
    #     self.Design = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="design_type_id")).select_by_index(random.choice(self.Design))
    #     time.sleep(2)
    #     self.View = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="category_view_id")).select_by_index(random.choice(self.View))
    #     time.sleep(2)
    #     self.Inventory = [1, 2, 3, 4, 5]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_type")).select_by_index(random.choice(self.Inventory))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="rate_per_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(2)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="total_sq_ft").send_keys(''.join(random.choice(string.digits) for i in range(5)))
    #     time.sleep(2)
    #     self.driver.find_element(by=By.NAME, value="tower").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
    #     time.sleep(2)
    #     self.Planning = [1, 2]
    #     Select(self.driver.find_element(by=By.NAME, value="inventory_planning")).select_by_index(random.choice(self.Planning))
    #
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(3)
    #     self.ProductType = ['Low Rental']
    #     self.driver.find_element(by=By.XPATH, value="//textarea[@class='select2-search__field'][@type='search']").send_keys(random.choice(self.ProductType) + Keys.ENTER)
    #     time.sleep(2)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(5)
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//button[@class = 'mt-2 form_submit btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']").click()
    #     time.sleep(6)
    #     self.check = self.driver.current_url
    #     if "create" not in self.check:
    #         print("Inventory Created With All Valid Details")
    #     else:
    #         self.assertFalse(True, msg="Inventory Not Created With All Valid Details")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()