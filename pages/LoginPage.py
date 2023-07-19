from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver


    warning_message_xpath = "//span[@class='errorText_12'][1]"


    def retrieve_warning_message(self):
       return self.driver.find_element(By.XPATH, self.warning_message_xpath).text
