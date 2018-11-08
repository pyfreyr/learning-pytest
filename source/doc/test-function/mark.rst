标记函数
===============


Pytest 查找测试策略
-----------------------

默认情况下，pytest 会递归查找当前目录下所有以 ``test`` 开始或结尾的 Python 脚本，并执行文件内的所有以 ``test`` 开始或结束的函数和方法。

对于下面脚本：

.. code-block:: python

   # test_no_mark.py

   def test_func1():
       assert 1 == 1

   def test_func2():
       assert 1 != 1

直接执行测试脚本会同时执行所有测试函数：

::

    $ pytest tests/test-function/test_no_mark.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items

    tests\test-function\test_no_mark.py .F                                   [100%]

    ================================== FAILURES ===================================
    _________________________________ test_func2 __________________________________

        def test_func2():
    >       assert 1 != 1
    E       assert 1 != 1

    tests\test-function\test_no_mark.py:6: AssertionError
    ===================== 1 failed, 1 passed in 0.07 seconds ======================

标记测试函数
--------------


由于某种原因（如 ``test_func2`` 的功能尚未开发完成），我们只想执行指定的测试函数。在 pytest 中有几种方式可以解决：

第一种，显式指定函数名，通过 ``::`` 标记。

::

    $ pytest tests/test-function/test_no_mark.py::test_func1
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\test-function\test_no_mark.py .                                    [100%]

    ========================== 1 passed in 0.02 seconds ===========================

第二种，使用模糊匹配，使用 ``-k`` 选项标识。

::

    $ pytest -k func1 tests/test-function/test_no_mark.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items / 1 deselected

    tests\test-function\test_no_mark.py .                                    [100%]

    =================== 1 passed, 1 deselected in 0.03 seconds ====================

.. note::

   以上两种方法，第一种一次只能指定一个测试函数，当要进行批量测试时无能为力；第二种方法可以批量操作，但需要所有测试的函数名包含相同的模式，也不方便。

第三种，使用 ``pytest.mark`` 在函数上进行标记。

带标记的测试函数如：

.. code-block:: python

   # test_with_mark.py

   @pytest.mark.finished
   def test_func1():
       assert 1 == 1

   @pytest.mark.unfinished
   def test_func2():
       assert 1 != 1

测试时使用 ``-m`` 选择标记的测试函数：

::

    $ pytest -m finished tests/test-function/test_with_mark.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 2 items / 1 deselected

    tests\test-function\test_with_mark.py .                                  [100%]

    =================== 1 passed, 1 deselected in 0.10 seconds ====================

使用 mark，我们可以给每个函数打上不同的标记，测试时指定就可以允许所有被标记的函数。

.. note::

   一个函数可以打多个标记；多个函数也可以打相同的标记。

   运行测试时使用 ``-m`` 选项可以加上逻辑，如：

   ::

      $ pytest -m "finished and commit"

      $ pytest -m "finished and not merged"
