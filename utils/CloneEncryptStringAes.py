#-*- coding: utf-8 -*-
# @Author  : wuqi
# @Time    : 2021/5/12 14:56
# @Software: PyCharm
# @File    : CloneEncryptStringAes.py
import jpype
import os,time
from unitTest.get_data import GetData
import logger


class CloneEncryptStringAes:
    def aes_encrypt(self, token):
        jvmPath = r'C:\Program Files\Java\jdk1.8.0_201\jre\bin\server\jvm.dll'
        # print(jvmPath)
        jar_path = os.path.join(os.path.abspath('.'), 'CloneEncryptStringAes.class')  # jar包路径
        # print(jar_path)
        jpype.startJVM(jvmPath, '-ea', "-Djava.class.path={}".format(os.path.abspath('.')), convertStrings=True)
        JClass = jpype.JClass("CloneEncryptStringAes")
        instance = JClass()
        # 对公网token加密
        # 加密规则：将公网token+时间戳(13位)进行拼接，然后使用aes加密
        token_plus_timestamp = token+str(int(round(time.time()*1000)))
        encrypted_token = instance.encryptAes(token_plus_timestamp)
        # jpype.shutdownJVM()
        setattr(GetData, 'pvt_token', encrypted_token)
        # return encrypted_token

    # def aes_encrypt1(self, token):
    #     class_path = r'F:\20210220\utils'
    #     if not os.path.exists(os.path.join(class_path, "CloneEncryptStringAes.class")):
    #         logger.error("指定目录{}无法找到文件{}".format(class_path, "CloneEncryptStringAes.class"))
    #         return
    #     # 对公网token加密
    #     # 加密规则：将公网token+时间戳(13位)进行拼接，然后使用aes加密
    #     token_plus_timestamp = token + str(int(round(time.time() * 1000)))
    #     # 启动jvm,注意class_path是目录，不用带上class文件名
    #     if not jpype.isJVMStarted():
    #         jpype.startJVM(jpype.getDefaultJVMPath(), "-ea",
    #                        "-Djava.class.path={}".format(os.path.realpath(class_path)), convertStrings=True)
    #     print(class_path)
    #     aes_class = jpype.JClass("CloneEncryptStringAes")
    #     aes_instance = aes_class()
    #     encrypted_token = aes_instance.encryptAes(token_plus_timestamp)
    #     # 关闭JVM
    #     # jpype.shutdownJVM()
    #     return encrypted_token


if __name__ == '__main__':
    CloneEncryptStringAes().aes_encrypt('eTir/N9Z7ddMjuvo8M5MJWRLAWrlJ7pUlUe2+')
    # print(CloneEncryptStringAes().aes_encrypt1('eTir/N9Z7ddMjuvo8M5MJWRLAWrlJ7pUlUe2+'))
    print(getattr(GetData, 'pvt_token'))