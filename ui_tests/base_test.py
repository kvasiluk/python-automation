import pytest

from ui_tests.pageobjects import Pages
from utils.config import Config


@pytest.mark.usefixtures("driver")
class BaseTest(object):

    @pytest.fixture(autouse=True)
    def nav_to_main(self, driver):
        """ Navigate to main app page specified in config"""
        driver.get(Config.jira_url)

    @pytest.fixture
    def login(self):
        self.pages.login_page.go_to()
        self.pages.login_page.login()

    @property
    def pages(self):
        return Pages(self.driver)
