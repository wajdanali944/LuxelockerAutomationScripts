from selenium.webdriver.common.by import By


class  ForgotPassword:

    def __init__(self,driver):
        self.driver = driver

    forgot_your_password_button_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']"
    enter_email_field_xpath = "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input"
    send_button_xpath = "//*[@id=':r3:']"
    warning_message_xpath = "//span[@class='text-xs']"


    def click_on_forgot_password_button(self):
        self.driver.find_element(By.XPATH, self.forgot_your_password_button_xpath).click()

    def enter_email_address(self, email_address_text):
        self.driver.find_element(By.XPATH, self.enter_email_field_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_email_field_xpath).send_keys(email_address_text)

    def click_on_send_button(self):
        self.driver.find_element(By.XPATH, self.send_button_xpath).click()


    def retreive_warning_message_xpath(self):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text