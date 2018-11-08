import pytest

def connect(host, port):
    if not isinstance(port, int):
        raise TypeError('port type must be int')

def test_raises():
   with pytest.raises(TypeError) as e:
       connect('localhost', '6379')
   exec_msg = e.value.args[0]
   assert exec_msg == 'port type must be int'