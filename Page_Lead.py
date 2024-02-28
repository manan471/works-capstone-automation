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


class Lead_Page():
    def __init__(self, driver):
        self.driver = driver
        self.add_btn = "(//a[@class = 'inline-flex items-center text-sm font-medium leading-5 transition duration-150 ease-in-out focus:outline-none text-white-500 hover:text-white-700 focus:text-white-700 '])[3]"
        self.add_leadbtn = "//p[text() = 'Add Lead']"
        self.fname = "first_name"
        self.lname = "last_name"
        self.phone = "phone"
        self.city = "(//div[@class = 'MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-182didf'])[2]"
        self.project = "(//div[@class = 'MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-182didf'])[3]"
        self.product_type = "(//div[@class = 'MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-182didf'])[4]"
        self.campaign_source = "(//div[@class = 'MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input css-qiwgdb'])[1]"
        self.campaign = "(//div[@class = 'MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input css-qiwgdb'])[2]"
        self.value = "value"
        self.click_savebtn = "//button[text() = 'Save']"
        self.detect_lead = "//div[@class = 'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation6 MuiAlert-root MuiAlert-filledSuccess MuiAlert-filled css-juoc2m']"
        self.click_lead = "(//div[@class = 'MuiButtonBase-root MuiListItemButton-root MuiListItemButton-gutters MuiListItemButton-root MuiListItemButton-gutters css-1o5cwzc'])[5]"
        self.click_selectlead = "(//div[@class = 'MuiBox-root css-yeouz0'])[1]"
        self.click_convertbtn = "//button[text() = 'Connect']"
        self.click_pipelineP1 = "(//div[@class = 'MuiBox-root css-5vl6in'])[2]"
        self.click_gotoclient = "//button[text() = 'Go To Clients']"
        self.click_clientbtn = "(//div[@class = 'MuiButtonBase-root MuiListItemButton-root MuiListItemButton-gutters MuiListItemButton-root MuiListItemButton-gutters css-1o5cwzc'])[6]"
        self.click_kycnextbtn = "//button[normalize-space()='Next']"
        self.click_bpnextbtn = "//button[normalize-space()='Next']"
        self.click_ipmnextbtn = "//button[normalize-space()='Next']"
        self.click_cpnextbtn = "//button[normalize-space()='Next']"
        self.click_installmentcart = "(//div[@class ='MuiBox-root css-4g6ai3'])[1]"
        self.click_bestinvestmentcart = "//button[text() = 'Best Investment']"
        self.crossbtn = "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-1jq3me9']"
        self.click_rental_cart = "//button[text() = 'Rental']"
        self.detectkfi = "//div[text() = 'Inventory Selection']"
        self.vreify_project = "//button[text() = 'Installment']"
        self.click_kfibtn = "//button[text() = 'KFI']"
        self.click_submittogeneratekfibtn = "//button[text() = 'Submit to Generate KFI']"
        self.click_radiobtn = "(//input[@class = 'PrivateSwitchBase-input css-1m9pwf3'])[1]"
        self.click_saveandnextbtn = "//button[text() = 'Save & Next']"
        self.detectbooking = "//div[text() = 'Client Selection']"
        self.add_cnic = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[6]"
        self.savecustomerbtn = "//button[text() = 'Save']"
        self.click_docinput = "//div[@class = 'MuiBox-root css-x86v8o']"
        self.backbtn = "//button[text() ='Back']"
        self.scheduleMeeting = "//button[text() = 'Schedule a Meeting']"
        self.desc = "desc"
        self.markasdonbtn = "//button[text() = 'Mark As Done']"
        self.savedairybtn = "(//button[text() = 'Save'])[2]"
        self.click_dealbtn = "(//div[@class = 'MuiButtonBase-root MuiListItemButton-root MuiListItemButton-gutters MuiListItemButton-root MuiListItemButton-gutters css-1o5cwzc'])[7]"
        self.detect_deallisting = "(//div[@class = 'MuiBox-root css-yeouz0'])[1]"



    def DelectDealListing(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_deallisting))):
            return True
        else:
            return False

    def ClickDealBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_dealbtn).click()
        time.sleep(2)

    def ClickSaveDiaryBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.savedairybtn).click()
        time.sleep(2)

    def ClickMarkAsDoneBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.markasdonbtn).click()
        time.sleep(2)

    def EnterDesc(self):
        self.driver.find_element(by=By.NAME, value=self.desc).send_keys("testing")
        time.sleep(2)


    def ClickScheduleMeetingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.scheduleMeeting).click()
        time.sleep(2)

    def ClickCrossBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.crossbtn).click()
        time.sleep(1)

    def ClickCustomerSaveDetailsBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.savecustomerbtn).click()
        time.sleep(2)

    def ClickDocumentDropdown(self):
        self.driver.find_element(by=By.XPATH, value=self.click_docinput).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//li[text() = 'Booking Form']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//span[text() = 'Choose File'])[3]").send_keys("C:\\Users\\Abdul Manan\\Downloads\\Receipt-91845-2023-08-04T13_13_08.921Z.pdf")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//span[text() = 'Submit']").click()

    def DelectReceivingPage(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.backbtn))):
            return True
        else:
            return False


    def EnterCNIC(self):
        self.driver.find_element(by=By.XPATH, value="(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[6]").send_keys("1310203755892")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[12]").send_keys("Meezan Bank")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[13]").send_keys("Meezan Bank")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[14]").send_keys("0921090921901209")
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value="(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[15]").send_keys("234234232100")

    def DelectClientSection(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detectbooking))):
            return True
        else:
            return False


    def ClickSaveandNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_saveandnextbtn).click()
        time.sleep(1)


    def ClickRadiobtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_radiobtn).click()
        time.sleep(3)


    def ClickSubmittoGenerateKFIButton(self): 
        self.driver.find_element(by=By.XPATH, value=self.click_submittogeneratekfibtn).click()
        time.sleep(1)

    def ClickKFIButton(self):
        self.driver.find_element(by=By.XPATH, value=self.click_kfibtn).click()
        time.sleep(1)

    def DelectProject(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.vreify_project))):
            return True
        else:
            return False

    def DelectKFI(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detectkfi))):
            return True
        else:
            return False

    def ClickRentalCart(self):
        self.driver.find_element(by=By.XPATH, value=self.click_rental_cart).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="(//div[@class = 'MuiBox-root css-1b9byhf'])[1]").click()


    def ClickBestInvestmentCart(self):
        self.driver.find_element(by=By.XPATH, value=self.click_bestinvestmentcart).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="(//div[@class = 'MuiBox-root css-1b9byhf'])[1]").click()

    def ClickInstallmentCart(self):
        self.driver.find_element(by=By.XPATH, value=self.click_installmentcart).click()
        time.sleep(2)

    def ClickCPNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_cpnextbtn).click()
        time.sleep(4)
        # self.driver.find_element(by=By.XPATH, value="//button[text() = 'Next']").click()



    def ClickIPMNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_ipmnextbtn).click()
        time.sleep(2)

    def ClickBPNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_bpnextbtn).click()
        time.sleep(2)


    def ClickKYCNextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_kycnextbtn).click()
        time.sleep(2)


    def ClickClientBtn(self):
        # global p
        # p = self.driver.find_element(by=By.XPATH, value="//p[text() = '5595']").text()
        # self.driver.find_element(by=By.XPATH, value=self.click_clientbtn).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="(//div[@class ='MuiBox-root css-gzsfut'])[1]").click()
        time.sleep(2)


    def ClickGoToClientBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_gotoclient).click()
        time.sleep(2)


    def ClickleadPipelineBtn(self):
        # for i in range(2):
        self.driver.find_element(by=By.XPATH, value=self.click_pipelineP1).click()
        time.sleep(2)

    def ClickleadConvertBtn(self):
        # time.sleep(2)
        # self.driver.find_element(by=By.XPATH, value="(//span[@class = 'MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-l024kx'])[13]").click()
        # time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_convertbtn).click()
        time.sleep(2)

    def ClickSelectLeadBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_selectlead).click()
        time.sleep(2)

    def ClickLeadBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_lead).click()
        time.sleep(1)
    def ClickAddBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.add_btn).click()
        time.sleep(1)

    def ClickAddLeadBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.add_leadbtn).click()
        time.sleep(1)

    def EnterFName(self,fname):
        self.driver.find_element(by=By.NAME, value=self.fname).send_keys(fname)
        time.sleep(1)

    def EnterLName(self,lname):
        self.driver.find_element(by=By.NAME, value=self.lname).send_keys(lname)
        time.sleep(1)

    def EnterPhoneNo(self, phone):
        self.driver.find_element(by=By.NAME, value=self.phone).send_keys(phone)
        time.sleep(1)

    def ClickCity(self):
        self.driver.find_element(by=By.XPATH, value=self.city).send_keys('Abbottabad' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

        # self.driver.find_element(by=By.XPATH, value=self.city).click()
        # time.sleep(1)
        # # self.driver.find_element(by=By.XPATH, value=self.city).send_keys(city)
        # time.sleep(1)
        # self.driver.find_element(by=By.XPATH, value="//li[text() = 'Abbottabad']").click()
        # time.sleep(1)
        # self.driver.find_element(by=By.NAME, value=self.city).send_keys(city)
        # time.sleep(1)
        # self.driver.find_element(by=By.NAME, value=self.city).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        # time.sleep(1)

    def ClickProject(self):
        self.driver.find_element(by=By.XPATH, value=self.project).send_keys('Amazon Mall' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

    def ClickProductType(self):
        self.driver.find_element(by=By.XPATH, value=self.product_type).send_keys('Installment' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

    def ClickCampaignSource(self):
        self.driver.find_element(by=By.XPATH, value=self.campaign_source).send_keys('Facebook' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

    def ClickCampaign(self):
        self.driver.find_element(by=By.XPATH, value=self.campaign).send_keys('Facebook Campaign' + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

    def EnterValue(self,value):
        self.driver.find_element(by=By.NAME, value=self.value).send_keys(value)
        time.sleep(1)

    def ClickSaveBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_savebtn).click()


    def VarifyAddLead(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.detect_lead))):
            return True
        else:
            return False




