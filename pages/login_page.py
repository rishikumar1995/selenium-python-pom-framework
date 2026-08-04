from selenium.webdriver.common.by import By
from pages.base_page import BasePage
# Reports Feature Branch Demo

class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.find(self.username).send_keys(username)

    def enter_password(self, password):
        self.find(self.password).send_keys(password)

    def click_login_button(self):
        self.find(self.login_button).click()

    def get_error_message(self):
        return self.find(self.error_message).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()