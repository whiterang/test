import unittest

class TestCase01(unittest.TestCase):
    
    def test_01(self):
        print("这是TestCase01的第01个测试用例")
        self.assertEqual(1+1, 2, "1+1不等于2")   

    def test_02(self):
        print("这是TestCase01的第02个测试用例")
        self.assertEqual(1+1, 2, "1+1不等于2")        