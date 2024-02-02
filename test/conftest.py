import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup_and_teardown(request):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://app-staging.luxelocker.com/")
        request.cls.driver = driver
        yield
    finally:
        if hasattr(request.cls, 'driver'):
           request.cls.driver.quit()