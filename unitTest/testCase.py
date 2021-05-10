# -*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/4/27 17:56
# @Software: PyCharm
# @File    : testCase.py
import unittest



class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    #     加断言

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 41, '5*8结果错了')


if __name__ == '__main__':
    unittest.main()
