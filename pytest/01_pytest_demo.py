import pytest
from config import Config
from pyappium import PyAppium

"""
    1. 直接运行py文件里面的方法
"""
def test_add():
    assert 1+1 == 2

def test_zhihu_index():
    # pyappium = PyAppium(desired_caps=Config.zhihu_desired_caps)
    assert True

"""
    2. 可以支持类，成员也是test_开头
"""
class TestPytest():
    def test_add(self):
        assert 1+1 == 2

    def test_zhihu_index(self):
        # pyappium = PyAppium(desired_caps=Config.zhihu_desired_caps)
        assert True