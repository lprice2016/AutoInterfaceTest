#/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from xlrd import open_workbook

from xml.etree import ElementTree as ElementTree

from Common import ReadConfig

from Common.Log import MyLog as Log

from Common import ConfigHttp

from Common import ConfigDB
from Common import CreateMobile

global rootPath

rootPath = ReadConfig.rootDir

localConfigHttp = ConfigHttp.ConfigHttp()

log = Log.get_log()
logger = log.getLogger()


#从excel文件中读取测试用例

def getXls(xlsName,sheetName):
    xlsNameValues = {}
    cls = []
    xlsPath = os.path.join(rootPath,"testFile",xlsName)
    file = open_workbook(xlsPath)

    sheet = file.sheet_by_name(sheetName)
    nRows = sheet.nrows
    clsTitileName = sheet.row_values(0)
    for i in range(nRows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    i = 0
    for values in cls:
        xlsNameValuesTmp = {}
        for title,value in zip(clsTitileName,values):
            xlsNameValuesTmp[title] = value
        xlsNameValues[i] = xlsNameValuesTmp
        i += 1
    return xlsNameValues
#从xml文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(rootPath,"testFile","SQL.xml")
        tree = ElementTree.parse(sql_path)
        root = tree.getroot()
        for db in root:
            #print(db.tag,db.attrib)
            table = {}
            for tb in db:
                sql = {}
                #print(tb.tag,tb.attrib)
                for sql_id in tb:
                    id =sql_id.attrib.get("id")
                    sql[id] = sql_id.text
                table[tb.attrib.get("name")] = sql
            database[db.attrib.get("name")] = table
def get_xml_dict(database_name,table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name,table_name,sql_id):
    db = get_xml_dict(database_name,table_name)
    sql = db.get(sql_id)
    return sql
#数据生成
def MobileIsNotExist():
    log = Log.get_log()
    logger =log.getLogger()
    #链接数据库
    db = ConfigDB.MyDB()
    db.connectDB()
    mobielIsNotExist = False
    #获取sql
    mobielIsExistSql = get_sql("dzjk_user","usr_info","1")
    if mobielIsExistSql is not None:
        mobielIsExistSql = mobielIsExistSql.strip()
        #创建moblie
        c = CreateMobile.CreateMobile()
        mobile = c.create()
        mobielIsExistSql = mobielIsExistSql.replace("${mobile}",mobile)
        db.executeSQL(mobielIsExistSql)
        if not db.getOne():
            mobielIsNotExist = True
        else:
            mobielIsNotExist = False
    db.closeDB()
    return mobielIsNotExist
def getChannelId():
    log = Log.get_log()
    logger = log.getLogger()
    #链接数据库
    db = ConfigDB.MyDB()
    db.connectDB()
    getChannelIdSql = get_sql("dzjk_user1","usr_channel","2")
    db.executeSQL(getChannelIdSql)
    ChannelId = db.getOne()
    if ChannelId:
        db.closeDB()
        return ChannelId[0]
    else:
        logger.info("获取ChannelId 报错！！！")
        db.closeDB()




# if __name__ == "__main__":
#     mobielIsExistSql = getChannelId()
#     print(mobielIsExistSql)