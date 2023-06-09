import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestCampusListing:
    def test_verify_campus_listing(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(15)
        rows = len(self.driver.find_elements(By.XPATH, "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr")) # count number of rows
        cols = len(self.driver.find_elements(By.XPATH, "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td")) # count number of columns
        print(rows)
        print(cols)
        print("Zone"+"    "+"Name"+"    "+"Street"+"    "+"Postalcode"+"       "+"Latitude"+"    "+"Longitude"+"   "+"Number of Units")
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                value = self.driver.find_element(By.XPATH, "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                print(value, end='     ')
            print()

