# -*- coding: utf-8 -*-
"""
@Auth ：
@File ：AIChatMessage.py
@IDE ：
@Motto :学习新思想，争做新青年
"""

from PySide6.QtWidgets import QWidget, QLabel, QTextEdit
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QPen, QTextOption, QPainterPath, QFontMetrics
from PySide6.QtCore import QRect, QSize, Qt, QDateTime


class RoleType:
    system = 1
    user = 2
    current_time = 3


class AIChatMessageWindow(QWidget):
    def __init__(self, parent=None):
        super(AIChatMessageWindow, self).__init__(parent)

        te_font = self.font()
        te_font.setFamily("Microsoft YaHei")
        te_font.setPointSize(14)
        self.setFont(te_font)

        self.leftPixmap = QPixmap("./ui/AI/img/20250207123441.jpg")
        self.rightPixmap = QPixmap("./ui/AI/img/20250207112921.jpg")

        # 初始化消息相关的属性
        self.message_text = ""  # 消息内容
        self.message_time = ""  # 消息时间
        self.current_time = ""  # 当前时间
        self.message_size = QSize()  # 消息的大小
        self.message_userType = RoleType.system  # 消息类型（默认为系统消息）
        self.frame_width = 0  # 消息框的宽度
        self.text_width = 0  # 文本宽度
        self.space_width = 0  # 空间宽度
        self.line_height = 0  # 行高
        self.is_sending = False  # 是否正在发送
        self.left_icon_rect = QRect()  # 左侧头像矩形
        self.right_icon_rect = QRect()  # 右侧头像矩形
        self.left_triangle_rect = QRect()  # 左侧三角形矩形
        self.right_triangle_rect = QRect()  # 右侧三角形矩形
        self.left_frame_rect = QRect()  # 左侧消息框矩形
        self.right_frame_rect = QRect()  # 右侧消息框矩形
        self.left_text_rect = QRect()  # 左侧文本矩形
        self.right_text_rect = QRect()  # 右侧文本矩形

    # 设置消息内容、时间、大小和用户类型
    def setText(self, text, time, allSize, userType):
        self.message_text = text  # 消息内容
        self.message_userType = userType
        self.message_time = time  # 消息的时间
        self.current_time = QDateTime.fromSecsSinceEpoch(int(time)).toString("hh:mm")  # 格式化时间
        self.message_size = allSize  # 消息的总大小
        self.update()  # 更新窗口

    # 计算文本的实际显示区域大小
    def font_rect(self, str):
        self.message_text = str
        minHei = 30  # 最小高度
        iconWH = 40  # 头像的宽高
        iconSpaceW = 20  # 头像与文本之间的间隔
        iconRectW = 5  # 头像矩形宽度
        iconTMPH = 10  # 头像的临时高度
        sanJiaoW = 6  # 三角形的宽度
        kuangTMP = 20  # 消息框的临时宽度
        textSpaceRect = 12  # 文本间隙

        # 计算消息框和文本的宽度
        self.frame_width = self.width() - kuangTMP - 2 * (iconWH + iconSpaceW + iconRectW)
        self.text_width = self.frame_width - 2 * textSpaceRect
        self.space_width = self.width() - self.text_width
        self.left_icon_rect = QRect(iconSpaceW, iconTMPH, iconWH, iconWH)  # 左侧头像矩形
        self.right_icon_rect = QRect(self.width() - iconSpaceW - iconWH, iconTMPH, iconWH, iconWH)  # 右侧头像矩形

        # 获取实际字符串的大小
        size = self.getRealString(self.message_text)

        hei = max(size.height(), minHei)

        # 设置三角形的位置和大小
        self.left_triangle_rect = QRect(iconWH + iconSpaceW + iconRectW, self.line_height // 2, sanJiaoW,
                                        hei - self.line_height)
        self.right_triangle_rect = QRect(self.width() - iconRectW - iconWH - iconSpaceW - sanJiaoW,
                                         self.line_height // 2, sanJiaoW, hei - self.line_height)

        # 根据文本的宽度和头像的位置，设置消息框的位置和大小
        if size.width() < (self.text_width + self.space_width):
            self.left_frame_rect.setRect(self.left_triangle_rect.x() + self.left_triangle_rect.width(),
                                         self.line_height // 4 * 3, size.width() - self.space_width + 2 * textSpaceRect,
                                         hei - self.line_height)
            self.right_frame_rect.setRect(
                self.width() - size.width() + self.space_width - 2 * textSpaceRect - iconWH - iconSpaceW - iconRectW - sanJiaoW,
                self.line_height // 4 * 3, size.width() - self.space_width + 2 * textSpaceRect, hei - self.line_height)
        else:
            self.left_frame_rect.setRect(self.left_triangle_rect.x() + self.left_triangle_rect.width(),
                                         self.line_height // 4 * 3, self.frame_width, hei - self.line_height)
            self.right_frame_rect.setRect(iconWH + kuangTMP + iconSpaceW + iconRectW - sanJiaoW,
                                          self.line_height // 4 * 3, self.frame_width, hei - self.line_height)

        # 设置文本的矩形区域
        self.left_text_rect.setRect(self.left_frame_rect.x() + textSpaceRect, self.left_frame_rect.y() + iconTMPH,
                                    self.left_frame_rect.width() - 2 * textSpaceRect,
                                    self.left_frame_rect.height() - 2 * iconTMPH)
        self.right_text_rect.setRect(self.right_frame_rect.x() + textSpaceRect, self.right_frame_rect.y() + iconTMPH,
                                     self.right_frame_rect.width() - 2 * textSpaceRect,
                                     self.right_frame_rect.height() - 2 * iconTMPH)

        return QSize(size.width(), hei)

    def getRealString(self, src):
        fm = self.fontMetrics()
        self.line_height = fm.lineSpacing()

        nCount = src.count("\n")
        nMaxWidth = 0
        max_chars_per_line = 50

        import re
        src = re.sub(r'(\d)(\D)', r'\1 \2', src)  # 数字后加空格
        #src = re.sub(r'(\D)(\d)', r'\1 \2', src)  # 数字前加空格

        # 如果没有换行符的情况下
        if nCount == 0:
            nMaxWidth = fm.horizontalAdvance(src)

            # 如果文本宽度超过了容器宽度，才需要根据最大字符数强制换行
            if nMaxWidth > self.text_width:
                num_lines = (len(src) + max_chars_per_line - 1) // max_chars_per_line
                nCount += num_lines  # 更新行数
                nMaxWidth = self.text_width
            else:
                num_lines = (len(src) + max_chars_per_line - 1) // max_chars_per_line
                nCount += num_lines  # 更新行数

        else:
            for line in src.split("\n"):
                line_width = fm.horizontalAdvance(line)
                nMaxWidth = max(nMaxWidth, line_width)

                # 计算行内字符数并处理换行
                num_lines = (len(line) + max_chars_per_line - 1) // max_chars_per_line
                nCount += num_lines

                # 对每一行宽度进行处理，特别是数字和文字的混合
                if line_width > self.text_width:
                    # 如果某一行超过最大宽度，强制换行
                    nMaxWidth = self.text_width

        # 返回尺寸
        return QSize(nMaxWidth + self.space_width, (nCount + 1) * self.line_height + self.line_height)

    # 绘制消息内容
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # 获取 QWidget 的设备像素比（DPI 比例）
        device_pixel_ratio = self.devicePixelRatio()

        if self.message_userType == RoleType.system:  # openai信息
            # 确保头像与设备像素比一致
            pixmap = self.leftPixmap
            if pixmap.devicePixelRatio() != device_pixel_ratio:
                # 将 QPixmap 缩放为正确的 DPI 比例
                pixmap = self.leftPixmap.scaled(self.left_icon_rect.size() * device_pixel_ratio,
                                                Qt.KeepAspectRatio, Qt.SmoothTransformation)
                pixmap.setDevicePixelRatio(device_pixel_ratio)

            # 绘制左侧头像
            painter.drawPixmap(self.left_icon_rect, pixmap)

            # 绘制消息框
            col_KuangB = QColor(234, 234, 234)
            painter.setBrush(col_KuangB)
            painter.drawRoundedRect(self.left_frame_rect.adjusted(-1, -1, 1, 1), 4, 4)

            # 绘制消息框的实际背景
            col_Kuang = QColor(255, 255, 255)
            painter.setBrush(col_Kuang)
            painter.drawRoundedRect(self.left_frame_rect, 4, 4)

            # 绘制文本
            penText = QPen(QColor(51, 51, 51))  # 设置文本颜色
            painter.setPen(penText)
            option = QTextOption(Qt.AlignLeft | Qt.AlignVCenter)
            option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)  # 设置自动换行
            painter.drawText(self.left_text_rect, self.message_text, option)

        elif self.message_userType == RoleType.user:  # 用户的消息,右侧头像
            # 确保头像与设备像素比一致
            pixmap = self.rightPixmap
            if pixmap.devicePixelRatio() != device_pixel_ratio:
                # 将 QPixmap 缩放为正确的 DPI 比例
                pixmap = self.rightPixmap.scaled(self.right_icon_rect.size() * device_pixel_ratio,
                                                 Qt.KeepAspectRatio, Qt.SmoothTransformation)
                pixmap.setDevicePixelRatio(device_pixel_ratio)  # 设置设备像素比

            # 绘制右侧头像
            painter.drawPixmap(self.right_icon_rect, pixmap)

            # 绘制消息框
            col_Kuang = QColor(75, 164, 242)
            painter.setBrush(col_Kuang)
            painter.drawRoundedRect(self.right_frame_rect, 4, 4)

            # 绘制文本
            penText = QPen(Qt.white)  # 设置文本颜色为白色
            painter.setPen(penText)
            option = QTextOption(Qt.AlignLeft | Qt.AlignVCenter)
            option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
            painter.drawText(self.right_text_rect, self.message_text, option)




        elif self.message_userType == RoleType.current_time:  # 时间消息
            penText = QPen(QColor(153, 153, 153))  # 设置时间文本的颜色
            painter.setPen(penText)
            option = QTextOption(Qt.AlignCenter)  # 时间居中显示
            option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
            # 设置时间文本的字体
            te_font = self.font()
            te_font.setFamily("Microsoft YaHei")
            te_font.setPointSize(10)
            painter.setFont(te_font)
            painter.drawText(self.rect(), self.current_time, option)
