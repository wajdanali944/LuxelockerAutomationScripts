from telnetlib import EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test.conftest import setup_and_teardown
from test.BaseTest import BaseClass


class call(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def recallable_button(driver):
        try:
            driver.find_element(By.XPATH,
                                "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-bq9v9b']/parent::div").click
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH,
                                "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root "
                                "MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium "
                                "MuiButton-containedSizeMedium MuiButton-root MuiLoadingButton-root "
                                "MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium "
                                "MuiButton-containedSizeMedium css-bq9v9b']").click()
            print("Modal button clicked")  # clicking on continue button
        except TimeoutException:
            print("Modal button was not found")


    def recallable_disable_button(driver):
        try:
            ele_dis = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium Mui-disabled MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1lrzbgp']/parent::div"))).is_enabled()
        # ele_dis = self.driver.find_element(By.XPATH,
        # "//*[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium Mui-disabled MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1lrzbgp']").click()
            ele_dis.click()
        except:
            print("Button is disabled")
            pass

    def recallable_campus_name_already_exists(driver):
        expected_warning_message = "Facility with this name already exists."
        try:
            elemexist = driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Peter")  # entering name
            assert elemexist.__eq__(expected_warning_message)
            print("Facility name already exists")
        except:

            print("Kindly enter some other name, this name already exists.")
            exit()