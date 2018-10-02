import pytest

from .base_test import BaseTest
from utils.config import Config


class TestSearch(BaseTest):
    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("search_string,results", [
        (Config.search_string_1, 5),
        (Config.search_string_2, 1),
        ("ZZZZZZZZZZZZZZnoresultZZZZZZZZZ", 0),
    ])
    def test_search(self, search_string, results):
        self.pages.topbar_menu.search(search_string)
        self.pages.search_results_page.wait_for_results()

        if results:
            res_count = self.pages.search_results_page.result_count()
            assert results == res_count, "Found {} issues, expected was {}".format(res_count, results)
        else:
            assert self.pages.search_results_page.is_no_issues_found(), "Issues found when expecting no results"
