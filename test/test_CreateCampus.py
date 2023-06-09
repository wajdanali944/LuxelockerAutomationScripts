import string
import time
import random
import pytest
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.recallable import call
from pages.CreateCampus import CreateCampus
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateCampus:
    def test_creating_campus_including_all_values(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(8)
        create_campus = CreateCampus(self.driver)
        create_campus.click_on_create_campus_button()
        time.sleep(6)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//p[normalize-space()="Select"]'))).click()  # clicking on select option
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "(//p[normalize-space()='Arizona'])[1]"))).click()  # clicking on dropdown options
        call.recallable_button(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))).send_keys(
            self.random_word(6))  # entering name
        create_campus.enter_campus_street("77 virg block")
        create_campus.enter_campus_postalcode("8790")
        create_campus.enter_campus_numberofunits("100")
        create_campus.enter_campus_longitude("10014")
        create_campus.enter_campus_latitude("20014")
        create_campus.enter_campus_maintenanceFee("200")
        create_campus.click_on_active_checkbox()
        call.recallable_button(self.driver)
        self.driver.implicitly_wait(4)
        call.recallable_button(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[normalize-space()='Air Conditioner']"))).click()  # selecting Air Conditioner
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[normalize-space()='Security Camera']"))).click()  # selecting security camera
        call.recallable_button(self.driver)

    def test_creating_campus_without_selecting_select_dropdown(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(8)
        create_campus = CreateCampus(self.driver)
        create_campus.click_on_create_campus_button()
        time.sleep(6)
        call.recallable_disable_button(self.driver)

    def test_creating_campus_with_existed_name(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(8)
        create_campus = CreateCampus(self.driver)
        create_campus.click_on_create_campus_button()
        time.sleep(6)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//p[normalize-space()="Select"]'))).click()  # clicking on select option
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "(//p[normalize-space()='Arizona'])[1]"))).click()  # clicking on dropdown options
        call.recallable_button(self.driver)
        call.recallable_campus_name_already_exists(self.driver)

    def test_creating_campus_without_entering_anything_in_details_section(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_campus_link()
        self.driver.implicitly_wait(8)
        create_campus = CreateCampus(self.driver)
        create_campus.click_on_create_campus_button()
        time.sleep(6)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//p[normalize-space()="Select"]'))).click()  # clicking on select option
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "(//p[normalize-space()='Arizona'])[1]"))).click()  # clicking on dropdown options
        call.recallable_button(self.driver)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(
            "")  # entering name
        create_campus = CreateCampus(self.driver)
        create_campus.enter_campus_street("")
        create_campus.enter_campus_postalcode("")
        create_campus.enter_campus_numberofunits("")
        create_campus.enter_campus_longitude("")
        create_campus.enter_campus_latitude("")
        create_campus.enter_campus_maintenanceFee("")
        create_campus.click_on_active_checkbox()
        call.recallable_disable_button(self.driver)

    def random_word(self, length=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for i in range(length))
