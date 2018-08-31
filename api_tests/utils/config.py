import configparser


class Config(object):

    config = configparser.ConfigParser()
    config.read('config.ini')

    timeout = config.getint('BASE', 'timeout')

    protocol = config.get('ENVIRONMENT', 'protocol')
    port = config.get('ENVIRONMENT', 'port')
    jira_url = "%s://%s:%s" % (protocol,
                               config.get('ENVIRONMENT', 'jira_srv'),
                               port)
    auth_url = config.get('ENVIRONMENT', 'auth_url')
    issue_url = config.get('ENVIRONMENT', 'issue_url')
    search_url = config.get('ENVIRONMENT', 'search_url')

    username = config.get('USER', 'username')
    password = config.get('USER', 'password')

    json_schemas_path = config.get('TEST', 'json_schemas_path')
