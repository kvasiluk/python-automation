import pytest

from ui_tests.base_test import BaseTest


class TestLogin(BaseTest):
    @pytest.mark.parametrize("username,password", [
        ("Kirill_Vasiluk", "Kirill_Vasiluk")
    ])
    def test_login_positive(self, username, password):
        login_page = self.pages.login_page
        login_page.go_to()
        login_page.login(username=username, password=password)

        assert self.pages.dashboard_page.is_dashboard_page(), "User is not moved to dashboard page after login"
        assert self.pages.topbar_menu.is_authenticated(), "Failed to login"

    @pytest.mark.parametrize("username,password", [
        ("Wrong_Username", "Kirill_Vasiluk"),
        ("Kirill_Vasiluk", "Wrong_Password"),
        ("Wrong_Username", "Wrong_Password"),
    ])
    def test_login_negative(self, username, password):
        login_page = self.pages.login_page
        login_page.go_to()
        login_page.login(username=username, password=password)

        exp_error_message = "Sorry, your username and password are incorrect - please try again."
        assert login_page.is_login_page(), "User is not remains on login page after failed login"
        assert exp_error_message in login_page.get_error_message(), "Unexpected failed login error message"
