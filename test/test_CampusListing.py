import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup_and_teardown")
class TestCampusListing:
    def test_verify_campus_listing(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
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

