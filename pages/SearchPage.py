from selenium.webdriver.common.by import By


class SearchPage:


    def __init__(self, driver):
        self.driver = driver


    valid_campus_name_xpath = "//*[@id='simple-tabpanel-0']/div/div[2]/div/div[1]/div/table/tbody/tr/td[2]"
    no_campus_name_message_xpath = "//p[@class='mt-2']"

    def display_status_of_campus_name(self):
        return self.driver.find_element(By.XPATH, self.valid_campus_name_xpath).is_displayed()

    def retrieve_no_campus_name_message(self):
        return self.driver.find_element(By.XPATH, self.no_campus_name_message_xpath).text

