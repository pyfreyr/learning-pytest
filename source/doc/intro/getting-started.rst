快速入门
==============


安装 Pytest
---------------

使用 pip 进行安装：

::

   $ pip install pytest


第一个测试函数
----------------


Pytest 使用 Python 的 ``assert`` 进行条件判断，最简单的测试函数如：


.. code-block:: python

   # test1.py

   def test_passing():
       assert (1, 2, 3) == (1, 2, 3)


运行测试函数
----------------

使用命令 ``pytest`` 运行测试函数：

::

   $ pytest tests/test1.py
   ============================= test session starts =============================
   platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
   rootdir: F:\self-repo\learning-pytest, inifile:
   collected 1 item

   tests\test1.py .                                                         [100%]

   ========================== 1 passed in 0.09 seconds ===========================

.. note::

   pytest 使用 ``.`` 标识测试成功（``PASSED``）。

.. tip::

   可以使用 ``-v`` 选项，显示测试的详细信息。

   使用 ``pytest -h`` 查看 pytest 的所有选项。

::

   ============================= test session starts =============================
   platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0 -- c:\anaconda3\python.exe
   cachedir: .pytest_cache
   rootdir: F:\self-repo\learning-pytest, inifile:
   collected 1 item

   tests/test1.py::test_passing PASSED                                      [100%]

   ========================== 1 passed in 0.03 seconds ===========================

测试失败
-------------

下面是一个失败的测试函数：

.. code-block:: python

   # test2.py

   def test_failing():
       assert (1, 2, 3) == (3, 2, 1)

运行结果为：

::

   $ pytest tests/test2.py
   ============================= test session starts =============================
   platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
   rootdir: F:\self-repo\learning-pytest, inifile:
   collected 1 item

   tests\test2.py F                                                         [100%]

   ================================== FAILURES ===================================
   ________________________________ test_failing _________________________________

       def test_failing():
   >       assert (1, 2, 3) == (3, 2, 1)
   E       assert (1, 2, 3) == (3, 2, 1)
   E         At index 0 diff: 1 != 3
   E         Use -v to get the full diff

   tests\test2.py:2: AssertionError
   ========================== 1 failed in 0.19 seconds ===========================

.. note::

   pytest 使用 ``F`` 标识测试失败（``FAILED``）。

pytest 对失败的测试给出了非常人性化的提示。

