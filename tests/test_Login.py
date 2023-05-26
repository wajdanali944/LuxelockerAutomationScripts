from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_login_with_valid_credentials():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
    driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
    # url = driver.current_url
    print(driver.current_url)
    driver.quit()


def test_login_with_invalid_email_and_valid_password():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789aA!")
    driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
    expected_warning_message = "The email you entered did not match our records. Please double-check and try again."
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, "(//span[@class='text-xs'])[1]").text.__contains__(expected_warning_message)
    # assert expected_warning_message == error_message
    driver.quit()


def test_login_with_valid_email_and_invalid_password():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@luxelocker.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234567899aA!")
    driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
    expected_warning_message = "The password you entered did not match our records. Please double-check and try again."
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)
    driver.quit()


def test_login_without_entering_credentials():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
    driver.find_element(By.XPATH, "(//button[normalize-space()='Log In'])[1]").click()
    driver.implicitly_wait(10)
    expected_warning_message = "Email is required"
    assert driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)
    driver.quit()



def generate_email_with_time_stamp():
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "wajdanali" + time_stamp + "@gmail.com"