#coding:utf-8
import requests
import json
import unittest

class TestQQ(unittest.TestCase):


     def setUp(self):
         # 测试数据准备
        self.url = "http://japi.juhe.cn/qqevaluate/qq"
        self.s = requests.session()


     def test_01(self):
        #测试QQ接口：key是错误的  qq是正确的   期望结果："KEY ERROR!"

        par = {
            "key": "8dbee1fcd8627fb6699bce7b986abc45",
            "qq": "3256814316"

        }
        r = self.s.get(self.url, params=par)
        #print(r.text)
        # 获取结果
        res = r.json()['reason']  # 返回的是字典，用r.json解析成字典
        print('实际结果：%s' % res)
        # 期望结果  返回结果里面  "KEY ERROR!"
        #assert res == "KEY ERROR!"
        self.assertTrue(res == "KEY ERROR11!")

        def tearDown(self):

            self.s.close()


     def test_02(self):
         #url = "http://japi.juhe.cn/qqevaluate/qq"
         par = {
             "key": "8dbee1fcd8627fb6699bce7b986abc45",
             "qq": ""

         }
         r = self.s.get(self.url, params=par)
         print(r.text)
         # 获取结果
         res = r.json()['reason']  # 返回的是字典，用r.json解析成字典
         print('实际结果：%s' % res)
         # 期望结果  返回结果里面  "KEY ERROR!"
         # assert res == "KEY ERROR!"
         self.assertTrue(res == "KEY ERROR!")


if __name__ =="__main__":
    unittest.main()






#字典取某个字段
'''reason = res['reason']
print(reason)
'''
