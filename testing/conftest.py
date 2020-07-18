# -*- coding:utf-8  -*-
#@Time      :2020/7/18 12:12
#@Author    : Sun
#@File      :conftest.py

import pytest
from pythoncode.calc import Calculator

@pytest.fixture(scope='function', autouse=True)
def start():
    print("开始计算")
    cla = Calculator()
    yield
    print("计算结束")


