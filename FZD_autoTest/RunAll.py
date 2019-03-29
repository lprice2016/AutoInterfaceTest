# #/usr/bin/env python
# #-*- coding:utf-8 -*-

#

import unittest

import HTMLTestRunner

import os
import os.path
import jpype
import threading
from Common import common

from Common.Log import MyLog as log


import Common.ReadConfig as readConfig

from Common.ConfigEmail import MyEmail
from Common.createIdNumAndRealName import CreateIdAndRealName

import xlrd


class RunAllCaseList:
    def __init__(self):
        self.caseListPath = os.path.join(readConfig.rootDir,"caseList")
        self.caseList = []

        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.reportPath = self.log.getReprotPath()
        self.email = MyEmail.getEmail()
        self.onOff = self.email.onOff

    def setCaseList(self):
        fb = open(self.caseListPath)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n",""))
            fb.close()
    def setCaseSuite(self):
        self.setCaseList()
        testSuite = unittest.TestSuite()
        suiteModel = []
        for case in self.caseList:
            caseFile = os.path.join(readConfig.rootDir,"TestCase")
            caseName = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(caseFile,pattern=caseName + ".py",top_level_dir=None)
            suiteModel.append(discover)

        if len(suiteModel) > 0:
            for suite in suiteModel:
                for testName in suite:
                    testSuite.addTest(testName)
        else:
            return None
        return testSuite
    def run(self):
        try:
            suite = self.setCaseSuite()
            if suite is not None:
                self.logger.info("***********测试开始***********")
                fp = open(self.reportPath,'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description=None)
                runner.run(suite)
                fp.close()
            else:
                self.logger.info("没有case进行测试")
        except Exception as ex:
            self.logger.error(ex)
        finally:
            if int(self.onOff) == 0:
                self.logger.info("发送邮件")
                self.email.sendEmail()
            elif int(self.onOff) == 1:
                self.logger.info("不会发送邮件给开发人员")
            else:
                self.logger.info("没有设定邮件是否发送的状态")
            self.logger.info("*********测试结束**********")



if __name__ == "__main__":
    #数据准备,如果mobile 在数据库中存在则重新生成
    if common.MobileIsNotExist():
        tt = RunAllCaseList()
        tt.run()
        jpype.shutdownJVM()

