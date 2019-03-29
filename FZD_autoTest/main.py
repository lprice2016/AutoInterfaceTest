#/usr/bin/env python3
#-*- coding:utf-8 -*-


import os
#
# import time
# from HTMLTestRunner import HTMLTestRunner
#
# from TestCase import testImg
#
# from Common import Log

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))


#
# if __name__ == "__main__":
#
#     log = Log.MyLog.get_log()
#     logger = log.getLogger()
#     #构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(testBaiDu.MyTest("test_case1"))#加入测试用例
#     suite.addTest(testBaiDu.MyTest("test_case2"))#加入测试用例
#     #执行测试
#     date = time.strftime("%Y%m%d") #定义date为日期，time 为时间
#     time = time.strftime("%Y-%m-%d %H:%M:%S")
#     path = './AutoTestReport/'
#     if not os.path.exists(path):
#         os.makedirs(path)
#     else:
#         pass
#     report_path = path + time + ".html"
#     report_title = u"测试报告"
#     desc = u"接口自动化测试报告详情"
#     with open(report_path,'wb') as report:
#         runner = HTMLTestRunner(stream=report,title=report_title,description=desc)
#         runner.run(suite)
#     report.close()
#
#     # for i ,j in zip([1,2,3,4],[5,6,7,8]):
    #     print(i,j)

if __name__ == "__main__":
    print("test")