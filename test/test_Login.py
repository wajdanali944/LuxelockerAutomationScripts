from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        # url = driver.current_url
        print(self.driver.current_url)

    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        expected_warning_message = "The email you entered did not match our records. Please double-check and try again."
        self.driver.implicitly_wait(10)
        assert self.driver.find_element(By.XPATH, "(//span[@class='text-xs'])[1]").text.__contains__(expected_warning_message)
        # assert expected_warning_message == error_message

    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234567899aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        expected_warning_message = "The password you entered did not match our records. Please double-check and try " \
                                   "again."
        self.driver.implicitly_wait(10)
        assert self.driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        expected_warning_message = "Email is required"
        assert self.driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)



    def generate_email_with_time_stamp(self):
            time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            return "wajdanali" + time_stamp + "@gmail.com"