# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import requests

class DailyReport(object):
    '''每日打卡相关操作'''

    def __init__(self, session):
        self.session = session
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/85.0.4183.102 Safari/537.36',
            'Connection': 'keep-alive',
        }

        self.home_url = 'https://weixine.ustc.edu.cn/2020/home'                                    # 首页 URL
        self.daliy_report_url = 'https://weixine.ustc.edu.cn/2020/daliy_report'                    # 登录 URL

    @property
    def token(self):
        home = self.session.get(self.home_url, headers=self.header).text
        soup = BeautifulSoup(home, 'html.parser')
        token = soup.find('input', {'name':'_token'})['value']
        if token == None:
            raise RuntimeError('未找到token，请检查是否登录成功！')
        return token

    def post_report(self, report:dict):
        self.form_data = report
        self.form_data['_token'] = self.token

        r = self.session.post(self.daliy_report_url, data=self.form_data, headers=self.header, allow_redirects=False)
        
        status_code = r.status_code                                                                # 其实这个判断条件不对, 懒得改了
        if status_code == 302:
            print(f'疫情每日上报提交成功')
        else:
            print(f'疫情每日上报提交失败')


def main():
    '''一些没啥用的测试代码
    '''
    s = requests.session()
    s.trust_env = False                                                                            # 解决代理造成的 requests.exceptions.ProxyError
    pass

if __name__  == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n操作已取消')
        exit(0)