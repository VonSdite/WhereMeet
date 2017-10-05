import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from make_map import resRowCol
from stock_price import getOpenPrice

class Ui(QWidget):
    """docstring for Quit"""

    def __init__(self, configFile='config.txt'):
        super(Ui, self).__init__()
        self.configFile = configFile                    # Ui的配置文件，配置桌子
        self.openPrice = getOpenPrice()                 # 开盘价
        self.row, self.col = resRowCol(self.openPrice)  # 目标结果行和列
        self.initUI()

    def initUI(self):
        # 设置背景图片
        bk = QLabel(self)
        bk.resize(950, 800)
        bk.move(0, 0)
        pixMap = QPixmap('img/bk.jpg').scaled(bk.width(), bk.height())
        bk.setPixmap(pixMap)

        priceLabel = QLabel(self)
        priceLabel.setText('<font color=white><b>今日股票开盘价%s元</b></font>' \
                           % self.openPrice.split('-')[-1])
        priceLabel.setFont(QFont('宋体', 20))
        priceLabel.move(530, 30)

        self.resTable = None            # 目标位置对象
        self.resTableColor = None       # 目标位置桌子颜色
        self.resTablePos = None
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
                    d.resize(40, 25)
                    pixMap = QPixmap('img/%s.jpg' % e).scaled(d.width(), d.height())
                    d.move(col, row)
                    d.setPixmap(pixMap)

                    if cnt_row == self.row and cnt_col == self.col:
                        self.resTable = d
                        self.resTableColor = e
                        self.resTablePos = (row, col)

                row += 40       # 下一行放置的位置


        btn = QPushButton('点我', self)
        btn.setIcon(QIcon(r'img\button.gif'))
        btn.resize(80, 40)
        btn.move(600, 690)
        btn.clicked.connect(self.buttonClicked)

        self.setWindowTitle('WhereMeet?')
        self.setWindowIcon(QIcon('img\gathering.jpg'))
        self.resize(950, 800)
        self.center()
        self.setFixedSize(self.width(), self.height())  # 禁止改变窗口大小
        self.show()

    def buttonClicked(self):
        self.resTable.resize(40, 110)
        self.resTable.move(self.resTablePos[1], self.resTablePos[0]-85)
        pixMap = QPixmap('img/%s_selected.jpg' % self.resTableColor).scaled(\
                                                            self.resTable.width(),\
                                                            self.resTable.height())
        self.resTable.setPixmap(pixMap)

        targetLabel = QLabel(self)
        targetLabel.setText('<font color=white>聚会位置：第<b>%d</b>行 第<b>%d</b>列</font>'\
                           % (self.row, self.col))
        targetLabel.setFont(QFont('宋体', 20))
        targetLabel.move(530, 130)
        targetLabel.show()

        sendButton = QPushButton('发送到微信', self)

        sendButton.setIcon(QIcon(r'img\wechat.jpg'))
        sendButton.resize(130, 40)
        sendButton.move(750, 690)
        sendButton.clicked.connect(self.sendMessage)
        sendButton.show()

    def sendMessage(self):
        pass


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = Ui()
    sys.exit(app.exec_())