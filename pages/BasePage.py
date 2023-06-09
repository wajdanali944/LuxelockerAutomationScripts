from utilities import ConfigReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS_SELECTOR"):
            self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_TAG_NAME"):
            self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_LINK_TEXT"):
            self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).click()

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS_SELECTOR"):
            self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_TAG_NAME"):
            self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_LINK_TEXT"):
            self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS_SELECTOR"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR,
                                                ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            dropdown = self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_TAG_NAME"):
            dropdown = self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_LINK_TEXT"):
            dropdown = self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            dropdown = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                                ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASS_NAME"):
            dropdown = self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).send_keys(
                value)
        select = Select()
        select.select_by_visible_text(value)

    def go_to_element(self, locator):
        if str(locator).endswith("_XPATH"):
            count = self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS_SELECTOR"):
            count = self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            count = self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_NAME"):
            count = self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_TAG_NAME"):
            count = self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_LINK_TEXT"):
            count = self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_PARTIAL_LINK_TEXT"):
            count = self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CLASS_NAME"):
            count = self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator))