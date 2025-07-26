# pages/home_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.myaccount_menu = (By.XPATH, "//span[normalize-space()='My Account']")
        self.login_menu = (By.XPATH, "//a[normalize-space()='Login']")
        self.register_menu = (By.XPATH, "//a[normalize-space()='Register']")

    def open_login_page(self):
        self.driver.find_element(*self.myaccount_menu).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.login_menu)
        ).click()

    def open_register_page(self):
        self.driver.find_element(*self.myaccount_menu).click()
        time.sleep(2)
        self.driver.find_element(*self.register_menu).click()
