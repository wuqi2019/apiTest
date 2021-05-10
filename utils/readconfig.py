# -*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/4/29 17:32
# @Software: PyCharm
# @File    : readconfig.py
import configparser


class readConfig:
    configPath = r'F:\20210220\configFile\config.ini'
    sections = 'Redis_test'

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(readConfig.configPath)
        self.item = self.cf.items(readConfig.sections)

    def getValue(self, key):
        return self.cf.get(readConfig.sections, key)


if __name__ == '__main__':
    rc = readConfig()
    print(rc.getValue('host'))
    print(rc.getValue('port'))
    print(rc.getValue('password'))

