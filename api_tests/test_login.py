import requests
import json
import pytest

base_url = 'http://jira.hillel.it:8080'
auth_url = '/rest/auth/1/session'


@pytest.mark.parametrize("username,password,response_code", [
    ("Kirill_Vasiluk", "Kirill_Vasiluk", 200),
    ("Wrong_Username", "Kirill_Vasiluk", 401),
    ("Kirill_Vasiluk", "Wrong_Password", 401),
])
def test_login(username, password, response_code):
    application_json = {"Content-Type": "application/json"}
    payload = json.dumps({'username': username, 'password': password}, ensure_ascii=False)

    login_resp = requests.session().post(base_url + auth_url, data=payload, headers=application_json, timeout=15)
    assert login_resp.status_code == response_code
