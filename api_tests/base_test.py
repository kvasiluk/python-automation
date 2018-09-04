import random
import string
import pytest
import json

from tests_data.tests_data import TestsData
from .utils.jsonschemaerror import check_json

from api_tests.common.http_request import BaseHttp


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


class BaseTest(object):
    http = BaseHttp()
    data = TestsData()

    @pytest.fixture
    def clear_session(self):
        """ Clear session headers """

        self.http.session.headers.clear()

    @pytest.fixture(scope='session', autouse=True)
    def set_session_cookie(self):
        """ Set authentication cookie to session by executing login on session level """

        payload = json.dumps({'username': 'Kirill_Vasiluk', 'password': 'Kirill_Vasiluk'}, ensure_ascii=False)

        login_resp = self.http.post('rest/auth/1/session', payload)

        self.http.update_auth_header(login_resp)

    @pytest.fixture()
    def create_issue_for_update(self):
        """Creates a new issue at setup, yields its key, deletes issue on teardown"""
        issue_data = {
            "fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": random_string(20),
                "description": random_string(50),
                "issuetype": {
                    "name": "Bug"
                }
            }
        }
        issue_key = self.http.post("rest/api/2/issue", json.dumps(issue_data)).json()["key"]
        yield issue_key
        self.http.delete("rest/api/2/issue/%s" % issue_key)

    def verify_json_schema(self, json_object, schema, iter_=False):
        """
        :param json_object: dict-like JSON object to verify
         :type json_object: dict
        :param schema: json schema object
         :type schema: dict
        :param iter_: iter over list
        :return:
        """
        if iter_:
            for js in json_object:
                check_json(js, schema)
        else:
            check_json(json_object, schema)
