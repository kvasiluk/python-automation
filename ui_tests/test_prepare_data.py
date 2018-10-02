import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.nobrowser
@pytest.mark.prepare
def test_create(create_issues):
    ChromeDriverManager().install()
    assert True


@pytest.mark.nobrowser
@pytest.mark.clean
def test_clean(clean_issues):
    assert True
