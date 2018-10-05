from selenium.webdriver.common.by import By


# Locators
from selenium.webdriver.common.keys import Keys

user_avatar = (By.CSS_SELECTOR, ".aui-avatar")
create_button = (By.ID, "create_link")
search_input = (By.ID, "quickSearchInput")


class TopbarMenu:
    def __init__(self, driver):
        self.driver = driver

    # properties
    @property
    def user_avatar(self):
        return self.driver.find_element(*user_avatar)

    @property
    def create_button(self):
        return self.driver.find_element(*create_button)

    @property
    def search_input(self):
        return self.driver.find_element(*search_input)

    # methods
    def is_authenticated(self):
        return len(self.driver.find_elements(*user_avatar))

    def create_issue(self):
        self.create_button.click()

    def search(self, search_text):
        self.search_input.send_keys(search_text + Keys.RETURN)
