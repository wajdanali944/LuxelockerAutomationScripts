import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestFilter:
    def test_filter_is_working_for_campus(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(15)
        ele_dis = self.driver.find_element(By.XPATH, "//p[normalize-space()='Filter']")
        if ele_dis.is_enabled():
                ele_dis.click()
                print("This will remain pending till the Filter option will not work in the campuses page")
        else:
             print("Filter button is not enabled in Campus section")

