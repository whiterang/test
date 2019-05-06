
def python_assert():
    """
        python自带的断言
    """
    a = 1+1
    b = 2
    assert a == b
    print("这是python自带的断言,断言通过！")

    assert 1 == 2
    print("断言1=2通过")

# python_assert()

import unittest
class TestCaseAssert(unittest.TestCase):

    def t1est_01(self):
        # 等于
        # a = 1
        # b = 2
        # self.assertEqual(b, a, "a不等于b失败!") # 断言相等
        # self.assertNotEqual(a, b) # 断言不等

        # 真假
        # flag = True
        # self.assertTrue(flag, "flag不是True")    # 判断真假
        # self.assertFalse(flag, "flag不是False")
        
        # 包含
        # str1 = "ljtest, good job!"
        # str2 = "ljtest"
        # self.assertIn(str2, str1)
        # self.assertNotIn(str2, str1)

        # 是否为空,不是空字符串"",而是判断是为None
        # a = None
        # self.assertIsNone(a)
        # self.assertIsNotNone(a)
        
        # 判断是否为某一个类型
        # "123" == str类型
        # [1,3,4] == list类型
        # {"username": "123"} == dict
        b = ""
        c = [1,2,3,4]
        d = {"username": "123"}
        self.assertIsInstance(b, str)
        self.assertIsInstance(c, list)
        self.assertIsInstance(d, dict)
        self.assertNotIsInstance(b, str)
        
    def test_failed(self):
        self.assertTrue(False)

    def test_error(self):
        a = 1/0


unittest.main()