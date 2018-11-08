跳过测试
==============


上一节提到 pytest 使用标记过滤测试函数，所以对于那些尚未开发完成的测试，最好的处理方式就是略过而不执行测试。

按正向的思路，我们只要通过标记指定要测试的就可以解决这个问题；但有时候的处境是我们能进行反向的操作才是最好的解决途径，即通过标记指定要跳过的测试。

Pytest 使用特定的标记 ``pytest.mark.skip`` 完美的解决了这个问题。

.. code-block:: python

   # test_skip.py

   @pytest.mark.skip(reason='out-of-date api')
   def test_connect():
       pass


执行结果可以看到该测试已被忽略：

::

    $ pytest tests/test-function/test_skip.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\test-function\test_skip.py s                                       [100%]

    ========================== 1 skipped in 0.13 seconds ==========================

.. note::

   pytest 使用 ``s`` 表示测试被跳过（``SKIPPED``）。


Pytest 还支持使用 ``pytest.mark.skipif`` 为测试函数指定被忽略的条件。

.. code-block:: python

   @pytest.mark.skipif(conn.__version__ < '0.2.0',
                       reason='not supported until v0.2.0')
   def test_api():
       pass

