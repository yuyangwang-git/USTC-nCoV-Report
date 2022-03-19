# USTC-nCoV-Report
中国科学技术大学健康打卡平台 (<https://weixine.ustc.edu.cn/2020/login>) 每日信息自动上报, 本项目可以同时为多个人实现定时打卡功能, 只需将每个人的信息填入 `report.ini` 文件即可.

2022年3月19日 修改report.ini以适应上报内容变化
2021年9月13日 第一版

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [示例](#示例)
- [使用许可](#使用许可)

## 背景

每天打卡太麻烦了, 容易忘~~吃饱了撑的~~, 决定写一个脚本挂服务器上.

## 安装

本项目需要Python 3.7或更高版本, 低版本未作测试.

安装 requests 库:

```sh
$ python3 -m pip install requests
```

安装 BeautifulSoup 库:

```sh
$ python3 -m pip install beautifulsoup4
```

## 使用说明

在目录下的 `report.ini` 文件夹下填入一个或多个人的信息, 然后执行:

```sh
$ python3 main.py
```

即可完成一次批量上报, 可以挂在服务器上使用 crontab 完成每日定时打卡, 如在每天早晨七点定时打卡:

```txt
0 7 * * * python3 /home/yourname/task/main.py
```

## 示例

这是一份 `report.ini` 文件示例, 包含两个人的信息(一个 section 对应一个人):

```ini
# 说明:
# 所有留空的选项, 不需要, 也不应填写
# 在此文件中增加若干 section, 可为多个人实现自动化打卡操作

# 修改记录:
# 2022年3月19日 增加 “现居地” 选项

[Tom]

# 用户名及学号
username = SA210000000
password = 1234567

_token = 

# 现居地
# 该项直接填写中文字符串即可，如：
# 东校区
# 西校区
# 南校区
# 北校区
# 中校区
# 高新校区
# 先研院
# 国金院
# 合肥市内校外
# 合肥市外校区
juzhudi = 西校区

# 当前身体状况
# 1 正常
# 2 疑似
# 3 确诊
# 4 其它
body_condition = 1
body_condition_detail = 

# 当前状态
# 1 正常在校园内
# 2 正常在家
# 3 居家留观     
# 4 集中留观
# 5 住院治疗
# 6 其它
now_status = 1
now_status_detail = 

# 目前有无发热症状
# 0 无
# 1 有
has_fever = 0

# 是否接触过确诊或疑似病例的患者
# 0 无
# 1 有
last_touch_sars = 0
last_touch_sars_date = 
last_touch_sars_detail = 

# 当前居住地是否为疫情中高风险地区
# 0 否
# 1 是
is_danger = 0

# 14天内是否有疫情中高风险地区旅居史
# 0 无
# 1 有
is_goto_danger = 0

# 紧急联系人
jinji_lxr = Jack

# 紧急联系人与本人关系
jinji_guanxi = 父亲

# 紧急联系人电话
# jiji 不是我写错，实际 post 的数据就是这样
jiji_mobile = 13500000000

# 其它情况说明
other_detail = 无

[Jack]
# 第二个人

username = SA210000001
password = 1234567

_token = 

juzhudi = 西校区
body_condition = 1
body_condition_detail = 
now_status = 1
now_status_detail = 
has_fever = 0
last_touch_sars = 0
last_touch_sars_date = 
last_touch_sars_detail = 
is_danger = 0
is_goto_danger = 0
jinji_lxr = Tom
jinji_guanxi = 儿子
jiji_mobile = 13500000001
other_detail = 无
```

## 使用许可

[MIT License](LICENSE)
