import wx
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def getRP():
    # 获取屏幕分辨率
    app = wx.App()
    mm = wx.DisplaySize()
    del app
    return mm[0], mm[1]

w, h = getRP()

if (w, h) == (1920, 1080):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (560, 40)        # 时间Label的位置
    PRICELABELPOS = (560, 100)       # 开盘价的位置
    RESULTLABELPOS = (530, 160)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (620, 750)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (740, 750)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (940, 840)     # 窗口大小，背景图片大小
    TABLESIZE = (70, 60)            # 桌子的大小
    COLINTERVAL = 80                # 桌子间列的间隔
    ROWINTERVAL = 40                # 桌子间行的间隔
    ROWSTART = 30                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1680, 1050):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (560, 40)        # 时间Label的位置
    PRICELABELPOS = (560, 100)       # 开盘价的位置
    RESULTLABELPOS = (530, 160)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (620, 750)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (740, 750)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (940, 840)     # 窗口大小，背景图片大小
    TABLESIZE = (70, 60)            # 桌子的大小
    COLINTERVAL = 80                # 桌子间列的间隔
    ROWINTERVAL = 40                # 桌子间行的间隔
    ROWSTART = 30                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1600, 900):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (560, 40)        # 时间Label的位置
    PRICELABELPOS = (560, 100)       # 开盘价的位置
    RESULTLABELPOS = (530, 160)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (620, 750)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (740, 750)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (940, 840)     # 窗口大小，背景图片大小
    TABLESIZE = (70, 60)            # 桌子的大小
    COLINTERVAL = 80                # 桌子间列的间隔
    ROWINTERVAL = 40                # 桌子间行的间隔
    ROWSTART = 30                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置


elif (w, h) == (1440, 900):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (560, 40)        # 时间Label的位置
    PRICELABELPOS = (560, 100)       # 开盘价的位置
    RESULTLABELPOS = (530, 160)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (620, 750)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (740, 750)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (940, 840)     # 窗口大小，背景图片大小
    TABLESIZE = (70, 60)            # 桌子的大小
    COLINTERVAL = 80                # 桌子间列的间隔
    ROWINTERVAL = 40                # 桌子间行的间隔
    ROWSTART = 30                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置


elif (w, h) == (1400, 1050):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (560, 40)        # 时间Label的位置
    PRICELABELPOS = (560, 100)       # 开盘价的位置
    RESULTLABELPOS = (530, 160)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (620, 750)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (740, 750)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (940, 840)     # 窗口大小，背景图片大小
    TABLESIZE = (70, 60)            # 桌子的大小
    COLINTERVAL = 80                # 桌子间列的间隔
    ROWINTERVAL = 40                # 桌子间行的间隔
    ROWSTART = 30                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1366, 768):
    TEXTSIZE = 14                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 8             # 按钮文字大小
    BUTTONICONSIZE = QSize(33, 33)  # 按钮图标大小        
    BUTTONPOS = (500, 500)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (620, 500)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (820, 610)     # 窗口大小，背景图片大小
    TABLESIZE = (50, 40)            # 桌子的大小
    COLINTERVAL = 50                # 桌子间列的间隔
    ROWINTERVAL = 30                # 桌子间行的间隔
    ROWSTART = 13                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1360, 768):
    TEXTSIZE = 14                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 8             # 按钮文字大小
    BUTTONICONSIZE = QSize(33, 33)  # 按钮图标大小        
    BUTTONPOS = (500, 500)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (620, 500)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (820, 610)     # 窗口大小，背景图片大小
    TABLESIZE = (50, 40)            # 桌子的大小
    COLINTERVAL = 50                # 桌子间列的间隔
    ROWINTERVAL = 30                # 桌子间行的间隔
    ROWSTART = 13                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1280, 1024):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (500, 600)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 600)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (850, 710)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 60                # 桌子间列的间隔
    ROWINTERVAL = 35                # 桌子间行的间隔
    ROWSTART = 13                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1280, 960):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (500, 600)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 600)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (850, 710)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 60                # 桌子间列的间隔
    ROWINTERVAL = 35                # 桌子间行的间隔
    ROWSTART = 13                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1280, 800):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (500, 600)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 600)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (850, 710)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 60                # 桌子间列的间隔
    ROWINTERVAL = 35                # 桌子间行的间隔
    ROWSTART = 13                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1280, 768):
    TEXTSIZE = 16                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(30, 30)  # 按钮图标大小        
    BUTTONPOS = (500, 560)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 560)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (850, 630)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 55                # 桌子间列的间隔
    ROWINTERVAL = 32                # 桌子间行的间隔
    ROWSTART = 5                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1280, 720):
    TEXTSIZE = 16                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(30, 30)  # 按钮图标大小        
    BUTTONPOS = (500, 560)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 560)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (850, 630)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 55                # 桌子间列的间隔
    ROWINTERVAL = 32                # 桌子间行的间隔
    ROWSTART = 5                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1280, 600):
    TEXTSIZE = 10                   # 文字大小
    DATELABELPOS = (400, 30)        # 时间Label的位置
    PRICELABELPOS = (400, 80)       # 开盘价的位置
    RESULTLABELPOS = (400, 130)     # 结果的位置
    BUTTONTEXTSIZE = 8             # 按钮文字大小
    BUTTONICONSIZE = QSize(20, 15)  # 按钮图标大小        
    BUTTONPOS = (400, 430)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (520, 430)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (650, 500)     # 窗口大小，背景图片大小
    TABLESIZE = (45, 35)            # 桌子的大小
    COLINTERVAL = 45                # 桌子间列的间隔
    ROWINTERVAL = 25                # 桌子间行的间隔
    ROWSTART = 8                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1152, 864):
    TEXTSIZE = 18                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(35, 35)  # 按钮图标大小        
    BUTTONPOS = (500, 600)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 600)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (850, 710)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 60                # 桌子间列的间隔
    ROWINTERVAL = 35                # 桌子间行的间隔
    ROWSTART = 8                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (1024, 768):
    TEXTSIZE = 16                   # 文字大小
    DATELABELPOS = (460, 30)        # 时间Label的位置
    PRICELABELPOS = (460, 80)       # 开盘价的位置
    RESULTLABELPOS = (460, 130)     # 结果的位置
    BUTTONTEXTSIZE = 10             # 按钮文字大小
    BUTTONICONSIZE = QSize(30, 30)  # 按钮图标大小        
    BUTTONPOS = (500, 560)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (630, 560)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (800, 630)     # 窗口大小，背景图片大小
    TABLESIZE = (60, 50)            # 桌子的大小
    COLINTERVAL = 55                # 桌子间列的间隔
    ROWINTERVAL = 30                # 桌子间行的间隔
    ROWSTART = 8                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

elif (w, h) == (800, 600):
    TEXTSIZE = 10                   # 文字大小
    DATELABELPOS = (400, 30)        # 时间Label的位置
    PRICELABELPOS = (400, 80)       # 开盘价的位置
    RESULTLABELPOS = (400, 130)     # 结果的位置
    BUTTONTEXTSIZE = 8             # 按钮文字大小
    BUTTONICONSIZE = QSize(20, 15)  # 按钮图标大小        
    BUTTONPOS = (400, 430)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (500, 430)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (650, 500)     # 窗口大小，背景图片大小
    TABLESIZE = (45, 35)            # 桌子的大小
    COLINTERVAL = 45                # 桌子间列的间隔
    ROWINTERVAL = 25                # 桌子间行的间隔
    ROWSTART = 8                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置

else:
    TEXTSIZE = 10                   # 文字大小
    DATELABELPOS = (400, 30)        # 时间Label的位置
    PRICELABELPOS = (400, 80)       # 开盘价的位置
    RESULTLABELPOS = (400, 130)     # 结果的位置
    BUTTONTEXTSIZE = 8             # 按钮文字大小
    BUTTONICONSIZE = QSize(20, 15)  # 按钮图标大小        
    BUTTONPOS = (400, 430)          # '点我'按钮的起始位置
    SENDBUTTONPOS = (500, 430)      # 发送信息按钮的起始位置
    BACKGROUNDSIZE = (650, 500)     # 窗口大小，背景图片大小
    TABLESIZE = (45, 35)            # 桌子的大小
    COLINTERVAL = 45                # 桌子间列的间隔
    ROWINTERVAL = 25                # 桌子间行的间隔
    ROWSTART = 8                   # 桌子的起始行位置
    COLSTART = 10                   # 桌子的起始列位置