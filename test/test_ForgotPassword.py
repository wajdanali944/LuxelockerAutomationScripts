import pytest
from selenium.webdriver.common.by import By

from pages.ForgotPassword import ForgotPassword


@pytest.mark.usefixtures("setup_and_teardown")
class TestForgotPassword:
    def test_forgot_password_with_non_existed_email(self):
        forgot_password = ForgotPassword(self.driver)
        forgot_password.click_on_forgot_password_button()
        self.driver.implicitly_wait(3)
        forgot_password.enter_email_address("wajdanali9333@gmail.com")
        forgot_password.click_on_send_button()
        expected_warning_message = "Email is required"
        self.driver.implicitly_wait(5)
        assert forgot_password.retreive_warning_message_xpath().__contains__(expected_warning_message)

    def test_forgot_password_with_existed_email(self):
        forgot_password = ForgotPassword(self.driver)
        forgot_password.click_on_forgot_password_button()
        self.driver.implicitly_wait(3)
        forgot_password.enter_email_address("hirat917+45@gmail.com")
        forgot_password.click_on_send_button()
        self.driver.implicitly_wait(5)
        self.driver.get("https://app-staging.luxelocker.com/")
        element = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/p")
        print(element.get_attribute('href'))

    def test_forgot_password_without_entering_email(self):
        forgot_password = ForgotPassword(self.driver)
        forgot_password.click_on_forgot_password_button()
        self.driver.implicitly_wait(3)
        forgot_password.enter_email_address("")
        forgot_password.click_on_send_button()
        self.driver.implicitly_wait(5)
        expected_warning_message = "Email is required"
        self.driver.implicitly_wait(3)
        assert forgot_password.retreive_warning_message_xpath().__contains__(expected_warning_message)
