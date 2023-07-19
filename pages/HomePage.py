from selenium.webdriver.common.by import By

from pages.SearchPage import SearchPage


class HomePage:


    def __init__(self, driver):
        self.driver = driver


    search_box_field_id = "Search"
    search_button_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeSmall css-z5jn5r'])[1]"
    email_address_field_xpath = "//input[@name='email']"
    password_field_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@type='submit']"
    side_bar_campus_section_xpath = "/html/body/div[1]/div/div[1]/ul/div[1]/div[1]/div/div[2]/span"
    side_bar_unit_section_xpath = "/html/body/div[1]/div/div[1]/ul/div[1]/div[2]/div/div[2]/span"
    side_bar_faq_section_xpath = "/html/body/div[1]/div/div[1]/ul/div[1]/div[4]/div"
    side_bar_announcement_section_xpath = "/html/body/div[1]/div/div[1]/ul/div[1]/div[5]/div/div[2]/span"



    def enter_product_into_search_box_field(self,product_name):
        self.driver.find_element(By.ID, self.search_box_field_id).click()
        self.driver.find_element(By.ID, self.search_box_field_id).clear()
        self.driver.find_element(By.ID, self.search_box_field_id).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def enter_email_address(self, email_address_text):
        self.driver.find_element(By.XPATH,self.email_address_field_xpath).click()
        self.driver.find_element(By.XPATH, self.email_address_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_address_field_xpath).send_keys(email_address_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.XPATH, self.password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_on_campus_link(self):
        self.driver.find_element(By.XPATH, self.side_bar_campus_section_xpath).click()

    def click_on_unit_link(self):
        self.driver.find_element(By.XPATH, self.side_bar_unit_section_xpath).click()

    def click_on_faq_link(self):
        self.driver.find_element(By.XPATH, self.side_bar_faq_section_xpath).click()

    def click_on_announcement_link(self):
        self.driver.find_element(By.XPATH, self.side_bar_announcement_section_xpath).click()