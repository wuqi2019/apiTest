# -*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/4/27 15:41
# @Software: PyCharm
# @File    : getRedisValue.py

import redis
from readconfig import readConfig


class getRedisValue:

    @staticmethod
    def getValue(key):
        host = readConfig().getValue('host')
        port = readConfig().getValue('port')
        password = readConfig().getValue('password')
        redis_obj = redis.Redis(host=host, port=port, password=password, decode_responses=True)
        return redis_obj.get(key)


if __name__ == '__main__':
    conn = getRedisValue()
    print(conn.getValue("edl:sms_total:18800000077"))



