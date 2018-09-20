from selenium import webdriver
from utils.config import Config


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = Config.jira_url

    def page_title(self):
        return self.driver.title

    def open(self, url):
        return self.driver.get(url)

    def go_to(self):
        self.driver.get(self.url)

    def go_to_main_page(self):
        self.driver.get(Config.jira_url)
