import json
import pytest

from .base_test import BaseTest
from .utils.config import Config


class TestCreateIssue(BaseTest):
    @pytest.mark.parametrize("issue_data,response_code", [
        ({
            "fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": BaseTest().random_string(20),
                "description": BaseTest().random_string(50),
                "issuetype": {
                    "name": "Bug"
                }
            }
        }, 201),
        ({
             "fields": {
                 "project":
                     {
                         "key": "AQAPYTHON"
                     },
                 "summary": '',
                 "description": '',
                 "issuetype": {
                     "name": ""
                 }
             }
         }, 400),
        ({
             "fields": {
                 "project":
                     {
                         "key": "AQAPYTHON"
                     },
                 "summary": BaseTest().random_string(300),
                 "description": BaseTest().random_string(3000),
                 "issuetype": {
                     "name": "Bug"
                 }
             }
         }, 400),
    ])
    def test_create_issue(self, issue_data, response_code):
        post_issue_resp = self.http.post(Config.issue_url, json.dumps(issue_data))

        assert post_issue_resp.status_code == response_code, 'Failed to post issue'
        if response_code == 201:
            self.verify_json_schema(post_issue_resp.json(), self.data.json_schema_by_name('post_issue'))
