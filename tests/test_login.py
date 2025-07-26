# tests/test_login.py

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(driver):
    # Navigate to login page
    home = HomePage(driver)
    home.open_login_page()

    # Perform login
    login = LoginPage(driver)
    login.login("vee@gmail.com", "demo")  # 🔁 Replace with your actual login credentials

    # Assertion: check that user is logged in
    assert "My Account" in driver.title or "Logout" in driver.page_source
