# -*- coding: utf-8 -*-
"""
@Auth ：
@File ：UserInfo.py
@IDE ：
@Motto :学习新思想，争做新青年
"""

from PySide6.QtCore import QSettings

class UserInfo:
    def __init__(self):
        self.settings = QSettings("Organization", "Application")

    def save_user_info(self, username, nickname, avatar_path,register_time):
        """保存用户信息到 QSettings"""
        self.settings.setValue("user/username", username)
        self.settings.setValue("user/nickname", nickname)
        self.settings.setValue("user/avatar", avatar_path)
        self.settings.setValue("user/register_time", register_time)

        self.settings.sync()  # 写入存储

    def load_user_info(self):
        """加载存储的用户信息"""
        username = self.settings.value("user/username", "")
        nickname = self.settings.value("user/nickname", "")
        avatar_path = self.settings.value("user/avatar", "")
        register_time = self.settings.value("user/register_time")
        return username, nickname, avatar_path, register_time

    def clear_user_info(self):
        """清除存储的用户信息"""
        self.settings.remove("user/username")
        self.settings.remove("user/nickname")
        self.settings.remove("user/avatar")
        self.settings.remove("user/register_time")
        self.settings.sync()

    def is_user_logged_in(self):
        """判断用户是否已经登录"""
        username = self.settings.value("user/username", "")
        return bool(username)


# if __name__ == '__main__':
#     UserInfo = UserInfo()
#     print("Storage location:", UserInfo.settings.fileName())



# from PySide6.QtGui import QPixmap
# from PySide6.QtCore import QMutex, QMutexLocker
#
# class UserInfo:
#     _instance = None
#     _mutex = QMutex()
#
#     def __new__(cls):
#         with QMutexLocker(cls._mutex):
#             if cls._instance is None:
#                 cls._instance = super(UserInfo, cls).__new__(cls)
#                 cls._instance.username = ""  # 用户名
#                 cls._instance.nickname = ""  # 昵称
#                 cls._instance.avatar = None  # 头像
#         return cls._instance
#
#     def set_username(self, username):
#         self.username = username
#
#     def get_username(self):
#         return self.username
#
#     def set_nickname(self, nickname):
#         self.nickname = nickname
#
#     def get_nickname(self):
#         return self.nickname
#
#     def set_avatar(self, avatar_pixmap):
#         self.avatar = avatar_pixmap
#
#     def get_avatar(self):
#         return self.avatar
