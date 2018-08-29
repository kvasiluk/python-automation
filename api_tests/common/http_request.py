import requests
from requests.compat import basestring

DEFAULT_HEADER = {'Content-Type': 'application/json'}
DEFAULT_TIMEOUT = 15


class BaseHttp(object):
    """
    Main Http interactions module
    """

    def __init__(self, headers=None, cookies=None):
        self.session = requests.session()
        self.session.headers.update(DEFAULT_HEADER)
        self.base_url = 'http://jira.hillel.it:8080'
        if headers:
            self.session.headers.update(headers)
        if cookies:
            self.session.cookies.update(cookies)

    def get(self, url_part, headers=None, cookies=None, timeout=DEFAULT_TIMEOUT, **kwargs):
        """
        :param url_part: request uri part. Not needed to put full url
        :param list cookies: custom request cookies
        :param timeout: custom timeout
        :param dict headers: custom request headers
        :rtype: requests.Response
        """

        url = self._make_url(url_part)

        response = self.session.get(url, cookies=cookies, headers=headers, timeout=timeout, **kwargs)

        return response

    def post(self, url_part, content=None, headers=None, cookies=None, timeout=DEFAULT_TIMEOUT, **kwargs):
        """
        :param url_part: request uri part. Not needed to put full url
        :param content: data to send
        :param list cookies: custom request cookies
        :param timeout: custom timeout
        :param dict headers: custom request headers
        :rtype: requests.Response
        """

        url = self._make_url(url_part)

        response = self.session.post(url, data=content, cookies=cookies, headers=headers, timeout=timeout, **kwargs)

        return response

    def put(self, url_part, content=None, headers=None, cookies=None, timeout=DEFAULT_TIMEOUT, **kwargs):
        """
        :param url_part: request uri part. Not needed to put full url
        :param content: data to send
        :param list cookies: custom request cookies
        :param timeout: custom timeout
        :param dict headers: custom request headers
        :rtype: requests.Response
        """

        url = self._make_url(url_part)

        response = self.session.put(url, data=content, cookies=cookies, headers=headers, timeout=timeout,**kwargs)

        return response

    def delete(self, url_part, headers=None, cookies=None, timeout=DEFAULT_TIMEOUT, **kwargs):
        """
        :param url_part: request uri part. Not needed to put full url
        :param list cookies: custom request cookies
        :param timeout: custom timeout
        :param dict headers: custom request headers
        :rtype: requests.Response
        """

        url = self._make_url(url_part)

        response = self.session.delete(url, cookies=cookies, headers=headers, timeout=timeout, **kwargs)

        return response

    def update_auth_header(self, response):
        if response and isinstance(response, basestring):
            self.session.headers.update({'Cookie': 'JSESSIONID=%s' % response})
        elif response.json()['session']['name'] == 'JSESSIONID':
            self.session.headers.update({'Cookie': 'JSESSIONID=%s' % response.json()['session']['value']})

    def _make_url(self, url_part):
        return '%s/%s' % (self.base_url, url_part)
