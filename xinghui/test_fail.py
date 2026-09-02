import time

import pytest
import yaml
from selenium import webdriver

# #../data.yaml去当前所在文件夹的上一级文件夹，找 data.yaml 文件
# f= open('../data.yaml','r',encoding='utf-8')
# data=yaml.safe_load(f)
# @pytest.mark.parametrize(
#     "n",#参数
#     data #数据
# )

#在分支上新增的注释，用于对比
#在分支上新增的注释，用于对比
#在分支上新增的注释，用于对比
def ddt(yaml_path,**kwargs):
    f=open(yaml_path,'r',encoding='utf-8')
    data_list=yaml.safe_load(f)
    return pytest.mark.parametrize('data',data_list,**kwargs)
#
# @ddt('../data.yaml')
# def test_fail(data):
#     assert 1==data
@pytest.fixture(scope="module")
def driver():
    d=webdriver.Edge()
    yield d
    d.quit()

@pytest.fixture()
def selenium(request,driver):
    request.node._driver=driver  #把浏览器给到当前用例
    yield driver

#下载了pytest-selenium，底层封装了一个fixture，所以直接调用该fixture即可
@ddt('ddt_login.yaml')
def test_web(selenium,data):
    # selenium.get('http://www.baidu.com')
    selenium.get('http://116.62.63.211/shop/?s=user/loginInfo.html')#浏览器操作

    el_username = selenium.find_element('xpath', '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input')
    el_password = selenium.find_element('xpath', '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input')
    el_submit = selenium.find_element('xpath',
                                        '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')
    el_username.send_keys(data['username'])#元素操作
    el_password.send_keys(data['password'])
    el_submit.click()

    time.sleep(1)
    sys_info=selenium.find_element('xpath','/html/body/div[10]/div/p').text

    assert sys_info==data['msg']#断言