from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_tests.pageobjects.base_page import BasePage
from utils.config import Config

# Locators
issue_items = (By.CSS_SELECTOR, ".search-results li")
no_results_message = (By.CSS_SELECTOR, ".no-results-message")


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super(SearchResultsPage, self).__init__(driver)
        self.url = "{}//{}".format(Config.jira_url, Config.dashboard_url)

    # properties
    @property
    def issues(self):
        return self.driver.find_elements(*issue_items)

    @property
    def result_count(self):
        return len(self.driver.find_elements(*issue_items))

    # methods
    def is_no_issues_found(self):
        return len(self.driver.find_elements(*no_results_message))

    def wait_for_results(self):
        wait = WebDriverWait(self.driver, 10)
        if not self.is_no_issues_found():
            wait.until(ec.presence_of_all_elements_located(issue_items))

    def validate_results(self, results=None):
        if results:
            return self.result_count == results

        return self.is_no_issues_found()
