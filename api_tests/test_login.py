import requests
import json

base_url = 'http://jira.hillel.it:8080'
auth_url = '/rest/auth/1/session'


def test_login_positive():
    username = 'Kirill_Vasiluk'
    password = 'Kirill_Vasiluk'
    application_json = {"Content-Type": "application/json"}
    payload = json.dumps({'username': username, 'password': password}, ensure_ascii=False)

    login_resp = requests.session().post(base_url + auth_url, data=payload, headers=application_json, timeout=15)
    assert login_resp.status_code == 200


def test_login_negative_wrong_username():
    username = 'Wrong_Username'
    password = 'Kirill_Vasiluk'
    application_json = {"Content-Type": "application/json"}
    payload = json.dumps({'username': username, 'password': password}, ensure_ascii=False)

    login_resp = requests.session().post(base_url + auth_url, data=payload, headers=application_json, timeout=15)
    assert login_resp.status_code == 401


def test_login_negative_wrong_password():
    username = 'Kirill_Vasiluk'
    password = 'Wrong_Password'
    application_json = {"Content-Type": "application/json"}
    payload = json.dumps({'username': username, 'password': password}, ensure_ascii=False)

    login_resp = requests.session().post(base_url + auth_url, data=payload, headers=application_json, timeout=15)
    assert login_resp.status_code == 401
