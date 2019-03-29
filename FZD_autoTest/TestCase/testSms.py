#/usr/bin/env python
#-*- coding:utf-8 -*-

"""跟注册相关的case均放在这边"""
import unittest,requests

from Common import common
import Common.ConfigHttp as configHttp

from Common.Log import MyLog as log

from Common.ReadConfig import ReadConfig

import datetime

import json



class MyTest(unittest.TestCase):
    """短信验证码"""
    def setUp(self):
        pass
    def testSms(self):
        """短信验证码"""
        self.readConfig = ReadConfig()
        self.imgcodeid = self.readConfig.getReslConfig("imgCodeId")
        self.cls = common.getXls("testCase.xlsx","test1")
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.Http = configHttp.ConfigHttp()
        self.HttpUrl = self.Http.setUrl(self.cls.get(1).get("url"))
        self.logger.info(self.HttpUrl)
        TempParams = json.loads(self.cls.get(1).get("params"))
        TempParams["imgCodeId"] = self.imgcodeid
        TempParams["mobile"] = self.readConfig.getReslConfig("mobile")
        self.params =json.dumps(TempParams)
        self.Http.setParams(self.params)
        self.r = self.Http.get()
        self.r.status_code
        self.r.encoding = 'utf-8'
        self.logger.info("result-----------",self.r.json().get("errorCode"))
        self.logger.info(self.r.status_code)
        assert self.r.status_code == 200,"请求失败"
        assert self.r.json().get("errorCode") == "0000000","响应失败"
    def tearDown(self):
        print("tearDown")
if __name__ == "__main__":
    tt =  MyTest()
    tt.testSms()


