import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRowsPerPage:

    def test_verifying_rows_per_page_with_total_rows_for_campus_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click() #click on Campus on side window
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")

        totalpaginationcount = self.driver.find_element(By.XPATH,
                                                            "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()

        if not self.check_for_more_records(count=20, total_records=splitval[2]):
            if not self.check_for_more_records(count=50, total_records=splitval[2]):
                if not self.check_for_more_records(count=100, total_records=splitval[2]):
                    print("Rows are more than 100")

    def test_verifying_rows_per_page_with_total_rows_for_units_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[2]/div/div[2]/span").click()  #click on Units on side window
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")

        totalpaginationcount = self.driver.find_element(By.XPATH,
                                                            "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()

        if not self.check_for_more_records(count=20, total_records=splitval[2]):
            if not self.check_for_more_records(count=50, total_records=splitval[2]):
                if not self.check_for_more_records(count=100, total_records=splitval[2]):
                    print("Rows are more than 100")

    def test_verifying_rows_per_page_with_total_rows_for_users_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[3]/div/div[2]/span").click()  #No need of click on side window because it is already on the Users page
        # self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div/div")

        totalpaginationcount = self.driver.find_element(By.XPATH,
                                                            "//span[@class='Pagination-rowsLabel']")
        text = totalpaginationcount.text
        splitval = text.split()

        if not self.check_for_more_records_for_users_page(total=20, all_records=splitval[2]):
            if not self.check_for_more_records_for_users_page(total=50, all_records=splitval[2]):
                if not self.check_for_more_records_for_users_page(total=100, all_records=splitval[2]):
                    print("Rows are more than 100")

    def test_verifying_rows_per_page_with_total_rows_for_faqs_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[4]/div").click()  #click on FAQS on side window
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div")

        totalpaginationcount = self.driver.find_element(By.XPATH,
                                                            "//*[@id=\"simple-tabpanel-0\"]/div/div[2]/div/div[2]/div[1]/div[2]/span")
        text = totalpaginationcount.text
        splitval = text.split()

        if not self.check_for_more_records(count=20, total_records=splitval[2]):
            if not self.check_for_more_records(count=50, total_records=splitval[2]):
                if not self.check_for_more_records(count=100, total_records=splitval[2]):
                    print("Rows are more than 100")

    def test_verifying_rows_per_page_with_total_rows_for_announcement_page(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div[1]/ul/div[1]/div[5]/div/div[2]/span").click()  # click on Announcements on side window
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div") #rows per page xpath

        totalpaginationcount = self.driver.find_element(By.XPATH,
                                                        "//span[@class='Pagination-rowsLabel']")  #pagination xpath
        text = totalpaginationcount.text
        splitval = text.split()

        if not self.check_for_more_records_for_announcement_page(ann_total=20, ann_all_records=splitval[2]):
            if not self.check_for_more_records_for_announcement_page(ann_total=50, ann_all_records=splitval[2]):
                if not self.check_for_more_records_for_announcement_page(ann_total=100, ann_all_records=splitval[2]):
                    print("Rows are more than 100")

    def check_for_more_records(self, count, total_records):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div").click()
        totalfacilities = self.driver.find_elements(By.XPATH, f"//li[normalize-space()='{count}']")
        totalfacilities[0].click()
        rows_count = len(self.driver.find_elements(By.XPATH,
                                                   "//html/body/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr"))

        if rows_count >= int(total_records):
            print(f'Rows are under {count}')
            return True
        else:
            return False

    def check_for_more_records_for_users_page(self, total, all_records):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div/div").click()
        totalfacilities = self.driver.find_elements(By.XPATH, f"//li[normalize-space()='{total}']")
        totalfacilities[0].click()
        rows_count = len(self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div/div[2]/div/div[3]/div/div[1]/div/table/tbody/tr[1]"))

        if rows_count >= int(all_records):
            print(f'Rows are under {total}')
            return True
        else:
            return False

    def check_for_more_records_for_announcement_page(self, ann_total, ann_all_records):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div").click()
        totalfacilities = self.driver.find_elements(By.XPATH, f"//li[normalize-space()='{ann_total}']")
        totalfacilities[0].click()
        rows_count = len(self.driver.find_elements(By.XPATH,
                                                   "/html/body/div[1]/div/div[2]/div/div[3]/div/div[1]/div/table/tbody/tr"))

        if rows_count >= int(ann_all_records):
            print(f'Rows are under {ann_total}')
            return True
        else:
            return False
