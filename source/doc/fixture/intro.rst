什么是固件
=============

固件（Fixture）是一些函数，pytest 会在执行测试函数之前（或之后）加载运行它们。

我们可以利用固件做任何事情，其中最常见的可能就是数据库的初始连接和最后关闭操作。

Pytest 使用 ``pytest.fixture()`` 定义固件，下面是最简单的固件，只返回北京邮编：

.. code-block:: python

    # test_postcode.py

    @pytest.fixture()
    def postcode():
        return '010'


    def test_postcode(postcode):
        assert postcode == '010'

固件可以直接定义在各测试脚本中，就像上面的例子。更多时候，我们希望一个固件可以在更大程度上复用，这就需要对固件进行集中管理。Pytest 使用文件 ``conftest.py`` 集中管理固件。


.. note::

   在复杂的项目中，可以在不同的目录层级定义 ``conftest.py``，其作用域为其所在的目录和子目录。

.. important::

   不要自己显式调用 ``conftest.py``，pytest 会自动调用，可以把 conftest 当做插件来理解。


