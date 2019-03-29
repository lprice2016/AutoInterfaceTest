#/usr/bin/env python
#-*- coding:utf-8 -*-

import paramiko
class ReSetFeTime():
    def __init__(self):
        self.ss1 =  paramiko.SSHClient()
        self.ss2 = paramiko.SSHClient()
        self.ss1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ss2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    def setFeTime(self):
        self.ss1.connect()
