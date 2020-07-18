# -*- coding:utf-8  -*-
#@Time      :2020/7/18 12:11
#@Author    : Sun
#@File      :test_calc.py

import pytest
from pythoncode.calc import Calculator
import yaml
import os


file = './data/test.yaml'
with open(file,'r',encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adds = datas['add'].keys()
    add_datas = list(datas['add'].values())
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
    @pytest.mark.parametrize(('a,b,result'),add_datas,ids=adds)
    def test_add(self, a, b, result ):
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result',cut_datas,ids=cuts)
    def test_cut(self, a, b, result):
        assert result == self.cal.cut(a, b)

    @pytest.mark.parametrize('a,b,result',mult_datas,ids=mults)
    def test_mult(self, a, b, result):
        assert result == self.cal.mult(a, b)

    @pytest.mark.parametrize('a,b,result',div_datas,ids=divs)
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)