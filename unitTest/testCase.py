# -*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/4/27 17:56
# @Software: PyCharm
# @File    : testCase.py
import unittest
from utils.xlutils import xl
import requests
import json
from unitTest.get_data import GetData


# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):  # test method names begin with 'test'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#
#     #     加断言
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 41, '5*8结果错了')
#
#
# if __name__ == '__main__':
#     unittest.main()


class HttpRequest(unittest.TestCase):
    # def __init__(self, url, data, method, methodName):
    #     super(HttpRequest, self).__init__(methodName)
    #     self.url = url
    #     self.data = data
    #     self.method = method
    #
    # def test_api(self, method):
    #     if self.method == 'GET':
    #         res = requests.get(self.url+'?'+self.data)

    def login(self):
        data = {"phone": "18581438351",
                "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee",
                "deviceId": "d91c170b6d1445b6b0b1d762bd88dc6e"
                }
        res = requests.post(url='http://testbmcapp.hikcreate.com/v1/user/login/gesture', data=json.dumps(data), header=getattr(GetData, 'header'))
        return res


if __name__ == '__main__':
    print(HttpRequest.login())