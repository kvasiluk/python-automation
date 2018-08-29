import pytest

from .base_test import BaseTest

search_url = 'rest/api/2/search'


class TestSearch(BaseTest):
    @pytest.mark.parametrize("search_jql,results", [
        ('?jql=project=AQAPYTHON%20AND%20creator=kirill_vasiluk&maxResults=5', 5),
        ('?jql=project=AQAPYTHON%20AND%20creator=kirill_vasiluk&maxResults=1', 1),
        ('?jql=project=HR%20AND%20creator=kirill_vasiluk&maxResults=5', 0),
    ])
    def test_search(self, search_jql, results):
        search_resp = self.http.get(search_url + search_jql)
        assert search_resp.status_code == 200, 'Search failed'
        assert len(search_resp.json()['issues']) == results, 'Search results do not match'
