import json
import pytest

from api_tests.common.http_request import BaseHttp
from .base_test import BaseTest

auth_url = 'rest/auth/1/session'


class TestLogin(BaseTest):
    @pytest.mark.parametrize("username,password,response_code", [
        ("Kirill_Vasiluk", "Kirill_Vasiluk", 200),
        ("Wrong_Username", "Kirill_Vasiluk", 401),
        ("Kirill_Vasiluk", "Wrong_Password", 401),
    ])
    def test_login(self, username, password, response_code):
        http = BaseHttp()
        payload = json.dumps({'username': username, 'password': password}, ensure_ascii=False)

        login_resp = http.post(auth_url, payload)
        assert login_resp.status_code == response_code, "Failed to login"
