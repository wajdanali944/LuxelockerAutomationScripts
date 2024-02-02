from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789Ll!@")
        home_page.click_on_login_button()


    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address(self.generate_email_with_time_stamp())
        home_page.enter_password("123456789Ll!@")
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        expected_warning_message = "The email you entered did not match our records. Please double-check and try again."
        self.driver.implicitly_wait(10)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)


    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789Ll!")
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        expected_warning_message = "The password you entered did not match our records. Please double-check and try again."
        self.driver.implicitly_wait(10)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)



    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("")
        home_page.enter_password("")
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        expected_warning_message = "Email is required"
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)



    def generate_email_with_time_stamp(self):
            time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            return "wajdanali" + time_stamp + "@gmail.com"