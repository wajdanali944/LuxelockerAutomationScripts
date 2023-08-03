import string
import time
import random
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.CreateUnits import CreateUnits
from pages.CreateUser import CreateUser
from pages.HomePage import HomePage
from pynput.keyboard import Key, Controller

from utilities.recallable import call


@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateUser:

    def test_create_user_including_nothing(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        time.sleep(6)
        create_user = CreateUser(self.driver)
        create_user.click_on_new_user_button()
        create_user.enter_first_name("")
        create_user.enter_last_name("")
        create_user.enter_email_name("")
        create_user.enter_password_name("")
        create_user.enter_confirm_password_name("")
        call.recallable_disable_create_user_button(self.driver)


    def test_create_user_including_everything(self):
        home_page = HomePage(self.driver)
        home_page.enter_email_address("admin@luxelocker.com")
        home_page.enter_password("123456789aA!")
        home_page.click_on_login_button()
        time.sleep(8)
        create_user = CreateUser(self.driver)
        create_user.click_on_new_user_button()
        create_user.enter_first_name("self.random_word(6)")
        create_user.enter_last_name("self.random_word(6)")
        create_user.enter_email_name("self.random_word(6)")
        create_user.enter_password_name("self.random_word(6)")
        create_user.enter_confirm_password_name("self.random_word(6)")
        call.recallable_disable_create_user_button(self.driver)



    # def random_word(self, length=6, chars=string.ascii_lowercase):
    #     return ''.join(random.choice(chars) for i in range(length))