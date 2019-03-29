#/usr/bin/env python
#-*- coding:utf-8 -*-

from Common.ReadConfig import ReadConfig
from random import choice


class CreateMobile:
    def __init__(self):
        self.mobile_num = ""
        self.readConfig = ReadConfig()
        pass
    def getRandomDigit(self):
        return choice(['0','1','2','3','4','5','6','7','8','9'])
    def create(self):
        #130-133号段是联通的，134-139号段是移动的。移动现在还获得了159号段。
        mobile_3 = choice(["130","131","132","133","134","135","136","137","138","138","159"])
        self.mobile_num += mobile_3
        while(len(self.mobile_num) < 11):
            self.mobile_num += self.getRandomDigit()
        self.readConfig.setReslConfig("mobile",self.mobile_num)
        return self.mobile_num

if __name__ == "__main__":
    cc = CreateMobile()
    print(cc.create())
    print(cc.mobile_num)

