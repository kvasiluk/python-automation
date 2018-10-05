from selenium.webdriver.common.by import By

from ui_tests.pageobjects.base_page import BasePage
from utils.config import Config

# Locators
header_label = (By.CSS_SELECTOR, ".aui-page-header-main")
create_button = (By.ID, "create_link")
issue_created_message = (By.CSS_SELECTOR, ".aui-message-success")


class DashboardPage(BasePage):
    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.url = "{}//{}".format(Config.jira_url, Config.dashboard_url)

    # properties
    @property
    def create_button(self):
        return self.driver.find_element(*create_button)

    @property
    def issue_created_message(self):
        return self.driver.find_element(*issue_created_message).text

    # methods
    def is_dashboard_page(self):
        dashboard_title = "System Dashboard"
        return dashboard_title in self.driver.find_element(*header_label).text and dashboard_title in self.page_title()

    def click_create(self):
        self.create_button.click()
