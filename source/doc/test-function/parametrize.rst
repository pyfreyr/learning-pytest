参数化
=============

当对一个测试函数进行测试时，通常会给函数传递多组参数。比如测试账号登陆，我们需要模拟各种千奇百怪的账号密码。

当然，我们可以把这些参数写在测试函数内部进行遍历。不过虽然参数众多，但仍然是一个测试，当某组参数导致断言失败，测试也就终止了。

通过异常捕获，我们可以保证程所有参数完整执行，但要分析测试结果就需要做不少额外的工作。

在 pytest 中，我们有更好的解决方法，就是参数化测试，即每组参数都独立执行一次测试。使用的工具就是 ``pytest.mark.parametrize(argnames, argvalues)``。

这里是一个密码长度的测试函数，其中参数名为 ``passwd``，其可选列表包含三个值：

.. code-block:: python

   # test_parametrize.py

   @pytest.mark.parametrize('passwd',
                         ['123456',
                          'abcdefdfs',
                          'as52345fasdf4'])
   def test_passwd_length(passwd):
       assert len(passwd) >= 8

运行可知执行了三次测试：

::

    $ pytest tests/test-function/test_parametrize.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 3 items

    tests\test-function\test_parametrize.py F..                              [100%]

    ================================== FAILURES ===================================

再看一个多参数的例子，用于校验用户密码：

.. code-block:: python

    # test_parametrize.py

    @pytest.mark.parametrize('user, passwd',
                             [('jack', 'abcdefgh'),
                              ('tom', 'a123456a')])
    def test_passwd_md5(user, passwd):
        db = {
            'jack': 'e8dc4081b13434b45189a720b77b6818',
            'tom': '1702a132e769a623c1adb78353fc9503'
        }

        import hashlib

        assert hashlib.md5(passwd.encode()).hexdigest() == db[user]

使用 ``-v`` 执行测试

::

    $ pytest -v tests/test-function/test_parametrize.py::test_passwd_md5
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0 -- c:\anaconda3\python.exe
    cachedir: .pytest_cache
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items

    tests/test-function/test_parametrize.py::test_passwd_md5[jack-abcdefgh] PASSED [ 50%]
    tests/test-function/test_parametrize.py::test_passwd_md5[tom-a123456a] PASSED [100%]

    ========================== 2 passed in 0.04 seconds ===========================

如果觉得每组测试的默认参数显示不清晰，我们可以使用 ``pytest.param`` 的 ``id`` 参数进行自定义。

.. code-block:: python

    # test_parametrize.py

    @pytest.mark.parametrize('user, passwd',
                             [pytest.param('jack', 'abcdefgh', id='User<Jack>'),
                              pytest.param('tom', 'a123456a', id='User<Tom>')])
    def test_passwd_md5_id(user, passwd):
        db = {
            'jack': 'e8dc4081b13434b45189a720b77b6818',
            'tom': '1702a132e769a623c1adb78353fc9503'
        }

        import hashlib

        assert hashlib.md5(passwd.encode()).hexdigest() == db[user]

现在的执行结果为：

::

    $ pytest -v tests/test-function/test_parametrize.py::test_passwd_md5_id
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0 -- c:\anaconda3\python.exe
    cachedir: .pytest_cache
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items

    tests/test-function/test_parametrize.py::test_passwd_md5_id[User<Jack>] PASSED [ 50%]
    tests/test-function/test_parametrize.py::test_passwd_md5_id[User<Tom>] PASSED [100%]

    ========================== 2 passed in 0.07 seconds ===========================


