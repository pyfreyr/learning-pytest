import pytest


@pytest.fixture()
def postcode():
    return '010'


def test_postcode(postcode):
    assert postcode == '010'
