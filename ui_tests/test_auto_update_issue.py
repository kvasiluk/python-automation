import allure
import pytest

from .base_test import BaseTest

step = allure.step


@allure.feature("Update issue")
class TestUpdateIssue(BaseTest):
    @pytest.mark.ui
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("update_data", [
        {'summary': 'This field was changed from UI'},
        {'priority': 'High'},
        {'assignee': 'Kirill Vasiluk'}
    ])
    def test_update_issue(self, update_data, create_issue_for_update):
        with step("Update existing issue fields"):
            issue_page = self.pages.issue_page
            issue_page.open_issue(create_issue_for_update)
            issue_page.update_issue(update_data)

            assert issue_page.validate_data(update_data), "Failed to update issue"
