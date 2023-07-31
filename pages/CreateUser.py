import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By


class CreateUser:


    def __init__(self, driver):
        self.driver = driver

    create_user_button_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/span/p"
    enter_first_name_field_name = "fName"
    enter_last_name_field_name = "lName"
    enter_email_field_name = "email"
    enter_password_field_name = "password"
    enter_confirm_password_field_name = "confirmPassword"



    def click_on_new_user_button(self):
        self.driver.find_element(By.XPATH, self.create_user_button_xpath).click()

    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.NAME, self.enter_first_name_field_name).click()
        self.driver.find_element(By.NAME, self.enter_first_name_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_first_name_field_name).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.NAME, self.enter_last_name_field_name).click()
        self.driver.find_element(By.NAME, self.enter_last_name_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_last_name_field_name).send_keys(last_name_text)

    def enter_email_name(self, email_text):
        self.driver.find_element(By.NAME, self.enter_email_field_name).click()
        self.driver.find_element(By.NAME, self.enter_email_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_email_field_name).send_keys(email_text)

    def enter_password_name(self, password_text):
        self.driver.find_element(By.NAME, self.enter_password_field_name).click()
        self.driver.find_element(By.NAME, self.enter_password_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_password_field_name).send_keys(password_text)

    def enter_confirm_password_name(self, password_text):
        self.driver.find_element(By.NAME, self.enter_confirm_password_field_name).click()
        self.driver.find_element(By.NAME, self.enter_confirm_password_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_confirm_password_field_name).send_keys(password_text)