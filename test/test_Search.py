import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789Ll!@")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(20)
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Miami")
        search_page = home_page.click_on_search_button()
        assert search_page.display_status_of_campus_name()

    def test_search_for_a_non_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789Ll!@")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("----asdf---")
        search_page = home_page.click_on_search_button()
        expected_warning_message = "No data found."
        assert search_page.retrieve_no_campus_name_message().__eq__(expected_warning_message)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789Ll!@")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span").click()
        self.driver.implicitly_wait(15)
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        try:
         elem_disabled = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeSmall css-z5jn5r'])[1]"))).is_enabled()

         elem_disabled.click()

        except:
            print("Search button is disabled.")
            pass
