# pages/login_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators using XPath
        self.email_input = (By.XPATH, "//input[@id='input-email']")
        self.password_input = (By.XPATH, "//input[@id='input-password']")
        self.login_button = (By.XPATH, "//input[@value='Login']")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

