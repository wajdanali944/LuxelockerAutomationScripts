import string
import time
import random
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.CreateUnits import CreateUnits
from pages.HomePage import HomePage
from pynput.keyboard import Key, Controller

from utilities.recallable import call


@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateUnits:

    def test_creating_units_including_all_values(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        self.driver.implicitly_wait(10)
        home_page.click_on_unit_link()
        self.driver.implicitly_wait(10)
        create_unit = CreateUnits(self.driver)
        create_unit.click_on_new_unit_button()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//p[normalize-space()="Select"]'))).click()  # clicking on select option
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//p[normalize-space()='Miami Campus'][1])"))).click()  # clicking on dropdown options
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='unitNum']"))).send_keys(
            self.random_word(6))  # entering name
        create_unit.enter_width("898")
        create_unit.enter_length("24")
        self.driver.implicitly_wait(5)
        create_unit.Not_enter_Sq_Ft()
        create_unit.Not_enter_Maintenance_Fee()
        create_unit.enter_description("This is a new unit")
        create_unit.click_on_available_for_lease_checkbox()
        create_unit.click_on_available_for_sale_checkbox()
        create_unit.enter_lease_price("100")
        self.driver.implicitly_wait(3)
        create_unit.enter_buy_price("900")
        self.driver.find_element(By.XPATH, "//p[normalize-space()='+Upload images']").click()
        time.sleep(3)
        keyboard = Controller()
        keyboard.type("C:\\Users\\HP\\PycharmProjects\\Luxelocker\\Files\\IMG_0573.jpg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        self.driver.implicitly_wait(6)
        create_unit.click_on_active_checkbox()
        self.driver.implicitly_wait(6)
        call.recallable_save_button(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/span[2]")





    def random_word(self, length=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for i in range(length))