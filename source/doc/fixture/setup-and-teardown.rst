预处理和后处理
================

很多时候需要在测试前进行预处理（如新建数据库连接），并在测试完成进行清理（关闭数据库连接）。

当有大量重复的这类操作，最佳实践是使用固件来自动化所有预处理和后处理。

Pytest 使用 ``yield`` 关键词将固件分为两部分，``yield`` 之前的代码属于预处理，会在测试前执行；``yield`` 之后的代码属于后处理，将在测试完成后执行。


以下测试模拟数据库查询，使用固件来模拟数据库的连接关闭：

.. code-block:: python

    # test_db.py

    @pytest.fixture()
    def db():
        print('Connection successful')

        yield

        print('Connection closed')


    def search_user(user_id):
        d = {
            '001': 'xiaoming'
        }
        return d[user_id]


    def test_search(db):
        assert search_user('001') == 'xiaoming'

执行时使用 ``-s`` 阻止消息被吞：

::

    $ pytest -s tests/fixture/test_db.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\fixture\test_db.py Connection successful
    .Connection closed


    ========================== 1 passed in 0.02 seconds ===========================

可以看到在测试成功的 ``.`` 标识前后有数据库的连接和关闭操作。

.. tip::

   如果想更细的跟踪固件执行，可以使用 ``--setup-show`` 选项：

::

    $ pytest --setup-show tests/fixture/test_db.py
    ============================= test session starts =============================
    platform win32 -- Python 3.6.4, pytest-3.6.1, py-1.5.2, pluggy-0.6.0
    rootdir: F:\self-repo\learning-pytest, inifile:
    collected 1 item

    tests\fixture\test_db.py
          SETUP    F db
            tests/fixture/test_db.py::test_search (fixtures used: db).
          TEARDOWN F db

    ========================== 1 passed in 0.03 seconds ===========================









