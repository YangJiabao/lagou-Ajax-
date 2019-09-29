import random
import time
import json
import requests
from openpyxl import Workbook


def get_json(url, page, lang_name):
    url1 = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
    headers = {
        #'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        #'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        #'Accept-Encoding': 'gzip, deflate, br',
        #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'X-Anit-Forge-Token': 'None',
        #'X-Anit-Forge-Code': '0',
        #'X-Requested-With': 'XMLHttpRequest',
        #'Content-Length': '25',
        #'Connection': 'keep-alive',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    }
    data = {'first': 'true', 'pn': page, 'kd': lang_name}
    #print(url)
    s = requests.Session()
    s.get(url1, headers=headers, timeout=3)# 请求首页获取cookies
    cookie = s.cookies# 为此次获取的cookies
    response = s.post(url, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
    time.sleep(5)
    response.encoding = response.apparent_encoding
    text = json.loads(response.text)
    info = text["content"]["positionResult"]["result"]
    #json = requests.post(url, data, headers=headers)#.json()
    #print(json.text)
    #response = json.json()
    #response = ['content']['positionResult']['result']:
    info_list = []
    for i in info:
        info = []
        info.append(i.get('positionName', '无'))
        info.append(i.get('workYear', '无'))
        info.append(i.get('education', '无'))
        info.append(i.get('createTime', '无'))
        info.append(i.get('city', '无'))
        info.append(i.get('positionAdvantage', '无'))
        info.append(i.get('salary', '无'))
        info.append(i.get('companySize', '无'))
        info.append(i.get('district', '无'))
        info.append(i.get('companyFullName', '无'))  # 改过了
        info_list.append(info)
    #list_con = json['content']['positionResult']['result']
    return info_list


def main():
    lang_name = 'python'
    wb = Workbook()  # 打开 excel 工作簿
    for i in ['合肥','上海','南京']:   # 五个城市
        page = 1
        ws1 = wb.active
        ws1.title = lang_name
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(i)
        #url = 'https://www.lagou.com/jobs/list_python/p-city_79?px=default#filterBox'
        while page < 20:   # 每个城市20页信息
            info = get_json(url, page, lang_name)
            page += 1
            print( 'page：', page)
            time.sleep(random.randint(10, 20))
            for row in info:
                ws1.append(row)
    wb.save('{}职位信息.xlsx'.format(lang_name))

if __name__ == '__main__':
    main()
