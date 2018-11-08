.. learning-pytest documentation master file, created by
   sphinx-quickstart on Mon Jun 11 10:03:52 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pytest 使用手册
===========================================

.. image:: images/pytest1.png

`pytest`_: helps you write better programs。

.. _pytest: https://docs.pytest.org/en/latest/index.html


快速入门
======================

.. toctree::
   :caption: 第一部分 快速入门
   :hidden:

   doc/intro/getting-started

:doc:`doc/intro/getting-started`
   使用 pytest 运行最简单的测试用例。

测试函数
===========

.. toctree::
   :caption: 第二部分 测试函数
   :hidden:

   doc/test-function/assert
   doc/test-function/exception
   doc/test-function/mark
   doc/test-function/skip
   doc/test-function/xfail
   doc/test-function/parametrize

:doc:`doc/test-function/assert`
   使用 assert 编写测试。

:doc:`doc/test-function/exception`
   使用 pytest 进行异常捕获测试。

:doc:`doc/test-function/mark`
   使用标记执行特定的测试用例。

:doc:`doc/test-function/skip`
   使用标记跳过测试。

:doc:`doc/test-function/xfail`
   明知失败还是要执行的解决方法。

:doc:`doc/test-function/parametrize`
   参数化测试。


固件
===========

.. toctree::
   :caption: 第三部分 固件
   :hidden:

   doc/fixture/intro
   doc/fixture/setup-and-teardown
   doc/fixture/scope
   doc/fixture/autouse
   doc/fixture/rename
   doc/fixture/parametrize
   doc/fixture/builtin-fixture


:doc:`doc/fixture/intro`
   固件就是函数，pytest 可以集中进行管理以便复用。

:doc:`doc/fixture/setup-and-teardown`
   使用固件实现预处理和后处理。

:doc:`doc/fixture/scope`
   声明作用域声明固件的作用范围。

:doc:`doc/fixture/autouse`
   让固件自动执行，完成诸如计时，日志任务。

:doc:`doc/fixture/rename`
   重命名固件。

:doc:`doc/fixture/parametrize`
   固件参数化，提升复用性和可维护性。

:doc:`doc/fixture/builtin-fixture`
   介绍 pytest 内置固件，避免重复造轮子。

插件
============

插件的介绍和使用，请移步 `Using plugins`_ 和 `Writing plugins`_ 。

.. _Using plugins: https://docs.pytest.org/en/latest/plugins.html
.. _Writing plugins: https://docs.pytest.org/en/latest/writing_plugins.html

配置
============

参考官方文档 `Configuration`_ 。

.. _Configuration: https://docs.pytest.org/en/latest/customize.html


贡献者
=========



联系
=========

本教程为 `Python Testing with pytest`_ 读书笔记，只作为交流学习。如有侵权，请联系本人删除。

.. _Python Testing with pytest: https://pragprog.com/book/bopytest/python-testing-with-pytest

.. _Github: https://github.com/ifreyr/learning-pytest/tree/master/tests

本教程所有测试示例代码可在 `Github`_ 下载。

如果您在阅读过程中发现有任何问题或建议，欢迎通知本人更新，帮助更多 Pythoner。

Email: mrchan3030@foxmail.com

