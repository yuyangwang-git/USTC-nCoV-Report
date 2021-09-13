# -*- coding: utf-8 -*-

import time
import random
import requests
import configparser
from multiprocessing.dummy import Pool
from cas_login import CAS
from daily_report import DailyReport

class Student(object):

    def __init__(self, config:dict) -> None:
        self.config = config
        self.username = self.config.pop('username')
        self.password = self.config.pop('password')
        
        if self.config['now_city'] != '340100':                                                    # 如在合肥, 需额外提交校区信息，详见前端 frontend.js 文件
            self.config.pop('is_inschool')
        self.report = self.config

def post_report(student):
    time.sleep(random.uniform(0, 120))

    session = requests.session()
    session.trust_env = False

    # login in CAS System
    cas = CAS(session, student)
    cas.login()

    # post daily report
    report = DailyReport(session)
    report.post_report(student.report)

def main():
    config = configparser.ConfigParser()
    config.read('report.ini', encoding='utf-8')
    
    students = []                                                                                  # 可以根据配置文件同时为多人填写疫情打卡
    for section in config.sections():
        print(f'正在读取 {section} 的个人信息')
        student = dict(config[section])
        students.append(Student(student))

    pool = Pool(processes=len(students))
    pool.map(post_report, students)
    pool.close()
    pool.join()

if __name__  == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n操作已取消')
        exit(0)
