# -*- coding: utf-8 -*-
"""
@Auth ：
@File ：login.py
@IDE ：
@Motto:学习新思想，争做新青年
@Email ：
"""
import os
import sys
sys.path.append('ui/UserLogin')
import datetime
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon, Qt, QPalette, QBrush, QPixmap, QGuiApplication, QColor
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog

from mysql.dataDB import *
from ui.UserLogin.register import Ui_registerWindow as registerWindow
import re
from utils.avatar import set_border_avatar, save_avatar_file, upload_avatar
from utils.message import DialogOver



# 登录
class RegisterClient(QMainWindow,registerWindow):
    def __init__(self):
        super(RegisterClient, self).__init__()
        self.setupUi(self)
        # 从文件加载UI定义
        self.setWindowIcon(QIcon('img/favicon.ico'))

        # 设置窗口大小
        self.resize(700, 450)
        # 设置窗口不可拖动
        self.setFixedSize(self.width(), self.height())
        # 设置窗口只显示关闭按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("ui/UserLogin/img/登录.png")))
        self.setPalette(palette)
        self.close_btn.clicked.connect(QApplication.quit)
        self.register_btn.clicked.connect(self.onRegisterIn)
        self.min_btn.clicked.connect(self.min_window)
        self.back_btn.clicked.connect(self.back_login)
        self.label_register_avatar.mousePressEvent = self.upload_avatar
        self.avatar_file_path = None  # 初始化头像文件路径
        #self.main_window = Client()

    def min_window(self):
        self.showMinimized()

    # 注册页面返回功能
    def back_login(self):
        self.hide()
        SI.loginWin.show()

    def upload_avatar(self, event):
        """处理点击头像时上传头像"""
        # 上传头像并显示为带边框的头像
        image_path = upload_avatar(self.label_register_avatar, circular=False, border_width=30, border_color=QColor('#ffffff'))
        if image_path:
            self.avatar_file_path = image_path  # 保存文件路径


    def onRegisterIn(self):
        # 获取用户名密码 去除前后误输入空格
        nick_nema = self.register_nickname.text().strip()
        username = self.register_username.text().strip()
        password = self.register_password.text().strip()
        ack_psd = self.again_password.text().strip()
        # 匹配手机号
        ret = re.match("1[356789]\d{9}", username)


        le = len(username)

        if len(username) == 0 or len(password) == 0 or len(ack_psd) == 0 or len(nick_nema) == 0:
            DialogOver(parent=self, text="昵称、账号、密码不能为空", title="错误", flags="warning")
            return


        # 手机号不匹配
        if ret is None or le!=11:
            DialogOver(parent=self, text="手机号错误", title="错误", flags="warning")
            return
        # 匹配密码包含数字，字母，特殊字符
        """  分开来注释一下：
                ^ 匹配一行的开头位置
                (?![0-9]+$)预测该位置后面不全是数字
                (?![a-zA-Z]+$)预测该位置后面不全是字母
                [0 - 9A - Za - z]{8, 16}由8 - 16位数字或这字母组成  
                $ 匹配行结尾位置 """
        ret_psd = re.match("^(?![A-Za-z]+$)(?![A-Z0-9]+$)(?![a-z0-9]+$)(?![a-z\W]+$)(?![A-Z\W]+$)(?![0-9\W]+$)[a-zA-Z0-9\W]{6,16}$",password)
        if not ret_psd:
            DialogOver(parent=self, text="密码不符合要求，必须包含字母、数字、特殊字符", title="错误", flags="warning")
            return


        if str(password) != str(ack_psd):
            DialogOver(parent=self, text="两次输入密码不一致", title="错误", flags="warning")
            return
        sql = "select * from user where username = '%s'" % username
        result = selectDB(sql)
        if len(result) != 0:
            DialogOver(parent=self, text="该账号已存在，请重新注册", title="错误", flags="warning")
            return
        # 检查头像是否上传
        if self.avatar_file_path is None:
            DialogOver(parent=self, text="请上传头像", title="错误", flags="warning")
            return

        else:
            register_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            avatar_filename = save_avatar_file(self.avatar_file_path)
            sql2 = "insert into user(username,password,nick_name, avatar,register_time) values ('%s','%s','%s','%s','%s')" % (username, password,nick_nema,avatar_filename,register_time)
            insertDB(sql2)
            DialogOver(parent=self, text="恭喜您注册成功", title="成功", flags="success")
            SI.loginWin.show()
            self.hide()







if __name__ == "__main__":
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    app = QApplication([])
    SI.Ui_registerWindow = RegisterClient()
    SI.Ui_registerWindow.show()
    sys.exit(app.exec())
