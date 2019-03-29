#/usr/bin/env python
#-*- coding:utf-8 -*-

import pymysql

from Common import ReadConfig as readConfig

from Common.Log import MyLog as log

localReadConfig = readConfig.ReadConfig()


class MyDB:
    global host,userName,passWord,port,dataBase,config
    host = localReadConfig.getDBConfig("host")
    userName = localReadConfig.getDBConfig("userName")
    passWord = localReadConfig.getDBConfig("passWord")
    port = localReadConfig.getDBConfig("port")
    dataBase = localReadConfig.getDBConfig("dataBase")
    config = {
        "host":str(host),
        "user":userName,
        "passwd":passWord,
        "port":int(port),
        "db":dataBase
    }

    def __init__(self):
        self.log = log.get_log()
        self.logger = self.log.getLogger()

        self.db = None
        self.cursor = None
    def connectDB(self):
        try:
            #链接DB
            self.db = pymysql.connect(**config)
            #创建游标
            self.cursor = self.db.cursor()
            self.logger.info("链接数据库成功")
        except ConnectionError as e:
            self.logger.error(e)
    def executeSQL(self,sql):
        self.connectDB()
        #执行sql
        self.cursor.execute(sql)
        #执行完成sql之后进行提交
        self.db.commit()
        return self.cursor
    def getAll(self):
        value = self.cursor.fetchall()
        return value
    def getOne(self):
        value = self.cursor.fetchone()
        return value
    def closeDB(self):
        try:
            self.db.close()
            self.logger.info("数据库关闭")
        except Exception as e:
            self.logger.error(e)