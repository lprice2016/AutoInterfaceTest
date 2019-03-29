#/usr/bin/env python
#-*- coding:utf-8 -*-


import os

import sys
#对文件处理
import codecs

import importlib


importlib.reload(sys)


import configparser
#ConfigParser模块在python中用来读取配置文件，配置文件的格式跟windows下的ini配置文件相似，可以包含一个或多个节(section),
# 每个节可以有多个参数（键=值）。使用的配置文件的好处就是不用在程序员写死，可以使程序更灵活。


proDir = os.path.split(os.path.realpath(__file__))[0]
#根目录
rootDir = os.path.split(proDir)[0]
#配置文件根目录
configPath = os.path.join(rootDir,"config")
#DB配置文件目录
DBConfigPath = os.path.join(configPath,"DBConfig")
#HttpConfig 配置文件目录
HttpConfigPath = os.path.join(configPath,"HttpConfig")
#Email配置文件目录
EmailConfigPath = os.path.join(configPath,"EmailConfig")
#Email配置文件目录
ResConfigPath = os.path.join(configPath,"ResConfig")


class ReadConfig:
    def __init__(self):
        #print("heheh")
        #读取数据录的配置
        DBFd = open(DBConfigPath,encoding='utf-8')
        DBdata = DBFd.read()
        #读取Http目录的配置
        HttpFd = open(HttpConfigPath,encoding='utf-8')
        HttpData = HttpFd.read()
        #读取Email目录配置
        EmailFd = open(EmailConfigPath,encoding='utf-8')
        EmailData = EmailFd.read()
        #读取Response目录配置
        ResFd = open(ResConfigPath,encoding="utf-8")
        ResData = ResFd.read()
        #remove BOM
        for data,dataFD in zip([DBdata,HttpData,EmailData,ResData],[DBFd,HttpFd,EmailFd,ResFd]):
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                dataFile = codecs.open(DBConfigPath,'w')
                dataFile.write(DBdata)
                dataFile.close()
                dataFD.closed()

        #创建一个读取配置文件对象，读取数据库配置文件
        self.DBCF = configparser.ConfigParser()
        #读取配置文件，传入一个文件路径名称即可，读取数据库文件
        self.DBCF.read(DBConfigPath,encoding="utf-8")
        #创建一个读取HttpConfig的配置文件
        self.HttpCF = configparser.ConfigParser()
        self.HttpCF.read(HttpConfigPath,encoding="utf-8")
        #创建一个读取EmailConfig的配置文件
        self.EmailCF = configparser.ConfigParser()
        self.EmailCF.read(EmailConfigPath,encoding="utf-8")
        # 创建一个读取ResConfig的配置文件
        self.ResCF = configparser.ConfigParser()
        self.ResCF.read(ResConfigPath,encoding="utf-8")
    def getDBConfig(self,name):
        value = self.DBCF.get("DATABASE",name)
        return value
    def getHttpConfig(self,name):
        value = self.HttpCF.get("HTTP",name)
        return value
    def setHttpConfig(self,name):
        self.HttpCF.set("HTTP",name)
    def getEmailConfig(self,name):
        value = self.EmailCF.get("EMAIL",name)
        return value
    def setEmailConfig(self,name,value):
        self.EmailCF.set("EMAIL",name,value)
    def getReslConfig(self,name):
        value = self.ResCF.get("Response",name)
        return value
    def setReslConfig(self,name,value):
        self.ResCF.set("Response",name,value)
        self.ResCF.write(open(ResConfigPath, 'w',encoding="utf-8"))


if __name__ == "__main__":
    dd = ReadConfig()