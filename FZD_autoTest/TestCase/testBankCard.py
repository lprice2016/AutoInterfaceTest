#/usr/bin/env python
#-*- coding:utf-8 -*-

"""跟注册相关的case均放在这边"""
import unittest,requests

from Common import common
import Common.ConfigHttp as configHttp
import json
from Common.Log import MyLog as log
import threading

from Common import ReadConfig

from Common.createIdNumAndRealName import CreateIdAndRealName



class MyTest(unittest.TestCase):
    """银行卡认证-发短信"""
    def setUp(self):
        # #随机生成身份证和姓名
        # IdNumAndRealName = CreateIdAndRealName()
        # IdNumAndRealName.createIdNumAndName()
        pass

    def testBankCard(self):
        """银行卡认证-发短信"""
        self.cls = common.getXls("testCase.xlsx","test1")
        self.log = log.get_log()
        self.readConfig = ReadConfig.ReadConfig()
        self.logger = self.log.getLogger()
        self.Http = configHttp.ConfigHttp()
        self.HttpUrl = self.Http.setUrl(self.cls.get(8).get("url"))
        self.logger.info(self.HttpUrl)
        TempParams = json.loads(self.cls.get(8).get("params"))
        self.readConfig.setReslConfig("channelId",common.getChannelId())
        #TempParams["channelId"] = self.readConfig.getReslConfig("channelId")
        TempParams["mobile"] = self.readConfig.getReslConfig("mobile")
        TempParams["idCard"] = self.readConfig.getReslConfig("idnum")
        TempParams["name"] = self.readConfig.getReslConfig("realname")
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

    def tearDown(self):
        #self.confige.setReslConfig("imgCodeId",self.imgCodeId)
        print("tearDown")
if __name__ == "__main__":
    tt =  MyTest()
    tt.testBankCard()
    #print(cc)

