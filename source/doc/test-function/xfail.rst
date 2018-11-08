预见的错误
================

如果我们事先知道测试函数会执行失败，但又不想直接跳过，而是希望显示的提示。

Pytest 使用 ``pytest.mark.xfail`` 实现预见错误功能：

.. code-block:: python

   # test_xfail.py

   @pytest.mark.xfail(gen.__version__ < '0.2.0',
                      reason='not supported until v0.2.0')
   def test_api():
       id_1 = gen.unique_id()
       id_2 = gen.unique_id()
       assert id_1 != id_2

执行结果：

::

    $ pytest tests/test-function/test_xfail.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\test-function\test_xfail.py x                                      [100%]

    ========================== 1 xfailed in 0.12 seconds ==========================

.. note::

   pytest 使用 ``x`` 表示预见的失败（``XFAIL``）。

   如果预见的是失败，但实际运行测试却成功通过，pytest 使用 ``X`` 进行标记（``XPASS``）。

