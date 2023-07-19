import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By


class CreateUnits:

    def __init__(self, driver):
        self.driver = driver

    create_units_button_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/span[2]/span[1]"
    enter_width_field_name = "width"
    enter_length_field_name = "length"
    enter_description_field_css_selector = "textarea.h-24"
    not_enter_anything_in_Sq_Ft_field_xpath = ".//*[@name='length']/following::div[2]/div/div[1]"
    not_enter_anything_in_Maintenance_Fee_field_xpath = ".//*[@class='mt-5 undefined w-full']/following::div[2]/div"
    available_for_lease_checkbox_xpath = "/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[5]/div[1]/div[2]/label/span[2]"
    available_for_sale_checkbox_xpath = ".//*[@class='flex items-center justify-start ']/following::span"
    enter_lease_price_name = "leasePrice"
    enter_buy_price_name = "buyPrice"
    active_xpath = "(//input[@type='checkbox'])[23]"

    def click_on_new_unit_button(self):
        self.driver.find_element(By.XPATH, self.create_units_button_xpath).click()

    def enter_width(self, unit_width_text):
        self.driver.find_element(By.NAME, self.enter_width_field_name).click()
        self.driver.find_element(By.NAME, self.enter_width_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_width_field_name).send_keys(unit_width_text)

    def enter_length(self, unit_length_text):
        self.driver.find_element(By.NAME, self.enter_length_field_name).click()
        self.driver.find_element(By.NAME, self.enter_length_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_length_field_name).send_keys(unit_length_text)

    def enter_description(self, unit_description_text):
        self.driver.find_element(By.CSS_SELECTOR, self.enter_description_field_css_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.enter_description_field_css_selector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.enter_description_field_css_selector).send_keys(unit_description_text)

    def Not_enter_Sq_Ft(self):
        self.driver.find_element(By.XPATH, self.not_enter_anything_in_Sq_Ft_field_xpath)

    def Not_enter_Maintenance_Fee(self):
        self.driver.find_element(By.XPATH, self.not_enter_anything_in_Maintenance_Fee_field_xpath)

    def click_on_available_for_lease_checkbox(self):
        self.driver.find_element(By.XPATH, self.available_for_lease_checkbox_xpath).click()

    def click_on_available_for_sale_checkbox(self):
        self.driver.find_element(By.XPATH, self.available_for_sale_checkbox_xpath).click()

    def enter_lease_price(self, unit_leaseprice_text):
        self.driver.find_element(By.NAME, self.enter_lease_price_name).click()
        self.driver.find_element(By.NAME, self.enter_lease_price_name).clear()
        self.driver.find_element(By.NAME, self.enter_lease_price_name).send_keys(unit_leaseprice_text)

    def enter_buy_price(self, unit_buyprice_text):
        self.driver.find_element(By.NAME, self.enter_buy_price_name).click()
        self.driver.find_element(By.NAME, self.enter_buy_price_name).clear()
        self.driver.find_element(By.NAME, self.enter_buy_price_name).send_keys(unit_buyprice_text)

    def click_on_active_checkbox(self):
        self.driver.find_element(By.XPATH, self.active_xpath).click()
