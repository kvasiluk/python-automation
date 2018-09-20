from selenium.webdriver.common.by import By

from ui_tests.pageobjects.base_page import BasePage
from utils.config import Config

# Locators
user_avatar = (By.CSS_SELECTOR, ".aui-avatar")
header_label = (By.CSS_SELECTOR, ".aui-page-header-main")


class DashboardPage(BasePage):
    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.url = "{}//{}".format(Config.jira_url, Config.dashboard_url)

    # properties
    @property
    def user_avatar(self):
        return self.driver.find_element()

    # methods
    def is_dashboard_page(self):
        dashboard_title = "System Dashboard"
        return dashboard_title in self.driver.find_element(*header_label).text and dashboard_title in self.page_title()

    def is_authenticated(self):
        return len(self.driver.find_elements(*user_avatar))
