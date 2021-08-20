import sys
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class main_window:
    # 1.构造方法
    def __init__(self):
        self.widget = QtWidgets.QWidget()   # 创建widget
        self.window.setupUi(self.widget)    # 创建window放在widget上
        self.widget.show()  #显示窗口


"""主函数"""
if __name__ == '__main__':
    # 1.创建一个应用程序对象
    app = QApplication(sys.argv)  # 创建Qt应用
    m = main_window()
    app.exec_()