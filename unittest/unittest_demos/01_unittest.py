# 1.导入Unittest
import unittest

# TestCase:一个类，把测试用例封装到方法
class TestCaseUnittest(unittest.TestCase):
    
    # 每个方法以test_开头
    def test_01(self):
        print("test01")
        a = 1
        b = 2
        print(a == b)

    def test_02(self):
        print("\ntest02")
        c = 1/0
    
    def get_username(self):
        print("get_username")

unittest.main()