# -*- coding:utf-8  -*-
#@Time      :2020/7/19 11:43
#@Author    : Sun
#@File      :check_env.py

import pytest

#测试用例通过传入 fixture方法，获取测试数据、开发数据
def check_case(cmdoption):
    print('测试环境验证')
    env,data = cmdoption
    print(f'环境:{env},数据{data}')
    ip = data['env']['ip']
    port = data['env']['port']
    url = 'http://' + ip + ":" + str(port)
    print(url)

