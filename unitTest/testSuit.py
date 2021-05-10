# -*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/4/29 14:32
# @Software: PyCharm
# @File    : testSuit.py
import unittest
from unitTest.testCase import IntegerArithmeticTestCase
import HTMLTestRunnerNew

suite = unittest.TestSuite()  # 存储用例

# 添加用例方法1：
suite.addTest(IntegerArithmeticTestCase('testAdd'))
suite.addTest(IntegerArithmeticTestCase('testMultiply'))

# # 添加用例方法2：TestLoader
# loader = unittest.TestLoader()  # 创建一个加载器
# # 2.1 从类导入
# suite.addTest(loader.loadTestsFromTestCase(IntegerArithmeticTestCase))
#
# # 2.2 从模块导入
# from unitTest import testCase
#
# suite.addTest(loader.loadTestsFromModule(testCase))


"""
！！！测试报告！！！
"""

# 一、原始版：

# file = open('testResult.txt', 'w+', encoding='utf-8')
# runner = unittest.TextTestRunner(stream=file, verbosity=2)  # verbosity有三个值，分别是0、1、2，结果详细程度依次递增
# runner.run(suite)

# 使用上下文管理器，文件自动关闭
# with open('testResult.txt', 'w+', encoding='utf-8') as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)  # verbosity有三个值，分别是0、1、2，结果详细程度依次递增
#     runner.run(suite)

# 二、进阶版（生成HTML报告）
with open("test_report.html", 'wb') as html:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=html, verbosity=2, title='测试报告', description='--这是描述--',
                                              tester='靓仔')
    runner.run(suite)
