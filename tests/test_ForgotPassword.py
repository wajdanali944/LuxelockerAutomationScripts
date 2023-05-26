from selenium import webdriver
from selenium.webdriver.common.by import By


def test_forgot_password_with_non_existed_email():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']").click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input").send_keys("wajdanali933@gmail.com")
    driver.find_element(By.XPATH, "//*[@id=':r3:']").click()
    expected_warning_message = "Something went wrong"
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)
    # url = driver.current_url
    print(driver.current_url)
    driver.quit()


def test_forgot_password_with_existed_email():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']").click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input").send_keys("hirat917+45@gmail.com")
    driver.find_element(By.XPATH, "//*[@id=':r3:']").click()
    driver.implicitly_wait(5)
    driver.get("https://app-staging.luxelocker.com/")
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/p")
    print(element.get_attribute('href'))
    # url = driver.current_url
    #print(driver.current_url)
    driver.quit()

def test_forgot_password_without_entering_email():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://app-staging.luxelocker.com/")
    driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1i7v4ob']").click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/form/div/div[1]/div/input").send_keys("")
    driver.find_element(By.XPATH, "//*[@id=':r3:']").click()
    driver.implicitly_wait(5)
    expected_warning_message = "Email is required"
    driver.implicitly_wait(3)
    assert driver.find_element(By.XPATH, "//span[@class='text-xs']").text.__contains__(expected_warning_message)
    # url = driver.current_url
    #print(driver.current_url)
    driver.quit()