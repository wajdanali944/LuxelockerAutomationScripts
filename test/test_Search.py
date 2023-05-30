import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID, "Search").send_keys("Miami")
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeSmall css-z5jn5r'])[1]").click()

        assert self.driver.find_element(By.XPATH, "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr/td[2]").text.__contains__("Miami Campus")

    def test_search_for_a_non_valid_product(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID, "Search").send_keys("----asdf---")
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeSmall css-z5jn5r'])[1]").click()
        expected_warning_message = "No data found."
        assert self.driver.find_element(By.XPATH, "//p[@class='mt-2']").text.__contains__(expected_warning_message)

    def test_search_without_entering_any_product(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID, "Search").send_keys("")
        elem_disabled = self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeSmall css-z5jn5r'])[1]")
        if elem_disabled.is_enabled():
            elem_disabled.click()
        else:
            print("Search button is disabled.")
