import datetime
import time

import pytest

@pytest.fixture(scope='function')#装饰器，将函数变成特殊函数
def beifan():
    print("用例开始时间：",datetime.datetime.now())
    time.sleep(1)
    yield '我是幸会'
    print("用例结束时间：",datetime.datetime.now())