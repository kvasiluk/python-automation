import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.config import Config


@pytest.fixture(scope="session")
def up_browser(request):
    """ SetUp/TearDown selenium driver """

    d = None
    if Config.browser == 'chrome':
        options = webdriver.ChromeOptions()
        if Config.headless:
            options.add_argument("--headless")
        if Config.fullscreen:
            options.add_argument("--kiosk")
        options.add_argument("--no-sandbox")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("prefs", {
            "download.default_directory": r"utils/files",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,

        })

        d = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                             desired_capabilities=options.to_capabilities())

    elif Config.browser == 'firefox':
        d = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.addfinalizer(lambda *args: d.quit())
    return d


@pytest.fixture()
def driver(request, up_browser):
    """
    Set up a single session for these tests.
    """
    d = up_browser

    if Config.headless or (not Config.fullscreen):
        resolutions = {"720p": (1280, 720), "1080p": (1920, 1080), "1440p": (2560, 1440)}

        res = resolutions[Config.browser_resolution]
        d.set_window_size(*res)

    request.instance.driver = d

    return d