import json

import allure
import pytest

from .base_test import BaseTest, random_string
from utils.config import Config
from tests_data.json_object.json_data import create_issue_json

step = allure.step


@allure.feature("Create issue")
class TestCreateIssue(BaseTest):
    @pytest.mark.api
    @pytest.mark.parametrize("issue_data,response_code", [
        (create_issue_json(random_string(10), random_string(20), 'Bug'), 201),
        (create_issue_json('', '', ''), 400),
        (create_issue_json(random_string(300), random_string(3000), 'Bug'), 400),
    ])
    def test_create_issue(self, issue_data, response_code):
        with step("Send POST to issue url containing new issue data"):
            post_issue_resp = self.http.post(Config.issue_url, json.dumps(issue_data))

            assert post_issue_resp.status_code == response_code, 'Failed to post issue'
            if response_code == 201:
                self.verify_json_schema(post_issue_resp.json(), self.data.json_schema_by_name('post_issue'))
