内置固件
=============

tmpdir & tmpdir_factory
-------------------------

用于临时文件和目录管理，默认会在测试结束时删除。

.. note::

   ``tmpdir`` 只有 ``function`` 作用域，只能在函数内使用。

使用 ``tmpdir.mkdir()`` 创建目临时录，``tmpdir.join()`` 创建临时文件（或者使用创建的目录）。

.. code-block:: python

    def test_tmpdir(tmpdir):
        a_dir = tmpdir.mkdir('mytmpdir')
        a_file = a_dir.join('tmpfile.txt')

        a_file.write('hello, pytest!')

        assert a_file.read() == 'hello, pytest!'

.. note::

   ``tmpdir_factory`` 可以在所有作用域使用，包括 ``function, class, module, session``。

.. code-block:: python

    @pytest.fixture(scope='module')
    def my_tmpdir_factory(tmpdir_factory):
        a_dir = tmpdir_factory.mktemp('mytmpdir')
        a_file = a_dir.join('tmpfile.txt')

        a_file.write('hello, pytest!')

        return a_file


pytestconfig
-----------------

使用 ``pytestconfig``，可以很方便的读取命令行参数和配置文件。

下面示例演示命令行参数解析：首先在 ``conftest.py`` 中使用函数 ``pytest_addoption`` （特定的 `hook function`_ ）：

.. _hook function: https://docs.pytest.org/en/latest/writing_plugins.html#writing-hook-functions

.. code-block:: python

    # conftest.py

    def pytest_addoption(parser):
        parser.addoption('--host', action='store',
                         help='host of db')
        parser.addoption('--port', action='store', default='8888',
                         help='port of db')

然后就可以在测试函数中通过 ``pytestconfig`` 获取命令行参数：

.. code-block:: python

    # test_config.py

    def test_option1(pytestconfig):
        print('host: %s' % pytestconfig.getoption('host'))
        print('port: %s' % pytestconfig.getoption('port'))

.. note::

   ``pytestconfig`` 其实是 ``request.config`` 的快捷方式，所以也可以自定义固件实现命令行参数读取。


.. code-block:: python

    # conftest.py

    def pytest_addoption(parser):
        parser.addoption('--host', action='store',
                         help='host of db')
        parser.addoption('--port', action='store', default='8888',
                         help='port of db')


    @pytest.fixture
    def config(request):
        return request.config


    # test_config.py

    def test_option2(config):
        print('host: %s' % config.getoption('host'))
        print('port: %s' % config.getoption('port'))


执行结果：

::

    $ pytest -s --host=localhost tests/fixture/test_config.py::test_option2
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\fixture\test_config.py host: localhost
    port: 8888
    .

    ========================== 1 passed in 0.06 seconds ===========================

capsys
-----------

``capsys`` 用于捕获 ``stdout`` 和 ``stderr`` 的内容，并临时关闭系统输出。

.. code-block:: python

    # test_capsys.py

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

monkeypatch
--------------

``monkeypath`` 用于运行时动态修改类或模块。

.. tip::

   In Python, the term monkey patch only refers to dynamic modifications of a class or module at runtime, motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as you desire.

一个简单的 monkeypatch 如：

.. code-block:: python

    from SomeOtherProduct.SomeModule import SomeClass

    def speak(self):
        return "ook ook eee eee eee!"

    SomeClass.speak = speak

Pytest 内置 ``monkeypatch`` 提供的函数有：

- ``setattr(target, name, value, raising=True)``，设置属性；
- ``delattr(target, name, raising=True)``，删除属性；
- ``setitem(dic, name, value)``，字典添加元素；
- ``delitem(dic, name, raising=True)``，字典删除元素；
- ``setenv(name, value, prepend=None)``，设置环境变量；
- ``delenv(name, raising=True)``，删除环境变量；
- ``syspath_prepend(path)``，添加系统路径；
- ``chdir(path)``，切换目录。

其中 ``raising`` 用于通知 pytest 在元素不存在时是否抛出异常；``prepend`` 如果设置，环境变量将变为 ``value+prepend+<old value>`` 。

下面使用保存配置文件示例说明 monkeypatch 的作用和使用。

假设我们需要切换某个服务到国内科大源以加速，有以下脚本用于修改配置文件 ``.conf.json``：

.. code-block:: python

    # test_monkeypatch.py

    def dump_config(config):
        path = os.path.expanduser('~/.conf.json')
        with open(path, 'w', encoding='utf-8') as wr:
            json.dump(config, wr, indent=4)


    def test_config():
        dump_config(config)
        path = os.path.expanduser('~/.conf.json')
        expected = json.load(open(path, 'r', encoding='utf-8'))
        assert expected == config

似乎测试正常执行完全没有问题，但如果我们的家目录下恰好有这个配置文件并且维护了许多配置，运行测试将会覆盖原有配置，这太可怕了！

所以我们需要修改测试，最好能在临时目录里完成。但程序已经写死了文件路径，怎么办？

这种在运行时控制程序的功能就需要 monkeypatch 来实现，下面在测试过程中修改了环境变量：

.. code-block:: python

    # test_monkeypatch.py

    def test_config_monkeypatch(tmpdir, monkeypatch):
        monkeypatch.setenv('HOME', tmpdir.mkdir('home'))

        dump_config(config)
        path = os.path.expanduser('~/.conf.json')
        expected = json.load(open(path, 'r', encoding='utf-8'))
        assert expected == config

现在测试会来临时目录中执行，但环境变量可能对系统有依赖，所以更好的解决方法能自己控制路径中 ``~`` 的替换，这次通过改变 ``os.path.expanduser`` 的行为来实现：

.. code-block:: python

    # test_monkeypatch.py

    def test_config_monkeypatch2(tmpdir, monkeypatch):
        fake_home = tmpdir.mkdir('home')
        monkeypatch.setattr(os.path, 'expanduser',
                            lambda x: x.replace('~', str(fake_home)))
        dump_config(config)
        path = os.path.expanduser('~/.conf.json')
        expected = json.load(open(path, 'r', encoding='utf-8'))
        assert expected == config


recwarn
------------

``recwarn`` 用于捕获程序中 ``warnings`` 产生的警告。

.. code-block:: python

    # test_recwarn.py

    def warn():
        warnings.warn('Deprecated function', DeprecationWarning)


    def test_warn(recwarn):
        warn()
        assert len(recwarn) == 1
        w = recwarn.pop()
        assert w.category == DeprecationWarning

此外，pytest 可以使用 ``pytest.warns()`` 捕获警告：

.. code-block:: python

    def test_warn2():
        with pytest.warns(None) as warnings:
            warn()

        assert len(warnings) == 1
        w = warnings.pop()
        assert w.category == DeprecationWarning