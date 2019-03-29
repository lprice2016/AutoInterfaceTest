#/usr/bin/env python
#-*- coding:utf-8 -*-
import random
import calendar
import time
import datetime
import random
from Common import ReadConfig

areaCode = {
    "北京市":110000,
    "市辖区": 11010,
    "东城区": 110101,
    "西城区": 110102,
    "崇文区": 110103,
    "宣武区": 110104,
    "朝阳区": 110105,
    "丰台区": 110106,
    "宏伟区": 211004,
    "新北区": 320411,
    "武进区": 320412,
    "溧阳市": 320481,
    "金坛市": 320482,
    "苏州市": 320500,
    "市辖区": 320501,
    "鹤壁市": 410600,
    "市辖区": 410601,
    "鹤山区": 410602,
    "山城区": 410603,
    "淇滨区": 410611,
    "浚　县": 410621,
    "淇　县": 410622,
    "新乡市": 410700,
    "新都区": 510114,
    "温江区": 510115,
    "金堂县": 510121,
    "双流县": 510122,
    "郫　县": 510124,
    "大邑县": 510129,
    "蒲江县": 510131,
    "新津县": 510132,
    "乾　县": 610424,
    "礼泉县": 610425,
    "永寿县": 610426,
    "彬　县": 610427,
    "长武县": 610428,
    "旬邑县": 610429,
    "淳化县": 610430,
    "武功县": 610431,
    "兴平市": 610481,
    "渭南市": 610500,
    "彰武县": 210922,
    "辽阳市": 211000,
    "市辖区": 211001,
    "白塔区": 211002,
    "文圣区": 211003,
    "石景山区":11010,
    "清河门区":210905,
    "青白江区":510113
}


xing = ["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","何","吕","施","张","诸葛","第五","慕容","东方","苗","凤"
        ,"花","方"]
ming = ["蕾","磊","凯","恺","红","风","礼","通","峰","晴","花","香","娇","乐","佳","栋","东","鑫","欣","馨","玉","志","斌",
        "冰","兵","文","武","玲","莱","康","建","健","清","德","凤","悦","越","惠","辉","珞","丹","颖","亮","婧","露","璐",
        "冬","萍","劲"]
class CreateIdAndRealName():
    def __init__(self):
        self.generater = []
        self.randomCode = ""
        self.result = 0
        self.readConfig = ReadConfig.ReadConfig()

    def createIdNum(self):
        #生成地区号
        index = int(random.random()*len(areaCode))
        values = list(areaCode.values())
        self.generater.append(values[index])
        #生日
        birth_year = int((random.random() * 20) + 1980)
        birth_month = int(random.random() * 12 + 1)
        birth_day = int((random.random() * 31))
        builder = []
        builder.append(str(birth_year))
        if birth_month < 10:
            builder.append("0")
        builder.append(str(birth_month))
        if birth_day < 10:
            builder.append("0")
        builder.append(str(birth_day))
        builder = ''.join(str(i) for i in builder)
        self.generater.append(builder)
        #随机码
        code1 = int(random.random()*1000)
        if code1 < 10:
            self.randomCode = "00" + str(code1)
        elif code1 < 100:
            self.randomCode = "0" + str(code1)
        else:
            self.randomCode = str(code1)
        self.generater.append(self.randomCode)
        temp = "".join(str(i) for i in self.generater)
        #验证码
        c = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        r = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        #将generater 的前17为进行字节化

        for k in range(17):
            self.result += c[k] * int(temp[k])
        validateCode = r[self.result%11]
        self.generater.append(validateCode)
        self.generater = "".join(str(i) for i in self.generater)
        self.readConfig.setReslConfig("IdNum",self.generater)
    def createName(self):
        xingming = []
        index_xing = int(random.random()*len(xing))
        len_xingming = random.choice([1,2])
        xingming.append(xing[index_xing])
        for i in range(len_xingming):
            index_ming = int(random.random() * len(ming))
            xingming.append(ming[index_ming])
        realName = "".join(xingming)
        self.readConfig.setReslConfig("realName",realName)
    def createIdNumAndName(self):
        self.createIdNum()
        self.createName()
if __name__ == "__main__":
    ss = CreateIdAndRealName()
    ss.createIdNumAndName()