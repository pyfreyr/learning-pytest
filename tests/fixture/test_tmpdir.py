import pytest


def test_tmpdir(tmpdir):
    a_dir = tmpdir.mkdir('mytmpdir')
    a_file = a_dir.join('tmpfile.txt')

    a_file.write('hello, pytest!')

    assert a_file.read() == 'hello, pytest!'


@pytest.fixture(scope='module')
def my_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mytmpdir')
    a_file = a_dir.join('tmpfile.txt')

    a_file.write('hello, pytest!')

    return a_file
