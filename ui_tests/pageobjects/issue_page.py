from time import sleep

from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_tests.pageobjects.base_page import BasePage
from utils.config import Config

# Locators
issue_header = (By.CSS_SELECTOR, ".issue-header-content")
summary_edit = (By.ID, "summary-val")
priority_edit = (By.ID, "priority-val")
assignee_edit = (By.ID, "assignee-val")
input_edit = (By.TAG_NAME, "input")
loading_spinner = (By.CSS_SELECTOR, ".overlay-icon.throbber")


class IssuePage(BasePage):
    def __init__(self, driver):
        super(IssuePage, self).__init__(driver)
        self.url = "{}/browse/".format(Config.jira_url)

    # properties
    @property
    def summary(self):
        return self.driver.find_element(*summary_edit)

    @property
    def priority(self):
        return self.driver.find_element(*priority_edit)

    @property
    def assignee(self):
        return self.driver.find_element(*assignee_edit)

    # methods
    def is_issue_page(self):
        return len(self.driver.find_elements(*issue_header))

    def open_issue(self, key):
        self.url += key
        self.driver.get(self.url)

    @staticmethod
    def __get_input__(field):
        wait = WebDriverWait(field, 10)
        return wait.until(ec.presence_of_element_located(input_edit))

    def set_field(self, field, value):
        f = getattr(self, field, None)
        wait = WebDriverWait(f, 5)

        if not f:
            print("Changing {} is not supported".format(field))
            return

        f.click()
        input_element = self.__get_input__(f)
        input_element.send_keys(value)
        sleep(1)
        input_element.send_keys(Keys.ENTER)
        if input_element.is_enabled():
            input_element.send_keys(Keys.ALT, "s")
        wait.until(ec.invisibility_of_element_located(loading_spinner))

    def update_issue(self, issue_data):
        for k, v in issue_data.items():
            self.set_field(k, v)

    def validate_data(self, issue_data):
        self.go_to()
        for k, v in issue_data.items():
            f = getattr(self, k, None)

            if not f:
                print("{} is not supported".format(k))
                continue

            if v != f.text:
                return False

        return True
