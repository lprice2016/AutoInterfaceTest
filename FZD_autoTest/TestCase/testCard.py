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
    """身份认证"""
    def setUp(self):
        pass
    def testApply(self):
        """身份认证"""
        self.cls = common.getXls("testCase.xlsx","test1")
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.Http = configHttp.ConfigHttp()
        self.HttpUrl = self.Http.setUrl(self.cls.get(5).get("url"))
        self.logger.info(self.HttpUrl)
        TempParams = json.loads(self.cls.get(5).get("params"))
        self.readConfig = readConfig()
        TempParams["idNum"] = self.readConfig.getReslConfig("idnum")
        TempParams["realName"] = self.readConfig.getReslConfig("realname")
        self.params =json.dumps(TempParams)
        self.logger.info(self.params)
        self.Http.setParams(self.params)
        self.Http.setHeaders("jwt",self.readConfig.getReslConfig("jwt"))
        self.r = self.Http.post()
        self.r.status_code
        self.r.encoding = 'utf-8'
        self.logger.info("result-----------",self.r.json().get("errorCode"))
        assert self.r.status_code == 200,"请求失败"
        assert self.r.json().get("errorCode") == "0000000","响应失败"

        #assert self.r.status_code == 200
    def tearDown(self):
        #self.confige.setReslConfig("applyCode",self.r.json().get("data").get("applyCode"))
        print("tearDown")
if __name__ == "__main__":
    ss = MyTest()
    ss.testApply()


