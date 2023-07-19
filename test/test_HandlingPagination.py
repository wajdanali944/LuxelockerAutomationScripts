import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestHandlingPagination:

    def test_verifying_pagination_with_table_data_for_campus_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(15)
        rows = len(self.driver.find_elements(By.XPATH,
                                             "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr"))  # count number of rows
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()

        rows_next = len(self.driver.find_elements(By.XPATH,
                                                     "/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total = rows_next+rows
        rows_next1 = len(self.driver.find_elements(By.XPATH,
                                                  "/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total1 = rows_next1 + Total
        next_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()
        totalpaginationcount = self.driver.find_element(By.XPATH, "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()

        if Total1 >= int(splitval[2]):
            print(f'Total rows are {splitval[2]}')
        else:
            print("Rows are more than 60")

    def test_verifying_pagination_with_table_data_for_units_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_unit_link()
        self.driver.implicitly_wait(15)
        rows = len(self.driver.find_elements(By.XPATH,
                                             "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr"))  # count number of rows
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()

        rows_next = len(self.driver.find_elements(By.XPATH,
                                                     "/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total = rows_next+rows
        rows_next1 = len(self.driver.find_elements(By.XPATH,
                                                  "/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total1 = rows_next1 + Total
        next_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()
        totalpaginationcount = self.driver.find_element(By.XPATH, "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()

        if Total1 >= int(splitval[2]):
            print(f'Total rows are {splitval[2]}')
        else:
            print("Rows are more than 60")

    def test_verifying_pagination_with_table_data_for_users_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        rows = len(self.driver.find_elements(By.XPATH,
                                             "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr"))  # count number of rows
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()

        rows_next = len(self.driver.find_elements(By.XPATH,
                                                     "/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total = rows_next+rows
        rows_next1 = len(self.driver.find_elements(By.XPATH,
                                                  "/html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))
        Total1 = rows_next1 + Total
        next_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[2]/div/div[2]/div[2]/ul/li[2]'))).click()
        totalpaginationcount = self.driver.find_element(By.XPATH, "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()

        if Total1 >= int(splitval[2]):
            print(f'Total rows are {splitval[2]}')
        else:
            print("Rows are more than 60")
