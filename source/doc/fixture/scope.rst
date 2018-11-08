作用域
=============

固件的作用是为了抽离出重复的工作和方便复用，为了更精细化控制固件（比如只想对数据库访问测试脚本使用自动连接关闭的固件），pytest 使用作用域来进行指定固件的使用范围。

在定义固件时，通过 ``scope`` 参数声明作用域，可选项有：

- ``function``: 函数级，每个测试函数都会执行一次固件；
- ``class``: 类级别，每个测试类执行一次，所有方法都可以使用；
- ``module``: 模块级，每个模块执行一次，模块内函数和方法都可使用；
- ``session``: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。


.. note::

   默认的作用域为 ``function``。

.. code-block:: python

    @pytest.fixture(scope='function')
    def func_scope():
        pass


    @pytest.fixture(scope='module')
    def mod_scope():
        pass


    @pytest.fixture(scope='session')
    def sess_scope():
        pass


    @pytest.fixture(scope='class')
    def class_scope():
        pass

最简单使用固件方式是作为测试函数参数：

.. code-block:: python

    # test_scope.py

    def test_multi_scope(sess_scope, mod_scope, func_scope):
        pass

执行结果如下，可以清楚看到各固件的作用域和执行顺序：

::

    $ pytest --setup-show tests/fixture/test_scope.py::test_multi_scope
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\fixture\test_scope.py
    SETUP    S sess_scope
      SETUP    M mod_scope
          SETUP    F func_scope
            tests/fixture/test_scope.py::test_multi_scope (fixtures used: func_scope, mod_scope, sess_scope).
          TEARDOWN F func_scope
      TEARDOWN M mod_scope
    TEARDOWN S sess_scope

    ========================== 1 passed in 0.10 seconds ===========================




对于类使用作用域，需要使用 ``pytest.mark.usefixtures`` （对函数和方法也适用）：

.. code-block:: python

    # test_scope.py

    @pytest.mark.usefixtures('class_scope')
    class TestClassScope:
        def test_1(self):
            pass

        def test_2(self):
            pass

执行结果如下，可见所有测试函数都在固件作用范围内：

::

    $ pytest --setup-show tests/fixture/test_scope.py::TestClassScope
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items

    tests\fixture\test_scope.py
        SETUP    C class_scope
            tests/fixture/test_scope.py::TestClassScope::()::test_1 (fixtures used: class_scope).
            tests/fixture/test_scope.py::TestClassScope::()::test_2 (fixtures used: class_scope).
        TEARDOWN C class_scope

    ========================== 2 passed in 0.03 seconds ===========================











