# -*- coding:utf-8  -*-
#@Time      :2020/7/19 11:52
#@Author    : Sun
#@File      :conftest.py
import pytest
import yaml

#注册自定义参数 env 到配置对象
def pytest_addoption(parser):
    mygroup = parser.getgroup('mytest')
    mygroup.addoption("--env",#注册一个命令行选项
                      default='test',#这个是默认值
                      dest = 'env',
                      help='将命令行参数"--env"添加到pytest配置中')


"""
# 处理命令行传来得到参数，设置乘fixture，将test环境和dev环境获取中其他环境
# 分别处理，获取想要的不同环境下得测试数据
"""
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption('--env',default='test')
    if myenv == 'test':
        datapath = '../data/test/data.yaml'

    if myenv == 'dev':
        datapath = '../data/test/data.yaml'

    with open(datapath,'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return myenv,data