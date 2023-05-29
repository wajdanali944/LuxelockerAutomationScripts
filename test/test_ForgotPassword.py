import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup_and_teardown")
class TestForgotPassword:
    def test_forgot_password_with_non_existed_email(self):
        self.driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input").send_keys("wajdanali933@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@id=':r3:']").click()
        expected_warning_message = "Something went wrong"
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)
        # url = driver.current_url
        print(self.driver.current_url)

    def test_forgot_password_with_existed_email(self):
        self.driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input").send_keys("hirat917+45@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@id=':r3:']").click()
        self.driver.implicitly_wait(5)
        self.driver.get("https://app-staging.luxelocker.com/")
        element = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/p")
        print(element.get_attribute('href'))
        # url = driver.current_url
        #print(driver.current_url)

    def test_forgot_password_without_entering_email(self):
        self.driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input").send_keys("")
        self.driver.find_element(By.XPATH, "//*[@id=':r3:']").click()
        self.driver.implicitly_wait(5)
        expected_warning_message = "Email is required"
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)
        # url = driver.current_url
        #print(driver.current_url)
