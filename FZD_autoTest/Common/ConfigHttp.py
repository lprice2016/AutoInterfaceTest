#/usr/bin/env python
#-*- coding:utf-8 -*-


import requests
import json
import binascii
import jpype
import time
import os
import threading
from Common import ReadConfig as readConfig

from Common.Log import MyLog as log
import datetime
import random
import string
import hashlib
import time




localReadConfig = readConfig.ReadConfig()

jvmPath = jpype.getDefaultJVMPath()
jpype.startJVM(jvmPath, "-ea", "-Djava.ext.dirs=/Users/user/PycharmProjects/FZD_autoTest/lib/")
JDClassNonce = jpype.JClass("com.dzjk.jmeter.functions.NoncestrGenerate")
JDClassSign = jpype.JClass("com.dzjk.jmeter.functions.SignatureUtil")
class ConfigHttp:
    def __init__(self):
        global host,port,timeOut
        host = localReadConfig.getHttpConfig("host")
        port = localReadConfig.getHttpConfig("port")
        #timeout：设置接口连接的最大时间（超过该时间会抛出超时错误）
        timeOut = localReadConfig.getHttpConfig("timeOut")
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        #headers：定制请求头（headers），例如：content-type = application/x-www-form-urlencoded
        self.headers = eval(localReadConfig.getHttpConfig("header"))
        #params：用于传递测试接口所要用的参数，这里我们用python中的字典形式（key：value）进行参数的传递。
        self.params = {}
        self.data = {}
        #url：显而易见，就是接口的地址url啦
        self.url = None
        self.files = {}
    def setUrl(self,url):
        self.url = host + url
        self.logger.info(self.url)
    def setHeaders(self,key,values):
        self.headers[key] = values
        self.logger.info("header",self.headers)
    def generateRandomStr(self,randomlength=23):
        """生成一个制定长度的字符串"""
        noncestr = JDClassNonce.getRandomString(23)
        return noncestr
    def md5(self,data):
        m = hashlib.md5()
        m.update(str(data).encode())
        m.hexdigest()
        return m
    def getSignature(self,data):
        m = hashlib.md5()
        print(data)
        m.update(str(data).encode())
        #获取sign
        sign = m.hexdigest()
        return sign

    def setSignMd(self,param):
        data = {}
        requestBody = {}
        if param is not None and len(param) != 0:
            requestBody["request"] = json.loads(param)
            for key in requestBody["request"].keys():
                data[key] = requestBody["request"].get(key)
            requestBody["request"] = json.dumps(requestBody["request"])
        else:
            requestBody["request"] = ""
        data['timestamp'] = int(round(time.time() * 1000))
        data["noncestr"] =self.generateRandomStr(23)
        data["appId"]="fzd"
        self.logger.info(requestBody.get("request"))
        self.logger.info(data)
        data["signature"] = self.getSignatureUtil(requestBody.get("request"),data.get("appId"),data.get("noncestr"),data.get("timestamp"))
        self.logger.info(data)
        return data

    def setParams(self,param):
        self.params = self.setSignMd(param)
        self.data = json.dumps(self.params)
    def setFiles(self,file):
        self.files = file
    def getSignatureUtil(self,request,prodyctId,Noncestr,timeStamp):
        getSignatureUtil = JDClassSign.doSecurity(request,prodyctId,Noncestr,timeStamp)
        #jpype.shutdownJVM()
        return getSignatureUtil

    def get(self):
        try:
            response = requests.get(self.url,params=self.params,headers = self.headers,timeout = float(timeOut))
            return response
        except TimeoutError:
            self.logger.error("Time out!!")
            return None

    def post(self):
        try:
            response = requests.post(self.url,headers = self.headers,data=self.data,files = self.files,timeout = float(timeOut))
            return response
        except TimeoutError:
            self.logger.error("Time Out!!")
        return None
if __name__ == "__main__":
    ss= '{"type": "register", "imgCode": "8888", "mobile": "15203081314"}'
    dd = json.loads(ss)
    print(dd.keys())
    for i in dd.keys():
        print(i)



