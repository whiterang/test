import unittest

#TestCase:一个类，把测试用例封装倒方法
class TestCaseUnittest(unittest.TestCase):

# #以test_开头
#     def test_01(self):
#         a = 1
#         b = 2
#         print(a==b)
#         print("test_01")


#     def test_02(self):
#         a = 1
#         b = 2
#         print(a==b)
#         print("test02")

        def test_03(self):
            a=2
            b=2
            # self.assertEqual(a,b,"用例失败")
            self.assertNotEqual(a,b)
    
unittest.main()


