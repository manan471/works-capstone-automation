import unittest
from selenium import webdriver
import time

import os

from Page_DataBank import DataBank_Page
# import openpyxl
from page_Login import Login_Page
from Page_Lead import Lead_Page
from page_imarat import Imarat_Page
# trace malloc.start()

class WorksApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()
        # cls.driver.get("http://worksapp.propsure.rocks/")
        # cls.driver.implicitly_wait(10)

    def test_Worksapp_A(self):
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://worksapp.propsure.rocks/")
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        time.sleep(5)
        login.EnterEmail("mani.shah@gmail.com")
        login.EnterPassword("12345678")
        login.ClickLoginBtn()
        self.check = login.DetectloginPage()
        if self.check == True:
            print("Test_03:Verify WorksApp login page has been display successfully...")
        else:
            self.assertFalse(True, msg="Test_04:Verify WorksApp login failed...")




    # def test_Worksapp_B(self):
    #     driver = self.driver
    #     login = Login_Page(driver)
    #     lead = Lead_Page(driver)
    #     databank = DataBank_Page(driver)
    #     time.sleep(5)
    #     databank.ClickDataBank()
    #     databank.ClickFilter()
    #     databank.ClickAddBtn()
    #     databank.EnterFName()
    #     databank.EnterLname()
    #     databank.EnterPhone()
    #     databank.ClickSaveBtn()
    #     databank.ClickDataBankListing()
    #     time.sleep(4)





    def test_Worksapp_B(self):
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        time.sleep(5)
        lead.ClickLeadBtn()
        time.sleep(2)
        lead.ClickSelectLeadBtn()
        time.sleep(3)
        lead.ClickleadConvertBtn()
        time.sleep(2)
        lead.ClickleadPipelineBtn()
        time.sleep(2)
        lead.ClickGoToClientBtn()
        time.sleep(2)
        lead.ClickClientBtn()
        time.sleep(5)
        lead.ClickKYCNextBtn()
        time.sleep(2)
        lead.ClickScheduleMeetingBtn()
        time.sleep(2)
        lead.EnterDesc()
        time.sleep(2)
        lead.ClickSaveDiaryBtn()
        time.sleep(2)
        lead.ClickMarkAsDoneBtn()
        time.sleep(3)
        lead.ClickBPNextBtn()
        time.sleep(2)
        lead.ClickIPMNextBtn()
        time.sleep(2)
        lead.ClickCPNextBtn()
        time.sleep(4)
        self.check = lead.DelectKFI()
        if self.check == True:
            print("Test_02:Verify WorksApp inventory section has been display successfully...")
        else:
            self.assertFalse(True, msg="Test_02: Verify WorksApp inventory section has not been display successfully...")
        time.sleep(4)

    def test_Worksapp_C(self):
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        try:
            lead.ClickInstallmentCart()
        except:
            time.sleep(2)
        # try:
        #     lead.ClickBestInvestmentCart()
        # except:
        #     time.sleep(2)
        # try:
        #     lead.ClickRentalCart()
        # except:
        #     time.sleep(2)
        self.check = lead.DelectProject()
        if self.check == True:
            print("Test_03:Verify WorksApp inventory listing has been display successfully...")
        else:
            self.assertFalse(True, msg="Test_03:Verify WorksApp inventory listing has not been display successfully...")
        time.sleep(4)


    def test_Worksapp_D(self):
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        time.sleep(4)
        lead.ClickKFIButton()
        time.sleep(4)
        lead.ClickSubmittoGenerateKFIButton()
        time.sleep(4)
        lead.ClickCrossBtn()
        time.sleep(3)
        lead.ClickRadiobtn()
        time.sleep(3)
        lead.ClickSaveandNextBtn()
        time.sleep(5)
        self.check = lead.DelectClientSection()
        if self.check == True:
            print("Test_04:Verify WorksApp Generate KFI form has been display successfully...")
        else:
            self.assertFalse(True, msg="Test_04:Verify WorksAppGenerate KFI form has not been display successfully...")

    def test_Worksapp_E(self):
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        time.sleep(4)
        lead.EnterCNIC()
        time.sleep(2)
        lead.ClickCustomerSaveDetailsBtn()
        time.sleep(3)
        lead.ClickDocumentDropdown()
        time.sleep(5)
        lead.ClickSaveandNextBtn()
        time.sleep(3)
        self.check = lead.DelectReceivingPage()
        if self.check == True:
            print("Test_05:Verify WorksApp Receiving Report has been display successfully...")
        else:
            self.assertFalse(True, msg="Test_05:Verify WorksApp Receiving Report  has not been display successfully...")
        time.sleep(4)


    def test_Worksapp_F(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://imaratdev.propsure.rocks/login")
        self.driver.implicitly_wait(10)
        driver = self.driver
        login = Login_Page(driver)
        imarat = Imarat_Page(driver)
        imarat.EnterEmail("admin@propsure.rocks")
        time.sleep(2)
        imarat.EnterPassword("12345678")
        time.sleep(2)
        imarat.ClickloginBtn()
        imarat.ClickBooking()
        imarat.ClickAllBooking()
        imarat.ClickIconBtn()
        # imarat.ClickEditBtn()
        time.sleep(2)
        imarat.EnterPaymentType()
        time.sleep(1)
        imarat.EnterPaymentMode()
        time.sleep(1)
        imarat.EnterOfficeLocation()
        time.sleep(1)
        imarat.EnterPayment()
        time.sleep(1)
        imarat.EnterBank()
        time.sleep(2)
        imarat.EnterTransactionDate()
        time.sleep(1)
        imarat.EnterTexAmount()
        time.sleep(2)
        imarat.EnterCashFlowStatus()
        time.sleep(2)
        imarat.ClickSaveBtn()
        time.sleep(3)
        imarat.ClickPending_ActionBtn()
        time.sleep(4)
        imarat.ClickCashflowStatus()
        time.sleep(2)
        imarat.ClickCompanyBankTitle()
        time.sleep(5)
        imarat.ClickInprogressBtn()
        time.sleep(5)
        imarat.ClickBooking()
        imarat.ClickAllBooking()
        imarat.ClickAgainIconBtn()
        time.sleep(2)
        # imarat.Scroll_Down()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.check =  imarat.ClickFinishBtn()
        if self.check == True:
            self.assertFalse(True, msg="Verify WorksApp booking has been store successfully")
        else:
            print("Test_06:Verify WorksApp booking has not been store successfully")
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


    def test_Worksapp_G(self):
        self.driver.maximize_window()
        self.driver.get("http://worksapp.propsure.rocks/")
        self.driver.implicitly_wait(10)
        driver = self.driver
        login = Login_Page(driver)
        lead = Lead_Page(driver)
        time.sleep(7)
        login.EnterEmail("testbcm@gmail.com")
        login.EnterPassword("12345678")
        login.ClickLoginBtn()
        time.sleep(5)
        self.check = login.DetectloginPage()
        if self.check == True:
            print("Test_07:Verify WorksApp login page has been display successfully...")
        else:
            self.assertFalse(True, msg="Test_03: Verify WorksApp login failed...")
        time.sleep(3)

    def test_Worksapp_H(self):
        driver = self.driver
        lead = Lead_Page(driver)
        time.sleep(5)
        lead.ClickDealBtn()
        time.sleep(2)
        self.check = lead.DelectDealListing()
        if self.check == True:
            print("Test_08:Verify WorksApp finally client Convert to Deal has been display successfully....")
        else:
            self.assertFalse(True, msg="Verify WorksApp finally client Convert to Deal has not been display successfully....")
        time.sleep(10)









