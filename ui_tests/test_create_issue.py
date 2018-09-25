import json

import pytest

from api_tests.base_test import random_string
from ui_tests.base_test import BaseTest


class TestCreateIssue(BaseTest):
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("summary,description,issue_type,fail_expected", [
        (random_string(10), random_string(20), 'Bug', False),
        ('', '', '', True),
        (random_string(300), random_string(3000), 'Bug', True),
    ])
    def test_create_issue(self, summary, description, issue_type, fail_expected):
        self.pages.dashboard_page.click_create()

        create_issue_page = self.pages.create_issue_page
        create_issue_page.wait_for_page()
        create_issue_page.create_issue(issue_type, summary, description)

        if fail_expected:
            assert create_issue_page.is_create_issue_page(), "Create Issue form closed after failed creation"
            create_issue_page.cancel_creation()
        else:
            assert "successfully created" in self.pages.dashboard_page.issue_created_message, "Issue creation failed"
