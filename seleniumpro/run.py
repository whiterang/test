import unittest
from utils.HTMLTestRunner import HTMLTestRunner


testcase=unittest.defaultTestLoader.discover("./testcases","testcase_*.py")

testsuites = unittest.TestSuite()
testsuites.addTests(testcase)


title="猫宁自动化测试报告"
descr="这是猫宁项目web自动化测试报告的详细内容"
file_path="./reports/unittest_report.html"
with open(file_path,"wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuites)