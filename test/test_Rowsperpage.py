import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class TestRowsPerPage:
    def test_verifying_rows_per_page_with_total_rows(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div"):
           dropdown_count = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div").text
           totalfacilities = len(self.driver.find_elements(By.XPATH, "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[1]/div/table/tbody/tr"))
           if dropdown_count == totalfacilities:
                print ('Rows are 20')
           else:
                print("Need to click on 50 rows per page.")
        else:
             quit()
