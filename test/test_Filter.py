import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class TestFilter:
    def test_filter_is_working_for_campus(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        ele_dis = self.driver.find_element(By.XPATH, "//p[normalize-space()='Filter']")
        if ele_dis.is_enabled():
                ele_dis.click()
                print("This will remain pending till the Filter option will not work in the campuses page")
        else:
             print("Filter button is not enabled in Campus section")

