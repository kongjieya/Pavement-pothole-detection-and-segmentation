"""
@Auth ：
@File ：login.py
@IDE ：
@Motto:学习新思想，争做新青年
@Email ：
"""
import datetime
import sys

sys.path.append('ui/UserLogin')
import configparser
from PySide6.QtGui import QIcon, Qt, QPalette, QBrush, QPixmap, QGuiApplication
from PySide6.QtWidgets import QMainWindow, QApplication
from Register import RegisterClient
from ui.UserLogin.login import Ui_LoginMainWindow
from MainUI import Client
import re
from mysql.dataDB import *
from utils.message import DialogOver
from utils.UserInfo import UserInfo


class Win_Login(QMainWindow, Ui_LoginMainWindow):
    def __init__(self, parent=None):
        super(Win_Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('img/favicon.ico'))
        # 设置窗口大小
        self.resize(700, 450)
        # 设置窗口不可拖动
        self.setFixedSize(self.width(), self.height())
        # 设置窗口只显示关闭按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # 隐藏边框1
        self.setWindowFlags(Qt.FramelessWindowHint)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("ui/UserLogin/img/登录.png")))
        self.setPalette(palette)

        self.close_btn.clicked.connect(self.to_close)
        self.btn_login.clicked.connect(self.onSignIn)
        self.btn_register.clicked.connect(self.to_register)
        self.edit_password.returnPressed.connect(self.onSignIn)
        self.min_btn.clicked.connect(self.min_window)

        self.main_window = Client()

    def onSignIn(self):
        # 获取用户名密码
        username = self.edit_username.text().strip()
        password = self.edit_password.text().strip()

        if username == "" or password == "":
            DialogOver(parent=self, text="用户名/密码不能为空", title="错误", flags="warning")
            return

        sql = "SELECT * FROM user WHERE username = '%s' AND password = '%s'" % (username, password)
        result = selectDB(sql)

        if len(result) == 0:
            DialogOver(parent=self, text="用户名/密码错误", title="错误", flags="warning")
            return

        # 从数据库获取信息
        user_info = result[0]
        #print(user_info)
        avatar_path = user_info['avatar']
        nickname = user_info['nick_name']
        register_time = user_info['register_time']

        register_time = register_time.strftime('%Y-%m-%d')

        # 将用户信息保存到 UserInfo
        user_info_instance = UserInfo()
        user_info_instance.save_user_info(username, nickname, avatar_path, register_time)

        self.main_window.set_userinfo()
        self.main_window.show()
        self.hide()
        self.edit_username.setText("")
        self.edit_password.setText("")

    def to_register(self):
        SI.registerWin = RegisterClient()
        SI.registerWin.show()
        self.hide()

    def min_window(self):
        self.showMinimized()

    def to_close(self):
        closeDB()
        print("数据库已关闭")
        self.close()


if __name__ == '__main__':
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    app = QApplication([])
    user_info_instance = UserInfo()

    # 判断用户是否已登录
    if user_info_instance.is_user_logged_in():
        SI.mainWin = Client()
        SI.mainWin.show()
    else:
        SI.loginWin = Win_Login()
        SI.loginWin.show()

    sys.exit(app.exec())
