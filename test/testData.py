import sys
sys.path.append('../')
from make_map import *
import matplotlib.pyplot as plt
import numpy as np

def creatZhiFangTu(appearTimes, index, fenGe):
    i = np.arange(len(appearTimes))
    bar_width = 0.35
    rects1 = plt.bar(i, appearTimes, bar_width, color='#0072BC', label='柱状图')
    plt.xticks(i + bar_width, index)
    plt.ylim(ymax=100, ymin=0)
    plt.axhline(fenGe, xmin=0, xmax=10,hold=None,label="1",color='red',linestyle="-")
    plt.show()


if __name__ == '__main__':
    string = '2017-10-08-%.2f'
    num = 300.01

    cnt = 0
    z = []
    while num <= 400.0:
        s = string % num
        md = makeMd5(s)
        a, b = splitMd5(md)
        # a, b = addNumber(a, 0)%19+1, addNumber(b, 0)%8+1
        a, b = addNumber(a)%19+1, addNumber(b)%8+1
        z.append((a,b))
        num += 0.01
        cnt += 1

    print('共计: %d次' % cnt)
    index = []
    appearTimes = []
    diff = []
    for row in range(1, 19):
        for col in range(1, 8):
            count = z.count((row, col))
            index.append((row, col))
            diff.append(abs(count-cnt/162))
            appearTimes.append(count)
      
    creatZhiFangTu(appearTimes, index, cnt/162)      
    creatZhiFangTu(diff, index, 10)                 # 与基线的差值的绝对值直方图
