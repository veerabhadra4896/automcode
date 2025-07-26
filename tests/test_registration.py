
import pytest
import time
import random
from pages.home_page import HomePage
from pages.registration_page import RegisterPage


def generate_unique_email():
    return f"testuser{random.randint(1000, 9999)}@demo.com"

def test_registration_new_user(driver):
    home = HomePage(driver)
    home.open_register_page()
    time.sleep(5)
    register = RegisterPage(driver)
    register.register(
        firstname_input="john",
        lastname_input = "Doe",
        email_input= "vb@gmail.com",
        phone_input= "1234523",
        password_input="test@123"
    )

    assert "Your Account Has Been Created!" in driver.page_source


    time.sleep(2)
