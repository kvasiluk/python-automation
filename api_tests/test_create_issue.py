import json
import pytest

from api_tests.common.http_request import BaseHttp
from .base_test import BaseTest

issue_url = 'rest/api/2/issue'


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
        post_issue_resp = self.http.post(issue_url, json.dumps(issue_data))

        assert post_issue_resp.status_code == response_code, 'Failed to post issue'
