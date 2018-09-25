from selenium.webdriver.common.by import By


# Locators
user_avatar = (By.CSS_SELECTOR, ".aui-avatar")
create_button = (By.ID, "create_link")


class TopbarMenu:
    def __init__(self, driver):
        self.driver = driver

    # properties
    @property
    def user_avatar(self):
        return self.driver.find_element(user_avatar)

    @property
    def create_button(self):
        return self.driver.find_element(create_button)

    # methods
    def is_authenticated(self):
        return len(self.driver.find_elements(*user_avatar))

    def create_issue(self):
        self.create_button.click()
