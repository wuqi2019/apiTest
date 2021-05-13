#-*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/5/10 16:16
# @Software: PyCharm
# @File    : test.py


class getData:
    data = '初始属性'


if __name__ == '__main__':
    print(getData.data)
    setattr(getData, 'data', '修改后的属性')   # 此方法可以用于设置token、cookie等
    print(getData.data)
    print(hasattr(getData, 'data'))
    delattr(getData, 'data')
    print(hasattr(getData, 'data'))
