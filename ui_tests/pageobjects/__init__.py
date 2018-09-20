from ui_tests.pageobjects.dashboard_page import DashboardPage
from ui_tests.pageobjects.login_page import LoginPage


class Pages(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def dashboard_page(self):
        return DashboardPage(self.driver)