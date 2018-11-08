import pytest


@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass


class Connector:
    __version__ = '0.1.9'


@pytest.mark.skipif(Connector().__version__ < '0.2.0',
                    reason='not supported until v0.2.0')
def test_api():
    pass
