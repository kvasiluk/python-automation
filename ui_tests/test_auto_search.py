import allure
import pytest

from .base_test import BaseTest
from utils.config import Config

step = allure.step


@allure.feature("Search")
class TestSearch(BaseTest):
    @pytest.mark.ui
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("search_string,results", [
        (Config.search_string_1, 5),
        (Config.search_string_2, 1),
        ("ZZZZZZZZZZZZZZnoresultZZZZZZZZZ", 0),
    ])
    def test_search(self, search_string, results):
        with step("Search an issue"):
            self.pages.topbar_menu.search(search_string)
            self.pages.search_results_page.wait_for_results()

            assert self.pages.search_results_page.validate_results(results), \
                "Found {} issues, expected was {}".format(self.pages.search_results_page.result_count, results)
