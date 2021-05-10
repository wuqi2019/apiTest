#-*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/2/20 15:24
# @Software: PyCharm
# @File    : test0220.py
class TestA:
    a = '123'
    def print_self(self):
        print(self)
        print("{0}{1}{2}{3}".format("0", "1", "2", "3"))


a = TestA()
a.print_self()
print(a.a)