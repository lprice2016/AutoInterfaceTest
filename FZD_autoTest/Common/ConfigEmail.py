#/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import smtplib

from email.mime.multipart import  MIMEMultipart

from email.mime.text import MIMEText

from datetime import datetime

from email.mime.application import MIMEApplication

import threading

from Common import ReadConfig as readConfig

from Common.Log import MyLog as log

import zipfile

import glob


localReadConfig = readConfig.ReadConfig()

class Email:
    def __init__(self):
        global host,user,password,port,sender,title,content

        host = localReadConfig.getEmailConfig("mailHost")
        user = localReadConfig.getEmailConfig("mailUser")
        password = localReadConfig.getEmailConfig("mailPass")
        port = int(localReadConfig.getEmailConfig("port"))
        sender = localReadConfig.getEmailConfig("sender")
        title = localReadConfig.getEmailConfig("subject")
        content = localReadConfig.getEmailConfig("content")
        self.receiverValue = localReadConfig.getEmailConfig("receiver")
        self.onOff = localReadConfig.getEmailConfig("onOff")

        self.receiverList = []
        #获取收件人列表
        for receiver in str(self.receiverValue).split("/"):
            self.receiverList.append(receiver)
        #定义邮件发送时间
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + " " + date
        self.log = log.get_log()
        self.logger = self.log.getLogger()
        self.msg = MIMEMultipart("mixed")

    def configHeader(self):

        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiverList)
    def configContent(self):
        contentPlain = MIMEText(content,'plain','utf-8')
        self.msg.attach(contentPlain)
    def configZipFile(self):
        #如果邮件附件不为空，则发送附件信息
        if self.checkFile():
            reportPath = self.log.getReprotPath()
            zipPath = os.path.join(readConfig.rootDir,"resultReport","test.zip")
            #zip file
            files = glob.glob(reportPath)
            f = zipfile.ZipFile(zipPath,'w',zipfile.ZIP_DEFLATED)
            for file in files:
                f.write(file)
            f.close()
            reportFile = MIMEApplication(open(zipPath,'rb').read())
            reportFile['Content-Type'] = 'applocation/octet-stream'
            reportFile['Content-Disposition'] = 'attachment;filename = "test.zip"'
            self.msg.attach(reportFile)
    def cinfigFile(self):
        if self.checkFile():
            reportFile = self.log.getReprotPath()
            #self.logger.info(reportFile)
            #self.logger.info(open(reportFile).read() + "内容为空")
            reportFileHtml = MIMEText(open(reportFile, 'rb').read(), 'base64', 'utf-8')
            reportFileHtml["Content-Type"] = 'application/octet-stream'
            reportFileHtml["Content-Disposition"] = 'attachment; filename="report.html"'
            self.msg.attach(reportFileHtml)

    def checkFile(self):
        reportPath = self.log.getReprotPath()
        if os.path.isfile(reportPath) and not os.stat(reportPath) == 0:
            return True
        else:
            return False

    def sendEmail(self):
        self.configHeader()
        self.configContent()
        self.configZipFile()
        self.cinfigFile()
        try:
            smtp = smtplib.SMTP()
            #smtp.connect(host,port)
            smtp.connect(host)
            #smtp.login(user,password)
            smtp.login(user, password)
            self.logger.info(self.receiverList)
            smtp.sendmail(sender,self.receiverList,self.msg.as_string())
            smtp.quit()
            self.logger.info("测试报告已发送！！！")
        except Exception as ex:
            self.logger.error(ex)


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def getEmail():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email





