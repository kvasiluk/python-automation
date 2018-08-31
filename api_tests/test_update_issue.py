import json

import pytest

from .base_test import BaseTest
from .utils.config import Config


class TestUpdateIssue(BaseTest):
    @pytest.mark.parametrize("issue_data,response_code", [
        ({
             "fields": {
                 "summary": "This field was changed by REST"
             }
         }, 204),
        ({
             "fields": {
                 "priority": {"name": "High"}
             }
         }, 204),
        ({
             "fields": {
                 "assignee": {"name": "Kirill_Vasiluk"}
             }
         }, 204),
    ])
    def test_update_issue(self, issue_data, response_code, create_issue_for_update):
        issue_url = "%s/%s" % (Config.issue_url, create_issue_for_update)
        update_issue_resp = self.http.put(issue_url, json.dumps(issue_data))

        assert update_issue_resp.status_code == response_code, 'Failed to update issue'
