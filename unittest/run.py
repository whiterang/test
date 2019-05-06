import unittest
from utils.HTMLTestRunner import HTMLTestRunner


testcase=unittest.defaultTestLoader.discover("./testcases","testcase*.py")
testsuites=unittest.TestSuite()
testsuites.addTests(testcase)

# 第一种方法：
# runner=unittest.TextTestRunner()
# runner.run(testsuites)


# 第二种方法
title="测试报告"
descr="这是测试报告"
file_path="./reports/unittest_report.html"
with open(file_path,"wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuites)


"""
    首先新建一个运行入口：run.py
"""

# import unittest # 模块
# from utils.HTMLTestRunner import HTMLTestRunner

# # 1. 去查找testcases模块下面所有的testcase开头的py文件
# # 第一个参数是要寻找什么目录下面的case
# # 第二个参数是要匹配以什么字符串开头的/以什么字符串结尾的文件
# testcases = unittest.defaultTestLoader.discover("./testcases", "testcase*.py")  # 去查找testcase下面所有的testcase开头.py文件结尾的测试用例
# testsuites = unittest.TestSuite()       # 去实例化一个TestSuite()，创建测试集合
# testsuites.addTests(testcases)          # 用测试集去加载所有的测试用例

# # 第一种自带的： 使用unittest的run工具去运行测试集，很low，不推荐
# # runner = unittest.TextTestRunner()      
# # runner.run(testsuites)
# 推荐使用第二种：使用htmltestrunner这个工具去帮我们运行测试集，并生成高大山的html测试报告，高大山
# title = "测试报告"
# descr = "这是测试报告的描述文字"
# file_path = "./reports/unittest_report.html"
# with open(file_path, "wb") as f:            # 新建一个文件，并发对象赋值给f
#     runner = HTMLTestRunner(stream=f, title=title, description=descr)   # 并且把测试结果方法这个f文件里面
#     runner.run(testsuites)                                              # 再去用htmltestrunner去运行测试集