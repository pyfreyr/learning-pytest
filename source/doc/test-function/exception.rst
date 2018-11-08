捕获异常
===============

在测试过程中，经常需要测试是否如期抛出预期的异常，以确定异常处理模块生效。在 pytest 中使用 ``pytest.raises()`` 进行异常捕获：

.. code-block:: python

   # test_raises.py

   def test_raises():
       with pytest.raises(TypeError) as e:
           connect('localhost', '6379')
       exec_msg = e.value.args[0]
       assert exec_msg == 'port type must be int'

运行结果如下：

::

    $ pytest test_raises.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\test-function\test_raise.py .                                      [100%]

    ========================== 1 passed in 0.07 seconds ===========================
