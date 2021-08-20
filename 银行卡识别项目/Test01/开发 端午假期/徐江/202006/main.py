import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from resources.py_mainwindow import Ui_MainWindow
# 选择文件引入了Python自带tk库
import tkinter as tk
from tkinter import filedialog
import testDB
# 引入播放mp3的库
from playsound import playsound

class main_window:
    # 1.构造方法
    def __init__(self):
        # 1.1 设置界面
        self.window = Ui_MainWindow()
        self.widget = QtWidgets.QMainWindow()   # 创建widget
        self.window.setupUi(self.widget)    # 创建window放在widget上
        self.widget.show()  #显示窗口
        # 1.2 定义一些变量
        self.image_url = None  # 图片地址
        # 1.3 设置信号函数
        self.window.PB_Choose.clicked.connect(self.slot_PB_Choose)  # 【...】按钮
        self.window.PB_run.clicked.connect(self.slot_PB_run)    # 【识别】按钮

    # 2.【识别】按钮的信号函数
    def slot_PB_run(self):
        print("点击按钮")
        # 2.1 获取识别类型
        # 0代表银行卡，1代表身份证
        type = self.window.comboBox.currentIndex()
        print(type)
        # 2.2 调用识别函数
        # (1) 银行卡类型,目前问题：读取其他的图片程序无法继续运行
        if type == 0:
            mp3_file = testDB.bankcard(self.image_url)
            playsound(mp3_file)
        # (2) 身份证类型

    # 3.【...】按钮的信号函数，选择图片
    def slot_PB_Choose(self):
        print("点击选择按钮")
        root = tk.Tk()  # 使用自带的tkinter库
        root.withdraw()     # 设置对话框
        self.image_url = filedialog.askopenfilename()     # 获取文件路径
        self.window.lineEdit.setText(self.image_url)    # 文件路径写入到文本框


"""主函数"""
if __name__ == '__main__':
    # 1.创建一个应用程序对象
    app = QApplication(sys.argv)  # 创建Qt应用
    m = main_window()   # qt窗口测试
    app.exec_()