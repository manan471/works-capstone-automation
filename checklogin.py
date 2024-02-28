import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://worksapp.propsure.rocks")
time.sleep(2)
driver.find_element(by=By.NAME, value="email").send_keys("admin@gmail.com")
time.sleep(2)
driver.find_element(by=By.NAME, value="password").send_keys("123456789")
time.sleep(3)
driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div/form/div[3]/button").click()
time.sleep(20)