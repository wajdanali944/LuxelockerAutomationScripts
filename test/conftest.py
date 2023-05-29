import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    driver = None
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        print("Provide a valid browser name from this list chrome/firefox")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
