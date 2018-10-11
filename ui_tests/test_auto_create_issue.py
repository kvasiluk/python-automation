import allure
import pytest

from ui_tests.base_test import BaseTest
from ui_tests.constants import *

step = allure.step


@allure.feature("Create issue")
class TestCreateIssue(BaseTest):
    @pytest.mark.ui
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("summary,description,issue_type", [
        (summary_short, description_short, 'Bug'),
    ])
    def test_create_issue(self, summary, description, issue_type):
        with step("Create a new issue with all required fields"):
            self.pages.dashboard_page.click_create()

            create_issue_page = self.pages.create_issue_page
            create_issue_page.wait_for_page()
            create_issue_page.create_issue(issue_type, summary, description)

            assert "successfully created" in self.pages.dashboard_page.issue_created_message, "Issue creation failed"

    @pytest.mark.ui
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("summary,description,issue_type", [
        ('', '', ''),
        (summary_long, description_long, 'Bug'),
    ])
    def test_create_issue_negative(self, summary, description, issue_type):
        with step("Create a new issue with missing required fields and values too long"):
            self.pages.dashboard_page.click_create()

            create_issue_page = self.pages.create_issue_page
            create_issue_page.wait_for_page()
            create_issue_page.create_issue(issue_type, summary, description)

            assert create_issue_page.is_create_issue_page(), "Create Issue form closed after failed creation"
            create_issue_page.cancel_creation()

