from ui_tests.pageobjects.create_issue_page import CreateIssuePage
from ui_tests.pageobjects.dashboard_page import DashboardPage
from ui_tests.pageobjects.issue_page import IssuePage
from ui_tests.pageobjects.login_page import LoginPage
from ui_tests.pageobjects.search_results_page import SearchResultsPage
from ui_tests.pageobjects.topbar_menu import TopbarMenu


class Pages(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def dashboard_page(self):
        return DashboardPage(self.driver)

    @property
    def topbar_menu(self):
        return TopbarMenu(self.driver)

    @property
    def create_issue_page(self):
        return CreateIssuePage(self.driver)

    @property
    def search_results_page(self):
        return SearchResultsPage(self.driver)

    @property
    def issue_page(self):
        return IssuePage(self.driver)
