from enum import Enum

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_tests.pageobjects.base_page import BasePage
from utils.config import Config

# Locators
dialog_header = (By.CSS_SELECTOR, ".jira-dialog-heading")
project_edit = (By.ID, "project-field")
issue_type_edit = (By.ID, "issuetype-field")
summary_edit = (By.ID, "summary")
description_edit = (By.ID, "description-wiki-edit")
create_button = (By.ID, "create-issue-submit")
cancel_button = (By.CSS_SELECTOR, "a.cancel")
summary_error_label = (By.CSS_SELECTOR, ".error")


class IssueType(Enum):
    BUG = "Bug"
    EPIC = "Epic"
    USERSTORY = "User Story"
    TEST = "Test"
    TASK = "Task"
    STORY = "Story"


class CreateIssuePage(BasePage):
    def __init__(self, driver):
        super(CreateIssuePage, self).__init__(driver)
        self.url = "{}//{}".format(Config.jira_url, Config.create_issue_url)
        self.wait = WebDriverWait(self.driver, 10)

    # properties
    @property
    def project_edit(self):
        return self.wait.until(ec.element_to_be_clickable(project_edit))

    @property
    def issue_type_edit(self):
        return self.wait.until(ec.element_to_be_clickable(issue_type_edit))

    @property
    def summary_edit(self):
        return self.wait.until(ec.element_to_be_clickable(summary_edit))

    @property
    def description_edit(self):
        return self.wait.until(ec.element_to_be_clickable(description_edit))

    @property
    def create_button(self):
        return self.wait.until(ec.element_to_be_clickable(create_button))

    @property
    def cancel_button(self):
        return self.driver.find_element(*cancel_button)

    @property
    def summary_error(self):
        return self.driver.find_element(summary_error_label).text

    # methods
    def is_create_issue_page(self):
        header_title = "Create Issue"
        return header_title in self.driver.find_element(*dialog_header).text and header_title in self.page_title()

    def wait_for_page(self):
        self.wait.until(ec.presence_of_element_located(dialog_header))

    def fill_with(self, issue_type=IssueType.BUG, summary="Default", desc="Default"):
        self.project_edit.clear()
        self.project_edit.send_keys(Config.project_key + Keys.RETURN)
        self.issue_type_edit.clear()
        self.issue_type_edit.send_keys(issue_type + Keys.RETURN)
        self.summary_edit.clear()
        self.summary_edit.send_keys(summary)
        # self.description_edit.clear()
        # self.description_edit.send_keys(desc)

    def create_issue(self, issue_type=IssueType.BUG, summary="Default", desc="Default"):
        self.fill_with(issue_type, summary, desc)
        self.create_button.click()
        self.wait_for_issue_created()

    def wait_for_issue_created(self):
        try:
            self.wait.until(ec.invisibility_of_element_located(dialog_header))
        except TimeoutException:
            print("Issue creation failed")

    def cancel_creation(self):
        self.cancel_button.click()
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except:
            print("No alert")
