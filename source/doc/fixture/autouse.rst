自动执行
=================


目前为止，所有固件的使用都是手动指定，或者作为参数，或者使用 ``usefixtures``。

如果我们想让固件自动执行，可以在定义时指定 ``autouse`` 参数。

下面是两个自动计时固件，一个用于统计每个函数运行时间（``function`` 作用域），一个用于计算测试总耗时（``session`` 作用域）：

.. code-block:: python

    # test_autouse.py

    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


    @pytest.fixture(scope='session', autouse=True)
    def timer_session_scope():
        start = time.time()
        print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))

        yield

        finished = time.time()
        print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
        print('Total time cost: {:.3f}s'.format(finished - start))


    @pytest.fixture(autouse=True)
    def timer_function_scope():
        start = time.time()
        yield
        print(' Time cost: {:.3f}s'.format(time.time() - start))

注意下面的两个测试函数并都没有显式使用固件：

.. code-block:: python

    def test_1():
        time.sleep(1)


    def test_2():
        time.sleep(2)

执行测试可看到，固件自动执行并完成计时任务：

::

    $ pytest -s tests/fixture/test_autouse.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items

    tests\fixture\test_autouse.py
    start: 2018-06-12 10:16:27
    . Time cost: 1.003s.
    . Time cost: 2.003s.
    finished: 2018-06-12 10:16:30
    Total time cost: 3.016s.


    ========================== 2 passed in 3.11 seconds ===========================
