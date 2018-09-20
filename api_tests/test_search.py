import pytest

from .base_test import BaseTest
from utils.config import Config
from .constants import *


class TestSearch(BaseTest):
    @pytest.mark.parametrize("search_jql,results", [
        (search_jql_five, 5),
        (search_jql_one, 1),
        (search_jql_zero, 0),
    ])
    def test_search(self, search_jql, results):
        search_resp = self.http.get(Config.search_url + search_jql)
        assert search_resp.status_code == 200, 'Search failed'
        assert len(search_resp.json()['issues']) == results, 'Search results do not match'
