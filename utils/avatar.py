# -*- coding: utf-8 -*-
"""
@Auth ：
@File ：avatar.py
@IDE ：
@Motto :学习新思想，争做新青年
"""
from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap, Qt, QPainter, QPainterPath, QColor, QPen
import os
import sys
import datetime

from PySide6.QtWidgets import QFileDialog


def set_circular_avatar(label):
    avatar_pixmap = label.pixmap()
    if avatar_pixmap is None:
        return
    # 创建一个与图片大小相同的透明背景图
    size = avatar_pixmap.size()
    circular_pixmap = QPixmap(size)
    circular_pixmap.fill(Qt.transparent)
    # 使用 QPainter 在透明背景图上绘制圆形头像
    painter = QPainter(circular_pixmap)
    painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    # 创建一个圆形路径，裁剪出头像
    path = QPainterPath()
    path.addEllipse(0, 0, size.width(), size.height())
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, avatar_pixmap)
    painter.end()
    label.setPixmap(circular_pixmap)




def set_border_avatar(label, border_width=23, border_color=QColor(0, 177, 252)):
    # 加载图片
    avatar_pixmap = label.pixmap()
    if avatar_pixmap is None:
        return

    # 获取图片大小
    size = avatar_pixmap.size()

    # 创建一个与图片大小相同的透明背景图
    circular_pixmap = QPixmap(size)
    circular_pixmap.fill(Qt.transparent)
    painter = QPainter(circular_pixmap)
    painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 创建一个圆形路径，裁剪出头像
    path = QPainterPath()
    path.addEllipse(0, 0, size.width(), size.height())
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, avatar_pixmap)

    # 绘制圆形边框
    painter.setPen(QPen(border_color, border_width))  # 设置边框颜色和宽度
    painter.setBrush(Qt.transparent)  # 设置填充透明
    painter.setRenderHint(QPainter.Antialiasing)  # 启用抗锯齿
    painter.drawEllipse(border_width / 2, border_width / 2, size.width() - border_width, size.height() - border_width)
    painter.end()
    label.setPixmap(circular_pixmap)




def upload_avatar(label, circular=True, border_width=0, border_color=QColor(0, 177, 252)):
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
    file_dialog.setViewMode(QFileDialog.List)

    if file_dialog.exec():
        # 文件路径
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            image_path = selected_files[0]
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label.setPixmap(pixmap)
                if circular:
                    set_circular_avatar(label)
                else:
                    set_border_avatar(label, border_width=border_width, border_color=border_color)

                return image_path  # 返回文件路径
            else:
                print("无法加载该图片")
    return None



# 保存图片
def save_avatar_file(avatar_path):
    file_extension = os.path.basename(avatar_path)
    # 生成唯一的文件名
    new_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_' + file_extension
    save_dir = "user_avatars" 

    # 确保文件夹存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 保存文件到指定目录
    new_file_path = os.path.join(save_dir, new_filename)
    if QFile.copy(avatar_path, new_file_path):
        return new_filename
    else:
        print("保存头像文件失败")
        return None