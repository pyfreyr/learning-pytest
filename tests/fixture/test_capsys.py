import sys


def ping(output):
    print('Pong...', file=output)


def test_stdout(capsys):
    ping(sys.stdout)
    out, err = capsys.readouterr()
    assert out == 'Pong...\n'
    assert err == ''


def test_stderr(capsys):
    ping(sys.stderr)
    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'Pong...\n'
