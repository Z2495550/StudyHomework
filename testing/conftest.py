# -*- coding:utf-8  -*-
#@Time      :2020/7/18 12:12
#@Author    : Sun
#@File      :conftest.py

import pytest
import yaml
from pythoncode.calc import Calculator

@pytest.fixture(scope='function', autouse=True)
def start():
    print("开始计算")
    cla = Calculator()
    yield
    print("计算结束")


def pytest_collection_modifyitems(session,config,items):
    print(items)
    print(len(items))
    #倒序执行 items里面的测试用例
    # items.reverse()
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")



