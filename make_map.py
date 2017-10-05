# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

# 实现生成md5，映射饭堂座位的功能

import hashlib
from stock_price import getOpenPrice

# 制作md5值
def makeMd5(string):
    string = string.encode('utf-8')
    md = hashlib.md5()
    md.update(string)
    return md.hexdigest()

# 分割md5值，将md5值分成两半，并返回两部分的十进制值
def splitMd5(md):
    mdHeight, mdLow = md[:int(len(md) / 2)], md[int(len(md) / 2):]  # 将生成的md5值分成两部分
    mdHeight, mdLow = int('0x' + mdHeight, 16), int('0x' + mdLow, 16)  # 将16进制转10进制
    return mdHeight, mdLow

# 数字中所有数位相加, deviation是偏移量
# 偏移量是为了使得分布更加均匀
# emmm，这个偏移量实际上应该是有玄学因素影响的
# 通过160组数据,然后在0到100000的区间内找到这个27666的偏移量可能仅仅比较适合这160天的数据
def addNumber(num, deviation=27666):
    num = str(num+deviation)
    res = 0
    for e in num:
        res += ord(e)-ord('0')
    return res

# 映射的结果的行和列返回
def resRowCol(openPrice):
    md = makeMd5(openPrice)  # 获取生成的md5值
    mdHeight, mdLow = splitMd5(md)  # 分别获取高位md5值和低位md5值
    row = addNumber(mdHeight)  # 将高位md5值所有数位相加和作为行
    col = addNumber(mdLow)  # 将低位md5值所有数位相加和作为列
    return row, col

if __name__ == '__main__':
    row, col = resRowCol()
    print(row, col)