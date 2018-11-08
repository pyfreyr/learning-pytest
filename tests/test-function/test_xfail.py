import pytest


# xfail test
class IDGen1:
    __version__ = '0.1.9'

    def unique_id(self):
        return 1


gen1 = IDGen1()


@pytest.mark.xfail(gen1.__version__ < '0.2.0',
                   reason='not supported until v0.2.0')
def test_api1():
    id_1 = gen1.unique_id()
    id_2 = gen1.unique_id()
    assert id_1 != id_2


# xpass test
class IDGen2:
    __version__ = '0.1.9'

    def unique_id(self):
        import uuid
        return uuid.uuid4().hex


gen2 = IDGen2()


@pytest.mark.xfail(gen2.__version__ < '0.2.0',
                   reason='not supported until v0.2.0')
def test_api2():
    id_1 = gen2.unique_id()
    id_2 = gen2.unique_id()
    assert id_1 != id_2
