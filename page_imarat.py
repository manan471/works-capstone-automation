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


class Imarat_Page():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.click_loginbtn = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/form/div[4]/button"
        self.click_iconbtn = "(//a[@class='btn btn-soft-secondary btn-sm btn-icon'])[1]"
        self.click_editbtn = "(//a[@class = 'btn btn-soft-secondary btn-sm btn-icon'])[3]"
        self.click_paymenttype = "payment_type_id"
        self.paymentmode = "payment_mode_id"
        self.officelocation = "office_location_id"
        self.amount = "amount"
        self.bankname = "bank_id"
        self.cashflowstatus = "cash_flow_status"
        self.transactiondate = "booking_date"
        self.click_savebtn = "//button[@type = 'button'][@class ='mt-2 form_submit submit_reset btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2']"
        self.click_booking = "Bookings"
        self.click_allbooking = "All Bookings"
        self.tex_amount = "tax_amount"
        self.click_actionbtn = "//a[@class='btn btn-soft-secondary btn-sm btn-icon']"
        self.click_alltransaction = " (//i[@class = 'ri-download-2-fill me-2 align-bottom text-muted'])[1]"
        self.click_inprogressbtn = "//button[@class = 'dropdown-item in_progress_transaction']"
        self.deposit_bankname = "deposit_bank_title"
        self.company_accountno = "deposit_account_number"
        self.branchname = "deposit_branch_name"
        self.deposit_date = "deposit_date"
        self.deposit_amount = "deposit_amount"
        self.bank_depositid = "deposit_id"
        self.attact_file = "deposit_attachment"
        self.submit_depositbtn = "//*[@id='in_progress_transaction_model']/div/div/form/div/div/button[1]"
        self.approvebtn = "//tr[1]/td[20]/div[1]/ul[1]/li[4]/button[1]"
        self.transactionappove = "transaction_id"
        self.approveleardate = "clearance_date"
        self.approvebankstatement = "bank_deposited_date"
        self.approvebankrefernce = "bank_statement_refernce"
        self.approvesubmitbtn = "//*[@id='approved_transaction_model']/div/div/form/div/div/button[1]"
        self.savebookingbtn = "//button[@class = 'form_submit btn btn-success btn-label right ms-auto']"
        self.clickfinanceactionbtn = "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[12]/div[1]/a[1]/i[1]"
        self.click_inprogressbtn = "//*[@id='collapse-financial-']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[12]/div[1]/ul[1]/li[4]/button[1]"
        self.clickcashflowStatus = "cash_flow_status"
        self.click_transaction = "Transactions"
        self.click_companybanktitles = "deposit_bank_title"
        self.inprogressbtn = "//tr[1]/td[1]/div[1]/a[1]/i[1]"
        self.finishbtn = "//a[text()='Finish']"
        self.bookingfinishbtn = "//button[@type ='button'][@data-nexttab= 'pills-experience-tab']"


    def ClickFinishBtn(self):
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'form_submit btn btn-success btn-label right ms-auto']").click()
        time.sleep(3)
        # self.driver.find_element(by=By.XPATH, value=self.finishbtn).click()
        # time.sleep(2)
    def ClickInprogressBtn(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value= self.inprogressbtn).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="(//button[@class = 'dropdown-item approved_transaction'])[1]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="transaction_id").send_keys("3244")
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="clearance_date").send_keys("15" + "02" + "2024")
        time.sleep(1)
        self.driver.find_element(by=By.ID, value="bank_deposited_date").send_keys("16" + "02" + "2024")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//button[text() = 'Submit'])[75]").click()
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 1000);")




    # def ClickTransactionBtn(self):
    #     self.driver.find_element(by=By.LINK_TEXT, value=self.click_transaction).click()
    #     time.sleep(2)
    #     self.driver.find_element(by=By.LINK_TEXT, value=" All Payments").click()
    #     time.sleep(2)
    def ClickCompanyBankTitle(self):
        self.driver.find_element(by=By.ID, value=self.click_companybanktitles).send_keys("MCB-Amazon Mall (SMC-Pvt) Limited – Main" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="deposit_date").send_keys("15" + "02" + "2024")
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="deposit_amount").send_keys("9021")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//button[@class = 'btn btn-primary form_submit'])[1]").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000);")

    def Scroll_Down(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")


    def ClickCashflowStatus(self):
        self.driver.find_element(by=By.ID, value=self.clickcashflowStatus).send_keys("Processed" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(3)

    def ClickPending_ActionBtn(self):
        self.driver.refresh()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        # time.sleep(4)
        # self.driver.execute_script("window.scrollTo(500, 0);")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.clickfinanceactionbtn).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.click_inprogressbtn).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//select[@class = 'form-select cash_flow_status'])[2]").send_keys("Presented" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)


    def ClickSaveBookingBtn(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.savebookingbtn))):
            return True
        else:
            return False

    def ClickApproveSubmitBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.approvesubmitbtn).click()
        time.sleep(1)

    def ClickApproveBankRefernce(self):
        self.driver.find_element(by=By.NAME, value=self.approvebankrefernce).send_keys("21")
        time.sleep(1)

    def ClickApproveBankStatementDate(self):
        self.driver.find_element(by=By.NAME, value=self.approvebankstatement).send_keys("01" + "06" + "2022")
        time.sleep(1)

    def ClickApproveClearDate(self):
        self.driver.find_element(by=By.NAME, value=self.approveleardate).send_keys("08" + "06" + "2022")
        time.sleep(1)

    def EnterTransactionApproved(self):
        self.driver.find_element(by=By.ID, value=self.transactionappove).send_keys("123")
        time.sleep(1)

    def ClickApprovedBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.approvebtn).click()
        time.sleep(1)

    def ClickSubmitBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.submit_depositbtn).click()
        time.sleep(2)



    def EnterBankDepositId(self):
        self.driver.find_element(by=By.NAME, value=self.bank_depositid).send_keys("21")
        time.sleep(2)


    def EnterAmount(self):
        self.driver.find_element(by=By.NAME, value=self.deposit_amount).send_keys(p)
        time.sleep(2)

    def EnterDepositDate(self):
        self.driver.find_element(by=By.NAME, value=self.deposit_date).send_keys("01" + "06" + "2022")
        time.sleep(2)
    def EnterBranchName(self):
        self.driver.find_element(by=By.NAME, value=self.branchname).send_keys("G-10 Islamabad")
        time.sleep(2)


    def EnterBankName(self):
        self.driver.find_element(by=By.NAME, value=self.deposit_bankname).send_keys("MCB-Amazon Mall (SMC-PVT) Limited main" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)

    def EnterCashFlowStatus(self):
        self.driver.find_element(by=By.NAME, value=self.cashflowstatus).send_keys("To Be Deposit" + Keys.ARROW_DOWN+Keys.ENTER)
        time.sleep(2)


    # def ClickInProgressBtn(self):
    #     self.driver.find_element(by=By.XPATH, value=self.click_inprogressbtn).click()
    #     time.sleep(2)

    def ClickActionBtn(self):
        self.driver.execute_script("window.scrollTo(0,600)")
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0, 690);")

        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.click_actionbtn).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'dropdown-item in_progress_transaction']").click()
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="deposit_account_number").send_keys(p)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="deposit_bank_name").send_keys("Allied Bank")
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="deposit_branch_name").send_keys("G-10 Islamabad")
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value="deposit_date").send_keys("04-12-2023")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="(//button[text() = 'Submit'])[1]").click()
        time.sleep(4)

    def ClickAllTransaction(self):
        self.driver.find_element(by=By.XPATH, value=self.click_alltransaction).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,600)")
        time.sleep(1)

        # self.driver.execute_script("window.scrollBy(500, 0);")
        time.sleep(3)


    def ClickBooking(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.click_booking).click()
        time.sleep(1)
    def ClickAllBooking(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.click_allbooking).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(500, 0);")
        time.sleep(3)

    def EnterPaymentType(self):
        self.driver.find_element(by=By.NAME, value=self.click_paymenttype).send_keys(Keys.ARROW_DOWN +"Full payment" + Keys.ENTER)
        time.sleep(1)
    def EnterPaymentMode(self):
        self.driver.find_element(by=By.NAME, value=self.paymentmode).send_keys(Keys.ARROW_DOWN +"Cash" + Keys.ENTER)
        time.sleep(1)
    def EnterOfficeLocation(self):
        self.driver.find_element(by=By.NAME, value=self.officelocation).send_keys(Keys.ARROW_DOWN +"Graana" + Keys.ENTER)
        time.sleep(1)

    def EnterPayment(self):
        global p
        p = self.driver.find_element(by=By.XPATH,value="//*[@id='collapse-financial-']/div/div/div/div/div/div/table/tfoot/tr/td[1]").text
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.amount).send_keys(p)
        time.sleep(1)

    def EnterBank(self):
        self.driver.find_element(by=By.NAME, value=self.bankname).send_keys(Keys.ARROW_DOWN +"Bank of China Limited" + Keys.ENTER)
        time.sleep(1)

    def EnterTransactionDate(self):
        self.driver.find_element(by=By.NAME, value=self.transactiondate).send_keys("01" + "06" + "2022")
        time.sleep(1)

    def EnterTexAmount(self):
        self.driver.find_element(by=By.NAME, value=self.tex_amount).clear()
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value=self.tex_amount).send_keys("0")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 690);")
        time.sleep(2)

    # def ClickSaveBtn(self):
    #     self.driver.find_element(by=By.XPATH, value=self.click_savebtn).click()
    #     time.sleep(2)
    #     # self.driver.execute_script("window.scrollTo(0, 1000);")
    #     # time.sleep(2)
    #     # self.driver.execute_script("window.scrollTo(500, 0);")

    def ClickSaveBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_savebtn).click()
        time.sleep(5)
        # if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.click_savebtn))):
        #     return True
        # else:
        #     return False


    def EnterEmail(self,email):
        self.driver.find_element(by=By.NAME, value=self.email).send_keys(email)
        time.sleep(1)
    def EnterPassword(self,password):
        self.driver.find_element(by=By.NAME, value=self.password).send_keys(password)
        time.sleep(1)

    def ClickloginBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_loginbtn).click()
        time.sleep(1)

    def ClickIconBtn(self):
        self.driver.execute_script("window.scrollTo(0,600)")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.click_iconbtn).click()
        # time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, 1000);")
        # time.sleep(4)
        # self.driver.find_element(by=By.XPATH, value="//a[@class = 'btn btn-light btn-label previestab']").click()
        # time.sleep(4)
        # self.driver.find_element(by=By.ID, value="serach-customer").send_keys("qadeer")
        # time.sleep(2)
        # self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Qadeer Katalon1").click()
        # time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        # self.driver.find_element(by=By.XPATH, value="//button[@class = 'form_submit btn btn-success btn-label right ms-auto ']").click()
        # time.sleep(4)

        # self.driver.find_element(by=By.ID, value="serach-agents").send_keys("Abdul")
        # time.sleep(2)
        # self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Abdul Salam").click()
        # time.sleep(2)
        #
        # self.driver.execute_script("window.scrollTo(0, 500);")
        # time.sleep(2)
        # self.driver.find_element(by=By.XPATH, value="(//input[@type= 'text'])[4]").send_keys("manan abbasi")
        # time.sleep(2)
        # self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="manan abbasi").click()
        # time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        # self.driver.find_element(by=By.XPATH,value="//button[@type ='button'][@data-nexttab= 'pills-experience-tab']").click()
        # time.sleep(3)


    def ClickAgainIconBtn(self):
        self.driver.execute_script("window.scrollTo(0,600)")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.click_iconbtn).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(2)

    def ClickBookingFinishBtn(self):
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.bookingfinishbtn))):
            return True
        else:
            return False

    def ClickEditBtn(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.click_editbtn).click()
        time.sleep(1)

    def ClickPending_Transaction(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.click_editbtn).click()


