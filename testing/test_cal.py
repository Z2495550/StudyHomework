# -*- coding:utf-8  -*-
#@Time      :2020/7/18 12:11
#@Author    : Sun
#@File      :test_calc.py

import pytest
from pythoncode.calc import Calculator
import yaml
import os


file = '../data/test.yaml'
with open(file,'r',encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adds = datas['add'].keys()
    add_datas = datas['add'].values()
    cuts = datas['cut'].keys()
    cut_datas = datas['cut'].values()
    mults = datas['mult'].keys()
    mult_datas = datas['mult'].values()
    divs = datas['div'].keys()
    div_datas = datas['div'].values()


class TestCalc():

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        pass


    # @pytest.mark.parametrize("a, b, result",[
    #     (1,1,2),
    #     (-1,-1,-2),
    #     (-1,1,0)
    # ],)
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(('a,b,result'),add_datas,ids=adds)
    @pytest.mark.add
    def test_add(self, a, b, result ):
        assert result == self.cal.add(a, b)

    # 插件pytest-dependency	控制用例依赖关系
    '''
    如果test_add用例成功，test_cut会被执行
    如果test_add用例失败，test_cut会被跳过不被执行
    depends = [] 列表中加入依赖得到用例名称
    '''
    # 插件pytest-ordering控制用例执行顺序
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['test_add'],name='test_cut')
    @pytest.mark.parametrize('a,b,result',cut_datas,ids=cuts)
    @pytest.mark.cut
    def test_cut(self, a, b, result):
        assert result == self.cal.cut(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,result',mult_datas,ids=mults)
    @pytest.mark.mult
    def test_mult(self, a, b, result):
        assert result == self.cal.mult(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['test_mult'],name='test_div')
    @pytest.mark.parametrize('a,b,result',div_datas,ids=divs)
    @pytest.mark.div
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)