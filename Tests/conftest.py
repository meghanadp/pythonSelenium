import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.Config import TestData

"""initialise driver with python fixtures and params"""


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))  # access directly since TestBase is Static class
    if request.param == "firefox":
        driver = webdriver.firefox(executable_path=TestData.Gecko_Driver)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()
