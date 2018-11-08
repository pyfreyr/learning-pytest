重命名
=============

固件的名称默认为定义时的函数名，如果不想使用默认，可以通过 ``name`` 选项指定名称：

.. code-block:: python

    # test_rename.py

    @pytest.fixture(name='age')
    def calculate_average_age():
        return 28


    def test_age(age):
        assert age == 28

