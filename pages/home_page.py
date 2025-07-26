from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        myaccount_dropdown = (By.XPATH, "//span[normalize-space()='My Account']")
        login_menu = (By.XPATH, "//span[normalize-space()='Login']")
        register_menu = (By.XPATH, "//span[normalize-space()='Register']")
    def open(self, url):
        self.driver.get(url)

    def open_login_page(self):
        self.driver.find_element(*self.myaccount_dropdown).click()
        self.driver.find_element(*self.login_menu).click()

    def open_register_page(self):
        self.driver.find_element(*self.myaccount_dropdown).click()
        self.driver.find_element(*self.register_menu).click()

