from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname_input = (By.ID,"input-firstname")
        self.lastname_input = (By.ID,"input-lastname")
        self.email_input = (By.ID,"input-email")
        self.phone_input = (By.ID,"input-telephone")
        self.password_input = (By.ID,"input-password")
        self.confirm_password_input = (By.ID,"input-confirm")
        self.policy_checkbox = (By.XPATH,"//input[@name='agree']")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")

    def register(self,firstname_input,lastname_input,email_input,phone_input,password_input):
        self.driver.find_element(*self.firstname_input).send_keys(firstname_input)
        self.driver.find_element(*self.lastname_input).send_keys(lastname_input)
        self.driver.find_element(*self.email_input).send_keys(email_input)
        self.driver.find_element(*self.phone_input).send_keys(phone_input)
        self.driver.find_element(*self.password_input).send_keys(password_input)
        self.driver.find_element(*self.confirm_password_input).send_keys(password_input)
        self.driver.find_element(*self.policy_checkbox).click()
        self.driver.find_element(*self.continue_button).click()


