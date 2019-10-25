#coding:utf-8
import unittest
import requests
from cases.x1_zentao_login import login_zentao,is_login_success

class Test_Login(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def test_01(self):
        res = login_zentao('admin', 'YT123456')
        Login_result = is_login_success(res)
        print(Login_result)  #实际结果
        self.assertTrue(Login_result) #期望结果     断言就是实际结果跟期望结果作对比

    def test_02(self):
        res = login_zentao('admin11', 'YT123456')
        Login_result = is_login_success(res)
        print(Login_result)
        self.assertFalse(Login_result)
if __name__ == '__main__':
    unittest.main()











