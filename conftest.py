import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from api_tests.base_test import random_string
from tests_data.json_object.json_data import create_issue_json
from api_tests.common.http_request import BaseHttp
from utils.config import Config

http = BaseHttp()


@pytest.fixture(scope="session")
def up_browser(request):
    """ SetUp/TearDown selenium driver """

    d = None
    if Config.browser == 'chrome':
        options = webdriver.ChromeOptions()
        if Config.headless:
            options.add_argument("--headless")
        if Config.fullscreen:
            options.add_argument("--kiosk")
        # options.add_argument("--no-sandbox")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("prefs", {
            "download.default_directory": r"utils/files",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,

        })

        d = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                             desired_capabilities=options.to_capabilities())

    elif Config.browser == 'firefox':
        d = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.addfinalizer(lambda *args: d.quit())
    return d


@pytest.fixture()
def driver(request, up_browser):
    """
    Set up a single session for these tests.
    """
    d = up_browser

    if Config.headless or (not Config.fullscreen):
        resolutions = {"720p": (1280, 720), "1080p": (1920, 1080), "1440p": (2560, 1440)}

        res = resolutions[Config.browser_resolution]
        d.set_window_size(*res)

    request.instance.driver = d

    return d


@pytest.fixture(scope='class', autouse=True)
def create_and_clean_issues():
    """
    At setup creates 10 issues.
    At teardown deletes all issues in a testing project created by testing user
    """

    # set authentication cookie
    payload = json.dumps({'username': 'Kirill_Vasiluk', 'password': 'Kirill_Vasiluk'}, ensure_ascii=False)
    login_resp = http.post('rest/auth/1/session', payload)
    http.update_auth_header(login_resp)

    for i in range(10):
        issue_data = create_issue_json(random_string(10), random_string(20), 'Bug')
        http.post(Config.issue_url, json.dumps(issue_data))

    yield

    search_jql = "?jql=project={}%20AND%20creator={}".format(Config.project_key, Config.username)
    search_resp = http.get(Config.search_url + search_jql)
    for issue in search_resp.json()["issues"]:
        http.delete("rest/api/2/issue/%s" % issue["key"])