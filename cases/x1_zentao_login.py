#coding:utf-8
import requests

def login_zentao(user,psw):   #登录禅道功能
    s = requests.session()
    url = 'http://127.0.0.1:82/zentao/user-login-L3plbnRhby9teS5odG1s.html'

    body = {
        'account':user,  #用参数去代替  加了字符串就写死了
        'password':psw,
        'referer': '/zentao/my.html'
    }

    r = s.post(url, data=body)
    return r.content.decode('utf-8')
def is_login_success(result):
    if 'parent.location' in result:
       return True
    else:
      return False

if __name__ == '__main__':    #  if 下面代码是自己测试 测试函数功能用的
    res = login_zentao('admin','YT123456')
    Login_result = is_login_success(res)
    print(Login_result)





    '''if 'parent.location' in res:
        print('登录成功')
    else:
        print('登录失败')'''









