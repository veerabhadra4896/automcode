
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost/opencart/upload/")
    yield driver
    driver.quit()

