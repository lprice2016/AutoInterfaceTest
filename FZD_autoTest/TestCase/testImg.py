#/usr/bin/env python
#-*- coding:utf-8 -*-

"""跟注册相关的case均放在这边"""
import unittest,requests

from Common import common
import Common.ConfigHttp as configHttp

from Common.Log import MyLog as log
import threading

from Common.ReadConfig import ReadConfig

import datetime
from Common.createIdNumAndRealName import CreateIdAndRealName

# 随机生成身份证和姓名
IdNumAndRealName = CreateIdAndRealName()
IdNumAndRealName.createIdNumAndName()

class MyTest(unittest.TestCase):
    """获取图形验证码"""
    def setUp(self):
        self.confige = ReadConfig()
    def testImg(self):
        """获取图形验证码"""
        self.cls = common.getXls("testCase.xlsx","test1")
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.Http = configHttp.ConfigHttp()
        self.HttpUrl = self.Http.setUrl(self.cls.get(0).get("url"))
        self.logger.info(self.HttpUrl)
        self.Http.setParams(self.cls.get(0).get("params"))
        self.r = self.Http.get()
        self.r.status_code
        self.r.encoding = 'utf-8'
        self.logger.info("result-----------",self.r.json().get("errorCode"))
        assert self.r.status_code == 200,"请求失败"
        assert self.r.json().get("errorCode") == "0000000","响应失败"
        self.imgCodeId = self.r.json().get("data").get("imgCodeId")
        self.confige.setReslConfig("imgCodeId",self.imgCodeId)
    def testImg1(self):
        """获取图形验证码"""
        self.cls = common.getXls("testCase.xlsx","test1")
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.Http = configHttp.ConfigHttp()
        self.HttpUrl = self.Http.setUrl(self.cls.get(0).get("url"))
        self.logger.info(self.HttpUrl)
        self.Http.setParams(self.cls.get(0).get("params"))
        self.r = self.Http.get()
        self.r.status_code
        self.r.encoding = 'utf-8'
        self.r.text
        self.logger.info(self.r.text)
        self.logger.info(self.r.status_code)
        self.imgCodeId = self.r.json().get("data").get("imgCodeId")
        self.confige.setReslConfig("imgCodeId",self.imgCodeId)
    def tearDown(self):
        self.confige.setReslConfig("imgCodeId",self.imgCodeId)
        print("tearDown")
# if __name__ == "__main__":
#     # tt =  MyTest()
#     # tt.testImg()
#
#     cc = ReadConfig()
#     cc.setReslConfig("name_2","values_2")
#     #print(cc)

