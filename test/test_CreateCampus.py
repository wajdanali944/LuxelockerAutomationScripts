import time
from idlelib import browser

import pytest
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateCampus:
    def test_creating_campus_including_all_values(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()  #Login button click
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click() #campus button click side bar
        self.driver.implicitly_wait(8)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/span/span[1]").click() #create campus button click
        time.sleep(6)
        selbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//p[normalize-space()="Select"]'))).click()  #clicking on select option
        seleelem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//p[normalize-space()='Arizona'])[1]"))).click()  #clicking on dropdown options
        try:
           self.driver.find_element(By.XPATH, "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']/parent::div").click
           self.driver.implicitly_wait(3)
           self.driver.find_element(By.XPATH, "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']").click()
           print("Modal button clicked")   #clicking on continue button
        except TimeoutException:
            print("Modal button was not found")
        elename = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))).send_keys("Virginia")  # entering name
        self.driver.find_element(By.NAME, "street").send_keys("77 virg block")
        self.driver.find_element(By.NAME, "postalCode").send_keys("879000")
        self.driver.find_element(By.NAME, "numOfUnits").send_keys("10")
        self.driver.find_element(By.NAME, "longitude").send_keys("100.1")
        self.driver.find_element(By.NAME, "latitude").send_keys("200.1")
        self.driver.find_element(By.NAME, "maintenanceFee").send_keys("200")
        self.driver.find_element(By.XPATH, "//label[contains(@color,'#FFFFFF')]//input[contains(@type,'checkbox')]").click() #checkboxing active checkbox
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']/parent::div").click
            self.driver.implicitly_wait(3)
            self.driver.find_element(By.XPATH,
                                     "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']").click()
            print("Modal button clicked")  # clicking on continue button
        except TimeoutException:
            print("Modal button was not found")  # clicking on details page continue button
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']/parent::div").click
            self.driver.implicitly_wait(3)
            self.driver.find_element(By.XPATH,
                                     "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']").click()
            print("Modal button clicked")  # clicking on continue button
        except TimeoutException:
            print("Modal button was not found")  # clicking on System Settings continue button
        clcair = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Air Conditioner']"))).click()  # selecting Air Conditioner
        clcair = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[normalize-space()='Security Camera']"))).click()  # selecting security camera
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']/parent::div").click
            self.driver.implicitly_wait(3)
            self.driver.find_element(By.XPATH,
                                     "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']").click()
            print("Modal button clicked")  # clicking on continue button
        except TimeoutException:
            print("Modal button was not found")  # clicking on Save button on Amenties

    def test_creating_campus_without_selecting_select_dropdown(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()  #Login button click
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click() #campus button click side bar
        self.driver.implicitly_wait(8)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/span/span[1]").click() #create campus button click
        time.sleep(6)
        # selbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//p[normalize-space()="Select"]'))).click()  #clicking on select option
        # seleelem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, ""))).click()  #clicking on dropdown options

        try:
            ele_dis = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium Mui-disabled MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1lrzbgp']/parent::div")))
        # ele_dis = self.driver.find_element(By.XPATH,
                                 # "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium Mui-disabled MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1lrzbgp']").click()
            ele_dis.click()
        except:
            print("Button is disabled")
            pass




