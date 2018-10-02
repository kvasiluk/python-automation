import pytest


@pytest.mark.nobrowser
@pytest.mark.prepare
def test_create(create_issues):
    assert True


@pytest.mark.nobrowser
@pytest.mark.clean
def test_clean(clean_issues):
    assert True
