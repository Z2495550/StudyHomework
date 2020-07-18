# -*- coding:utf-8  -*-
#@Time      :2020/7/18 13:52
#@Author    : Sun
#@File      :RunAll.py

import pytest
import allure
import os


if __name__ == '__main__':
    args = ['-q', '-s',  '--alluredir', './Report/xml']
    pytest.main(args)
    os.system(f'allure generate ./Report/xml -o ./Report/html --clean')