#coding:utf-8
from common.HTMLreport import HTMLTestRunner
import unittest
import os

#查找的目录
curpash =os.path.dirname(os.path.realpath(__file__))
print(curpash)

startdir = os.path.join(curpash,'cases')
print(startdir)

discover = unittest.defaultTestLoader.discover(startdir,
                                               pattern='test*.py')

print(discover)
reportpath = os.path.join(curpash,'report','result.html')
print(reportpath)

fp = open(reportpath,'wb')

#生成报告
runner = HTMLTestRunner(stream=fp,
                     title="测试报告的标题",
                     description='测试用例的描述')
runner.run(discover)

fp.close()




