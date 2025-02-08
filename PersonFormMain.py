# -*- coding: utf-8 -*-
"""
@Auth ：
@File ：PersonFormMain.py
@IDE ：
@Motto :学习新思想，争做新青年
"""
from mysql.dataDB import SI
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Signal, Qt
from AICSMain import AIWindow
from ui.UserInfo.userform import Ui_personForm
from utils.UserInfo import UserInfo
from utils.message import DialogOver


class PersonFormMain(QDialog, Ui_personForm):
    userinfo_signal = Signal()
    logout_signal = Signal()  # 退出登录

    def __init__(self, parent=None):
        super(PersonFormMain, self).__init__(parent)
        self.setupUi(self)

        # 加载用户信息
        user_info = UserInfo()
        username, nickname, avatar_path, register_time = user_info.load_user_info()
        self.label_userform_name.setText(nickname)
        self.PersonFormMainBind()

    def PersonFormMainBind(self):
        self.pushButton_userform_logout.clicked.connect(self.on_logout)
        self.pushButton_userform_userinfo.clicked.connect(self.userinfo)
        self.pushButton_userform_AIFirstAid.clicked.connect(self.AIFirstAid)
        self.pushButton_userform_Feedback.clicked.connect(self.Feedback)


    def userinfo(self):
        self.userinfo_signal.emit()
        self.close()

    def AIFirstAid(self):
        SI.AIWindow = AIWindow()
        SI.AIWindow.show()
        self.close()


    def Feedback(self):
        DialogOver(parent=self, text="功能待上线", title="敬请期待", flags="info")

    def on_logout(self):
        self.logout_signal.emit()
        self.close()


