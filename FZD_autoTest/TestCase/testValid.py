#/usr/bin/env python
#-*- coding:utf-8 -*-

"""跟注册相关的case均放在这边"""
import unittest,requests

from Common import common
import Common.ConfigHttp as configHttp

from Common.Log import MyLog as log

from Common.ReadConfig import ReadConfig as readConfig

import datetime

import json



class MyTest(unittest.TestCase):
    """短信验证码-验证"""
    def setUp(self):
        pass
    def testValid(self):
        """短信验证码-验证"""
        self.cls = common.getXls("testCase.xlsx","test1")
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.Http = configHttp.ConfigHttp()
        self.HttpUrl = self.Http.setUrl(self.cls.get(2).get("url"))
        self.logger.info(self.HttpUrl)
        TempParams = json.loads(self.cls.get(2).get("params"))
        self.readConfig = readConfig()
        TempParams["mobile"] = self.readConfig.getReslConfig("mobile")
        self.params =json.dumps(TempParams)
        self.logger.info(self.params)
        self.Http.setParams(self.params)
        self.r = self.Http.post()
        self.r.status_code
        self.r.encoding = 'utf-8'
        self.logger.info("result-----------",self.r.json().get("errorCode"))
        assert self.r.status_code == 200,"请求失败"
        assert self.r.json().get("errorCode") == "0000000","响应失败"
        #assert self.r.status_code == 200
    def tearDown(self):
        print("tearDown")
# if __name__ == "__main__":
#     ss = MyTest()
#     ss.testValid()


