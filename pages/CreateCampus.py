from selenium.webdriver.common.by import By


class CreateCampus:

    def __init__(self, driver):
        self.driver = driver

    create_campus_button_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/span/span[1]"
    enter_campus_street_field_name = "street"
    enter_campus_postal_code_field_name = "postalCode"
    enter_campus_phone_number_field_name = "phone"
    enter_campus_number_of_units_field_name = "numOfUnits"
    enter_campus_longitude_field_name = "longitude"
    enter_campus_latitude_field_name = "latitude"
    enter_campus_maintenanceFee_field_name = "maintenanceFee"
    checkbox_active_xpath = "//label[contains(@color,'#FFFFFF')]//input[contains(@type,'checkbox')]"


    def click_on_create_campus_button(self):
        self.driver.find_element(By.XPATH, self.create_campus_button_xpath).click()

    def enter_campus_street(self,campus_street_text):
        self.driver.find_element(By.NAME, self.enter_campus_street_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_street_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_street_field_name).send_keys(campus_street_text)

    def enter_campus_postalcode(self,postal_code_text):
        self.driver.find_element(By.NAME, self.enter_campus_postal_code_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_postal_code_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_postal_code_field_name).send_keys(postal_code_text)

    def enter_campus_phone(self,phone_number_text):
        self.driver.find_element(By.NAME, self.enter_campus_phone_number_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_phone_number_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_phone_number_field_name).send_keys(phone_number_text)


    def enter_campus_numberofunits(self,number_of_units_text):
        self.driver.find_element(By.NAME, self.enter_campus_number_of_units_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_number_of_units_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_number_of_units_field_name).send_keys(number_of_units_text)

    def enter_campus_longitude(self, longitude_text):
        self.driver.find_element(By.NAME, self.enter_campus_longitude_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_longitude_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_longitude_field_name).send_keys(longitude_text)

    def enter_campus_latitude(self, latitude_text):
        self.driver.find_element(By.NAME, self.enter_campus_latitude_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_latitude_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_latitude_field_name).send_keys(latitude_text)

    def enter_campus_maintenanceFee(self, maintenanceFee_text):
        self.driver.find_element(By.NAME, self.enter_campus_maintenanceFee_field_name).click()
        self.driver.find_element(By.NAME, self.enter_campus_maintenanceFee_field_name).clear()
        self.driver.find_element(By.NAME, self.enter_campus_maintenanceFee_field_name).send_keys(maintenanceFee_text)

    def click_on_active_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_active_xpath).click()
