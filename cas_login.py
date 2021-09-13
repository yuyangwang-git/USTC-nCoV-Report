# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import requests

class CAS(object):
    '''CAS (passport.ustc.edu.cn) 登录相关操作'''

    def __init__(self, session, student):
        self.session = session
        self.student = student
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/85.0.4183.102 Safari/537.36',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br', 
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8'
        }
        self.login_url = 'https://passport.ustc.edu.cn/login'                                      # 登录 URL
        self.service_url = 'https://weixine.ustc.edu.cn/2020/caslogin'
        self._verification_code_url = 'https://passport.ustc.edu.cn/validatecode.jsp?type=login'

    @property
    def CAS_LT(self):
        r = self.session.get(self.login_url, params = {'service': self.service_url}).text          # 猜测是对某个字符串做 md5 得到的新字符串, 以后找时间验证一下
        soup = BeautifulSoup(r, 'html.parser')
        return soup.find('input', {'name':'CAS_LT'})['value']

    def login(self):
        self._need_verification_code = False

        if self._need_verification_code is True:                                                   # 留给以后增加验证码识别功能用
            pass
        else:
            form_data = {
                'model': 'uplogin.jsp',
                'CAS_LT': self.CAS_LT,
                'service': self.service_url,
                'warn': '',
                'showCode': '',
                'username': self.student.username,
                'password': self.student.password,
                'button': '',
            }
        r = self.session.post(self.login_url, data=form_data, headers=self.header, allow_redirects = False)
        
        status_code = r.status_code
        if status_code == 302:
            print(f'用户 {self.student.username} 登录成功')
            url = r.headers['location']
            print(f'即将跳转地址: {url}')
            self.session.get(url)
            return url
        else:
            print(f'用户 {self.student.username} 登录失败')
            return None

    # 似乎和合工大的系统一样蠢, 可以直接绕开验证码, 先把这部分删了
    # def get_login_info(self):
    #     r = self.session.get(self.login_url, params = {'service': self.service_url}).text
    #     soup = BeautifulSoup(r, 'html.parser')
    #     self._CAS_LT = soup.find('input', {'name':'CAS_LT'})['value']
    #     self._need_verification_code = soup.find('input', {'name':'showCode'})['value']

    # def get_verification_code(self):
    #     form_data = {
    #         'type': 'login'
    #     }
    #     r = self.session.get(self._verification_code_url, data=form_data, headers=self.header)
    #     with open('verification_code.jpeg', 'wb') as f:
    #         f.write(r.content)        

    # def get_verification_code_result(self):
    #     self._verification_code = input("请输入验证码: ")

def main():
    '''一些没啥用的测试代码
    '''
    Student = type('Student', (object,), dict())
    
    student = Student()
    student.username = ''
    student.password = ''

    session = requests.session()
    session.trust_env = False

    cas = CAS(session, student)
    redirect_url = cas.login()
    print(redirect_url)

if __name__  == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n操作已取消')
        exit(0)