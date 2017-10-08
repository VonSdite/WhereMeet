import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore

from make_map import resRowCol
from stock_price import getOpenPrice
import itchat, sys, os
import threading

class Signal(QObject):
    # 信号
    e = pyqtSignal()

class Ui(QWidget):
    """docstring for Quit"""

    def __init__(self, configFile='config.txt'):
        super(Ui, self).__init__()

        self.wechatTarget = 'Anti Cpp Cpp Club'         # 微信发送信息的目标
        self.configFile = configFile                    # Ui的配置文件，配置桌子
        self.openPrice = getOpenPrice(self)             # 开盘价
        self.row, self.col = resRowCol(self.openPrice)  # 目标结果行和列

        self.textSize = 15      # 文字大小
        self.initUI()

        # 微信发送信息线程
        self.wechatThreading = threading.Thread(target=self.wechatSendMessage)  
        self.wechatThreading.setDaemon(True)

        # 信号-槽
        self.networkErrorCatch = Signal()       # 微信网络异常信号
        self.networkErrorCatch.e.connect(self.networkError)
        self.notFindErrorCatch = Signal()       # 微信群组查找不到异常
        self.notFindErrorCatch.e.connect(self.notFindError)

        # 是否已经点了生成座位的button
        # 点了的话，就不重新运行，避免创建多余的线程
        self.isClicked = False

    def initUI(self):
        # 设置背景图片
        palette = QtGui.QPalette()
        # palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/bk.jpg')))
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QColor(0,0,0)))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        dateLabel = QLabel(self)
        dateLabel.setText('<font color=white><b>最新 %s</b></font>' %\
                     '-'.join(self.openPrice.split('-')[:-1]))
        dateLabel.setFont(QFont('宋体', self.textSize))
        dateLabel.move(560, 30)

        priceLabel = QLabel(self)
        priceLabel.setText('<font color=white><b>股票开盘价%s元</b></font>' \
                           % self.openPrice.split('-')[-1])
        priceLabel.setFont(QFont('宋体', self.textSize))
        priceLabel.move(560, 80)


        self.resTable = None            # 目标位置对象
        self.resTableColor = None       # 目标位置桌子颜色
        # 根据桌子配置文件来配置桌子
        with open(self.configFile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.row %= len(lines)

            cnt_row = 0         # 计数到第几行
            row = 40            # 放置的起始行的位置
            for line in lines:
                col = 10  # 放置的起始列的位置
                ########################################
                # 这块代码是用于self.col
                cnt_row += 1
                if cnt_row == self.row:
                    # 目标行因为是固定行数，所以开始就可以对行数取余
                    # 而列数不固定要先找到那一行确定列数才能取余
                    cnt = 0
                    for e in line:
                        # 计数有多少个桌子
                        # 因为可能配置文件桌子之间可以隔多个空格
                        # 所以采用遍历
                        if e != ' ' and e != '\n':
                            cnt += 1
                    self.col %= cnt
                ########################################
                cnt_col = 0
                for e in line:
                    if e == ' ':
                        col += 80   # 遇到空格就要空开一定的间隔
                        continue
                    if e == '\n':
                        break
                    cnt_col += 1
                    d = QLabel(self)
                    d.resize(60, 40)
                    pixMap = QPixmap('img/%s.png' % e).scaled(d.width(), d.height())
                    d.move(col, row)
                    d.setPixmap(pixMap)

                    if cnt_row == self.row and cnt_col == self.col:
                        self.resTable = d
                        self.resTableColor = e

                row += 40       # 下一行放置的位置

        btn = QPushButton('点我', self)
        btn.setIcon(QIcon(r'img\button.gif'))
        btn.resize(btn.sizeHint())
        btn.move(600, 690)
        btn.clicked.connect(self.buttonClicked)

        self.setWindowTitle('WhereMeet?')
        self.setWindowIcon(QIcon('img\gathering.jpg'))
        self.resize(950, 830)
        self.center()
        # self.setFixedSize(self.width(), self.height())  # 禁止改变窗口大小
        self.show()

    def signalShow(self):
        # 选中的桌子的显示
        # 通过showBoolean来设置显示什么图片
        if self.showBoolean:
            self.resTable.setPixmap(QPixmap(None))
            self.showBoolean = False
        else:
            pixMap = QPixmap('img/%s.png' % self.resTableColor).scaled(\
                self.resTable.width(), self.resTable.height())
            self.resTable.setPixmap(pixMap)
            self.showBoolean = True

    def showPic(self):
        # 显示选中桌子闪烁的计时器线程
        self.showPicSignal.e.emit()
        self.timer = threading.Timer(0.5, self.showPic)
        self.timer.start()


    def buttonClicked(self):
        if not self.isClicked:
            # 避免创建多余的线程
            self.isClicked = True

            # 通过线程timer来实现桌子闪烁
            # 使用QMoive的话，图片会带有锯齿，所以放弃使用该方法，转而使用线程计时器
            self.showPicSignal = Signal()
            self.showBoolean = True
            self.showPicSignal.e.connect(self.signalShow)
            self.timer = threading.Timer(0.5, self.showPic)
            self.timer.start()

            targetLabel = QLabel(self)
            targetLabel.setText('<font color=white>聚会位置：第<b>%d</b>行 第<b>%d</b>列</font>'\
                               % (self.row, self.col))
            targetLabel.setFont(QFont('宋体', self.textSize))
            targetLabel.move(530, 130)
            targetLabel.show()

            sendButton = QPushButton('发送到微信', self)

            sendButton.setIcon(QIcon(r'img\wechat.jpg'))
            sendButton.resize(sendButton.sizeHint())
            sendButton.move(750, 690)
            sendButton.clicked.connect(self.sendMessage)
            sendButton.show()

    def sendMessage(self):
        self.wechatThreading.start()
        
        # 线程只能用一次，所以重新创建
        self.wechatThreading = threading.Thread(target=self.wechatSendMessage)  
        self.wechatThreading.setDaemon(True)

    def networkError(self):
        q = QMessageBox(self)
        q.setText("网络异常, 无法发送微信消息")
        q.show()

    def notFindError(self):
        q = QMessageBox(self)
        q.setText("没有这个群聊，消息无法发送")
        q.show()        

    def wechatLogin(self):
        # 重写微信登录函数
        # 由于itchat自动登录 虽然异常处理我都捕获并处理了
        # 但是还是存在当我网络正常，但是不想登录或者不想扫二维码而把二维码关闭时
        # 此时wechat发消息这个线程是陷入死循环的，是一直等待你去登录微信
        # 如果只是一条线程倒是无所谓， 但是你多次按了微信发送消息的按钮，却不登录
        # 会开了很多条线程，十分浪费系统资源
        # 所以重写了itchat登录的过程
        def output_info(msg):
            print('[INFO] %s' % msg)

        def open_QR():
            for get_count in range(10):
                # output_info('Getting uuid')
                uuid = itchat.get_QRuuid()
                while uuid is None: 
                    uuid = itchat.get_QRuuid()
                # output_info('Getting QR Code')
                if itchat.get_QR(uuid): break
                elif get_count >= 9:
                    output_info('Failed to get QR Code, please restart the program')
                    sys.exit()
            output_info('Please scan the QR Code')
            return uuid

        uuid = open_QR()
        waitForConfirm = False
        while True:
            # 循环至登录或者status == '408'
            status = itchat.check_login(uuid)
            if status == '200':
                break
            elif status == '201':
                if not waitForConfirm:
                    output_info('Please press confirm')
                    waitForConfirm = True
            elif status == '408':
                os.system('del QR.png')
                sys.exit()

        userInfo = itchat.web_init()
        itchat.show_mobile_login()
        itchat.get_contact()
        itchat.start_receiving()
        output_info("Successful login")
        os.system('del QR.png')


    def wechatSendMessage(self):
        try:
            self.wechatLogin()
            try:
                room_name = itchat.search_chatrooms(name=self.wechatTarget)[0]['UserName']
            except IndexError:
                itchat.logout()
                self.notFindErrorCatch.e.emit()
                return

            if self.openPrice.split('-')[-1] == '0':
                itchat.send('股票可能还未开盘，或者股票获取失败', room_name)
            else:
                itchat.send("最新股价%s %s元\n\n聚会位置：第%d行 第%d列 :)" % \
                    ('-'.join(self.openPrice.split('-')[:-1]),\
                     self.openPrice.split('-')[-1], \
                     self.row, \
                     self.col), \
                        room_name)
            itchat.logout()
        except Exception as e:
            print(e)
            self.networkErrorCatch.e.emit()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = Ui()
    sys.exit(app.exec_())
