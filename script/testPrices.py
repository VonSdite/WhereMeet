
# 这一个测试块是为了找到比较好的偏移量使得
# 根据开盘价日期+开盘价生成的md5的值配合数位求和得出来的行列分布更加的均匀
# 然而可能只是玄学吧

import sys
sys.path.append('../')

from make_map import *
from stock_price import *
import requests
import json
import matplotlib.pyplot as plt

# 爬取多天开盘价来观察 分布是否均匀
def testPrice():
    # 股票的json数据源
    url = 'https://gupiao.baidu.com/api/stocks/stockdaybar?from=pc&os_ver=1&cuid=xxx&vv=100\
    &format=json&stock_code=hk00700&step=3&start=&count=160&fq_type=no&timestamp=1507184689016'

    res = requests.get(url=url)
    data = json.loads(res.text)     # 解析json数据
    prices = []
    # print(data)
    for e in data['mashData']:
        tmp = str(e['date'])
        date = tmp[:4]+'-'+tmp[4:6]+'-'+tmp[6:]+'-'
        prices.append('%s%.2f' % (date, e['kline']['open']))  # 保留两位小数的获取开盘价
    return prices       # 返回一堆开盘价

# 数字中所有数位相加, deviation是偏移量
def addNumber(num, deviation=0):
    num = str(num+deviation)
    res = 0
    for e in num:
        res += ord(e)-ord('0')
    return res

# 寻找合适的偏移量使得分布均匀
def findNiceDeviation(prices, begin=1, end=10000):
    # 寻找一个偏移值使得它们点数分布更均匀
    # 在1到100000中偏移量为27666使得分布更加均匀一点
    MAX = 0
    DEVIATION = 0
    for test in range(begin, end+1):
        cnt = 0
        vis = []
        for price in prices:
            # print(price)
            md = makeMd5(str(price))  # 获取生成的md5值
            mdHeight, mdLow = md[:int(len(md) / 2)], md[int(len(md) / 2):]  # 将生成的md5值分成两部分
            mdHeight, mdLow = int('0x' + mdHeight, 16), int('0x' + mdLow, 16)  # 将16进制转10进制
            mdHeight, mdLow = addNumber(mdHeight, test) % 19 + 1, addNumber(
                mdLow, test) % 8 + 1  # 所有数位求和

            if vis.count((mdHeight, mdLow)) == 0:
                # 计数有多少个点
                cnt += 1
                vis.append((mdHeight, mdLow))
        if cnt > MAX:
            MAX = cnt
            DEVIATION = test
        # print(str(test)+' 共有%d个坐标，图中有%d个点,重合的点有%d个，重合率%.2f%%' % \
        #                                               (len(prices), \
        #                                                cnt, \
        #                                                len(prices)-cnt, \
        #                                                (len(prices)-cnt)/len(prices)*100))
    print(MAX, DEVIATION)
    return DEVIATION

# 显示散点图, 传入的是开盘价列表
def showRO(prices, deviation=0):
    x = []
    y = []
    cnt = 0
    vis = []
    for price in prices:
        # print(price)
        md = makeMd5(str(price))  # 获取生成的md5值
        mdHeight, mdLow = md[:int(len(md) / 2)], md[int(len(md) / 2):]  # 将生成的md5值分成两部分
        mdHeight, mdLow = int('0x' + mdHeight, 16), int('0x' + mdLow, 16)  # 将16进制转10进制
        mdHeight, mdLow = addNumber(mdHeight, deviation) % 19 + 1, addNumber(mdLow, deviation)\
                          % 8 + 1  # 所有数位求和

        y.append(mdHeight)
        x.append(mdLow)

        if vis.count((mdHeight, mdLow)) == 0:
            # 计数有多少个点
            cnt += 1
            vis.append((mdHeight, mdLow))
    print('共有%d个坐标，图中有%d个点,重合的点有%d个，重合率%.2f%%' % (
    len(prices), cnt, len(prices) - cnt, (len(prices) - cnt) / len(prices) * 100))
    ax = plt.figure(figsize=(4, 4)).add_subplot(111)
    ax.set_xticks(range(10))
    ax.set_yticks(range(20))
    plt.plot(x, y, 'ro')
    plt.show()

if __name__ == '__main__':
    prices = testPrice()    # 获取一堆开盘价
    # print(prices)

    # findNiceDeviation(prices, 1, 100000)
    showRO(prices, 0)       # 显示散点图

