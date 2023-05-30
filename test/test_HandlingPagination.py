import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("setup_and_teardown")
class TestHandlingPagination:
    def test_verifying_pagination_with_table_data(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        rows = len(self.driver.find_elements(By.XPATH,
                                             "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr"))  # count number of rows
        cols = len(self.driver.find_elements(By.XPATH,
                                             "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr["
                                             "1]/td"))  # count number of columns
        print(rows)
        print(cols)

        next_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()

        rows_next = len(self.driver.find_elements(By.XPATH,
                                                     "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total = rows_next+rows
        next_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()
        totalpaginationcount =self.driver.find_element(By.XPATH, "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()
        print(splitval)

        assert str(Total) == splitval[2]
