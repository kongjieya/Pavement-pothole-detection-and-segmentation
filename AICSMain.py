"""
@Auth ：
@File ：AICSMain.py
@IDE ：
@Motto :学习新思想，争做新青年
"""
import json
import sys
import requests
from utils.AIChatMessage import AIChatMessageWindow, RoleType
from utils.deepseek import ApiThread
sys.path.append('ui/AI')
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication
from ui.AI.AICS import Ui_AIMainWindow
from PySide6.QtCore import QDateTime, QSize, Qt, QEvent
from PySide6.QtWidgets import QMainWindow, QListWidgetItem


class AIWindow(QMainWindow, Ui_AIMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_Submit.clicked.connect(self.on_pushButton_Submit_clicked)
        self.textEdit_input.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.textEdit_input and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                if event.modifiers() & Qt.ShiftModifier:
                    # 按下 Shift+Enter 插入换行
                    cursor = self.textEdit_input.textCursor()
                    cursor.insertText("\n")
                    return True  # 事件被处理，避免传递到其他控件
                else:
                    # 按下 Enter 键发送消息
                    self.on_pushButton_Submit_clicked()
                    return True
        return super().eventFilter(obj, event)

    def on_pushButton_Submit_clicked(self):

        message = self.textEdit_input.toPlainText()
        self.textEdit_input.clear()
        time = str(int(QDateTime.currentDateTime().toSecsSinceEpoch()))  # 获取时间戳
        if message != "":  # 确保消息不为空
            self.updateMessageTimeDisplay(time)
            user_window = AIChatMessageWindow(self.listWidget_out.parentWidget())
            user_item = QListWidgetItem(self.listWidget_out)
            self.updateMessageDisplay(user_window, user_item, message, time, RoleType.user)

        self.current_message_window = AIChatMessageWindow(self.listWidget_out.parentWidget())
        self.current_item = QListWidgetItem(self.listWidget_out)
        # 启动API请求线程
        self.api_thread = ApiThread(message)
        self.api_thread.response_signal.connect(self.on_api_response)
        self.api_thread.start()

        self.listWidget_out.setCurrentRow(self.listWidget_out.count() - 1)

    def on_api_response(self, response):
        time = str(int(QDateTime.currentDateTime().toSecsSinceEpoch()))  # 获取时间戳

        if hasattr(self, 'current_item') and self.current_item:
            current_message_window = self.current_message_window
            current_text = current_message_window.message_text  # 获取当前显示的文本
            current_text += response
            # 更新消息显示
            self.updateMessageDisplay(current_message_window, self.current_item, current_text, time, RoleType.system)
            # 将消息列表滚动到最新的消息项
            self.listWidget_out.setCurrentRow(self.listWidget_out.count() - 1)

    def updateMessageDisplay(self, message_window, current_item, text, time, userType):
        message_window.setFixedWidth(self.width())  # 设置消息窗口的宽度为主窗口的宽度
        size = message_window.font_rect(text)  # 获取文本的矩形区域
        current_item.setSizeHint(QSize(self.width(), size.height()))  # 设置列表项的高度为文本高度
        message_window.setText(text, time, size, userType)
        self.listWidget_out.setItemWidget(current_item, message_window)  # 将消息添加到消息列表中

    # 处理消息的时间显示
    def updateMessageTimeDisplay(self, curMsgTime):
        if self.listWidget_out.count() > 0:
            lastItem = self.listWidget_out.item(self.listWidget_out.count() - 1)
            message_window = self.listWidget_out.itemWidget(lastItem)
            lastTime = int(message_window.message_time)  # 获取最后一条消息的时间戳
            curTime = int(curMsgTime)  # 获取当前时间戳
            show_time = (curTime - lastTime) > 60  # 如果两条消息相差超过60秒，显示时间
        else:
            show_time = True

        if show_time:
            messageTime = AIChatMessageWindow(self.listWidget_out.parentWidget())
            itemTime = QListWidgetItem(self.listWidget_out)
            size = QSize(self.width(), 40)
            messageTime.resize(size)
            itemTime.setSizeHint(size)
            messageTime.setText(curMsgTime, curMsgTime, size, RoleType.current_time)
            self.listWidget_out.setItemWidget(itemTime, messageTime)

    def resizeEvent(self, event):
        for i in range(self.listWidget_out.count()):
            current_message_window = self.listWidget_out.itemWidget(self.listWidget_out.item(i))
            current_item = self.listWidget_out.item(i)
            self.updateMessageDisplay(current_message_window, current_item, current_message_window.message_text,
                                      current_message_window.message_time, current_message_window.message_userType)


if __name__ == '__main__':
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    app = QApplication(sys.argv)
    view = AIWindow()
    view.show()
    sys.exit(app.exec())
