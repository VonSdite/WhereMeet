# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

# 获取腾讯控股 (00700) 今日开盘价

import requests
import re

def getOpenPrice():
    # 股价的url
    url = "https://gupiao.baidu.com/stock/hk00700.html?from=aladingpc"
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
        image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Host': 'gupiao.baidu.com',
        'Referer': 'https://www.baidu.com/link?url=mJfAzXrA_JeZWXhNVwncnBE9zBHbkjdJj\
        -swnK1vZF2KAzdIt93gEfWAFmDjzCjicdjFh6aIzSBFccB2R9HwRO4wjfWbSiHabujk6Huf2c_&wd=&eqid\
        =af9ac96a0001632f0000000659d5bb04',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,\
         like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    # 爬取页面内容
    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'      # 编码为utf-8
    text = res.text

    # # 用于查看爬下来的HTML内容
    # with open("save.txt", 'w', encoding='utf-8') as f:
    #     f.write(res.text)

    # 正则表达式获取开盘价
    pattern_price = re.compile(r'<dl><dt>今开</dt><dd class="s-up">(.*?)</dd></dl>')
    pattern_date =  re.compile(r'\d{4}-\d{2}-\d{2}')
    openPrice = pattern_price.findall(text)[0]    # 开盘价
    date = pattern_date.findall(text)[0]          # 日期
    return '-'.join((date, openPrice))

if __name__ == '__main__':
    print(getOpenPrice())
