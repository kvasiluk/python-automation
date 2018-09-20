from selenium.webdriver.common.by import By

from ui_tests.pageobjects.base_page import BasePage
from utils.config import Config


# Locators
login_edit = (By.ID, "login-form-username")
password_edit = (By.ID, "login-form-password")
login_button = (By.ID, "login-form-submit")
error_message = (By.CSS_SELECTOR, ".aui-message.error")


class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.url = "{}//{}".format(Config.jira_url, Config.login_url)

    # properties
    @property
    def email_edit(self):
        return self.driver.find_element(*login_edit)

    @property
    def password_edit(self):
        return self.driver.find_element(*password_edit)

    @property
    def login_button(self):
        return self.driver.find_element(*login_button)

    @property
    def error_message(self):
        return self.driver.find_element(*error_message)

    # methods
    def is_login_page(self):
        return len(self.driver.find_elements(*login_button)) and "Log in" in self.page_title()

    def fill_credentials(self, username=Config.username, password=Config.password):
        self.email_edit.clear()
        self.email_edit.send_keys(username)
        self.password_edit.clear()
        self.password_edit.send_keys(password)
        self.email_edit.click()

    def login(self, username=Config.username, password=Config.password):
        self.fill_credentials(username, password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text
