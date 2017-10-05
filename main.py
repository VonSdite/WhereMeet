# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from ui import Ui
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    # 创建界面并运行程序
    app = QApplication(sys.argv)
    ui = Ui(configFile='config.txt')
    sys.exit(app.exec_())
