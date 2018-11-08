参数化
===============

在“第二部分 测试函数”中，介绍了函数的参数化测试：

.. code-block:: python

   # test-function/test_parametrize.py

   @pytest.mark.parametrize('passwd',
                         ['123456',
                          'abcdefdfs',
                          'as52345fasdf4'])
   def test_passwd_length(passwd):
       assert len(passwd) >= 8

因为固件也是函数，我们同样可以对固件进行参数化。在什么情况下需要对固件参数化？

假设现在有一批 API 需要测试对不同数据库的支持情况（对所有数据库进行相同操作），最简单的方法就是针对每个数据库编写一个测试用例，但这包含大量重复代码，如数据库的连接、关闭，查询等。

进一步，可以使用固件抽离出数据库的通用操作，每个 API 都能复用这些数据库固件，同时可维护性也得到提升。

更进一步，可以继续将这些固件合并为一个，而通过参数控制连接到不同的数据库。这就需要使用固件参数化来实现。固件参数化需要使用 pytest 内置的固件 ``request``，并通过 ``request.param`` 获取参数。

.. code-block:: python

    @pytest.fixture(params=[
        ('redis', '6379'),
        ('elasticsearch', '9200')
    ])
    def param(request):
        return request.param


    @pytest.fixture(autouse=True)
    def db(param):
        print('\nSucceed to connect %s:%s' % param)

        yield

        print('\nSucceed to close %s:%s' % param)


    def test_api():
        assert 1 == 1

执行结果：

::

    $ pytest -s tests/fixture/test_parametrize.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items

    tests\fixture\test_parametrize.py
    Succeed to connect redis:6379
    .
    Succeed to close redis:6379

    Succeed to connect elasticsearch:9200
    .
    Succeed to close elasticsearch:9200

    ========================== 2 passed in 0.10 seconds ===========================


.. note::

   与函数参数化使用 ``@pytest.mark.parametrize`` 不同，固件在定义时使用 ``params`` 参数进行参数化。

   固件参数化依赖于内置固件 ``request`` 及其属性 ``param``。


