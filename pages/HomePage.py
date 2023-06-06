from selenium.webdriver.common.by import By


class HomePage:


    def __init__(self, driver):
        self.driver = driver


    search_box_field_id = "Search"
    search_button_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorSecondary MuiSvgIcon-fontSizeSmall css-z5jn5r'])[1]"

    def enter_product_into_search_box_field(self,product_name):
        self.driver.find_element(By.ID, self.search_box_field_id).click()
        self.driver.find_element(By.ID, self.search_box_field_id).clear()
        self.driver.find_element(By.ID, self.search_box_field_id).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

