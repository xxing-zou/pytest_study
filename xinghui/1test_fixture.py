import time

import pytest

@pytest.mark.usefixtures('beifan')
def test_beifan():
    print("我是测试用例，我正在执行")

@pytest.fixture(scope='session')
def data():
    return {}  #可变对象

@pytest.mark.order(1)#自定义用例顺序
def test_api(beifan,data):
    print(beifan)
    data['msg']='我是第一个用例'

class Test_1():
    @pytest.fixture(scope='function')  # 装饰器，将函数变成特殊函数
    def beifan(self):
        time.sleep(1)
        yield '我是xinghui'


    def test_123(self,beifan,data):
        print("hhhh哈哈哈")
        print(beifan)
        print('上一个用例传递来的内容是：',data['msg'])
        data['msg']='我是第二个用例'

    def test_web(self,beifan):
        pass

