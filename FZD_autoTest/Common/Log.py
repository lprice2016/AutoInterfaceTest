#/usr/bin/env python
#-*- coding:utf-8 -*-

import logging

from datetime import datetime

import threading

import os

from Common import ReadConfig


class Log:

    def __init__(self):

        global logPath,resultPath,rootPath,reportPath

        rootPath = ReadConfig.rootDir
        resultPath = os.path.join(rootPath,"resultReport")

        logPath = os.path.join(resultPath,str(datetime.now().strftime("%Y年%m月%d日%H时%M分%S秒")))

        reportPath = os.path.join(logPath,"reprot.html")

        logInfoPath = os.path.join(logPath,"out.txt")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()

        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(logInfoPath)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)
    def getLogger(self):
        return self.logger
    def getReprotPath(self):
        return reportPath
    def getResultPath(self):
        return resultPath


class MyLog:
    log = None
    mutext = threading.Lock()
    def __init__(self):
        pass
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutext.acquire()
            MyLog.log = Log()
            MyLog.mutext.release()
        return MyLog.log

