# 1.导入Unittest
import unittest

# TestCase:一个类，把测试用例封装到方法
class TestCaseUnittest(unittest.TestCase):
    
    # unittest类开始执行的时候，首先调用setUpClass方法
    # classmethod：申明此类是一个类方法，去告诉python这是一个类方法，不需要初始化
    # staticmethod: 静态方法
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass")

    # tearDownClass：在这个类执行完成之后，最后去调用tearDownClass
    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass")

    # setup方法：每个成员方法执行之前，会去执行setUp方法
    def setUp(self):
        print("\nsetup")

    # tearDown方法：每个成员方法执行结束后，回去执行tearDown方法
    def tearDown(self):
        print("\ntearDown")

    # 每个方法以test_开头
    def test_01(self):
        print("\ntest_01")

    def test_02(self):
        print("\ntest_02")

unittest.main()