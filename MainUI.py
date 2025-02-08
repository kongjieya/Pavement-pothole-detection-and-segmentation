"""
@Auth ：
@File ：MainUI.py
@IDE ：
@Motto:学习新思想，争做新青年
@Email ：
"""
import json
import os
import re
import sys
sys.path.append('ui')
sys.path.append('ui/UserInfo')
import cv2
import numpy as np
from PIL.Image import Image
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu, QTableWidgetItem, QHeaderView, QDialog, \
    QGraphicsDropShadowEffect
from PySide6.QtGui import QImage, QPixmap, QColor, QCursor, QAction, QGuiApplication, QPainter, QPainterPath
from PySide6.QtCore import QTimer, QThread, Signal, QObject, Qt,QEvent
from mysql.dataDB import *
from utils.capnums import Camera
from detect_mainui import YoloPredictor
from ui.main_ui_v7 import Ui_MainWindow
from utils.main_utils import check_url
from utils.UserInfo import UserInfo
from utils.avatar import set_circular_avatar, upload_avatar, save_avatar_file
from utils.message import DialogOver
from PersonFormMain import PersonFormMain




class Client(QMainWindow, Ui_MainWindow):
    main2yolo_begin_sgl = Signal()

    def __init__(self, parent=None):
        super(Client, self).__init__()

        self.setupUi(self)  # 初始化界面
        self.m_flag = False
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏
        self.progressBar.setValue(0)

        self.yolo_init()

        # 主要功能绑定
        self.main_function_bind()
        self.pushButton_start_stop.setCheckable(True)  # 将按钮设置为开关状态为真

        self.yolo_predict.new_model_name = 'runs/segment/yolov8seg-EMA(0.714_0.707)/weights/best.pt'


        self.yolo_predict.load_yolo_model()

        # 配置加载
        self.load_config()

        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 90)
        self.tableWidget.setColumnWidth(4, 230)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)

        self.center_window()  # 居中显示窗口
        self.set_avatars()
        self.set_userinfo()
        self.person_form = None  # 初始化弹出窗口
        self.pushButton_mian_username.installEventFilter(self)  # 悬停事件
        self.installEventFilter(self)  # 主窗口的事件过滤器
        self.upload_avatar_path = None  # 初始化头像文件路径

      


    def yolo_init(self):
        # Yolo-v8 thread  初始化
        '''
        这段代码是 Yolo 模型的初始化过程，
        在这里主要是负责设置模型名称、创建 Yolo 线程、将 Yolo 信号连接到主线程的槽函数上，
        并将主线程的信号连接到 Yolo 类的槽函数上，并启动 Yolo 线程。
        '''
        self.yolo_predict = YoloPredictor()
        self.yolo_thread = QThread()
        # 将 Yolo 类中的信号绑定到主线程的槽函数上
        # # 显示预测视频（左，右）
        self.yolo_predict.yolo2main_trail_img.connect(lambda x: self.show_image(x, self.label_input, 'img'))  # 绑定原始图

        self.yolo_predict.yolo2main_box_img.connect(lambda x: self.show_image(x, self.label_out, 'img'))  # 绑定结果图

        self.yolo_predict.yolo2main_status_msg.connect(lambda x: self.show_status(x))
        self.yolo_predict.yolo2main_tabel_show.connect(self.tabel_show)
        self.yolo_predict.yolo2main_progressBar.connect(lambda x: self.progressBar.setValue(x))  # 进度条

        # 将主线程的信号绑定到 Yolo 类的槽函数上，并启动 Yolo 线程
        self.yolo_predict.moveToThread(self.yolo_thread)
        self.main2yolo_begin_sgl.connect(self.yolo_predict.run)

    # 主页面各功能绑定
    def main_function_bind(self):
        # 打开文件夹
        self.pushButton_openimg.clicked.connect(self.open_src_file)
        # 摄像头
        self.pushButton_sht.clicked.connect(self.chose_cam)
        # 开始
        self.pushButton_start_stop.clicked.connect(self.run_or_continue)
        # 终止
        self.pushButton_exit.clicked.connect(self.stop)

        self.min_btn.clicked.connect(self.to_minmal)
        self.max_btn.clicked.connect(self.max_or_restore)
        self.close_btn.clicked.connect(self.to_close)
        self.index_btn.clicked.connect(self.show_home)
        self.main_btn.clicked.connect(self.show_detect)
        self.userinfo_btn.clicked.connect(self.show_profile)
        self.index_btn.setCheckable(True)
        self.main_btn.setCheckable(True)
        self.userinfo_btn.setCheckable(True)

        # 设置默认选中的按钮和显示首页
        self.index_btn.setChecked(True)
        self.show_home()  # 确保启动时显示首页
        self.update_button_styles()
        self.label_avatar.mousePressEvent = self.upload_avatar
        self.exit_btn.clicked.connect(self.to_close)

        self.handleSubmit_btn.clicked.connect(self.handleSubmit)
        self.handleClose_btn.clicked.connect(self.handleClose)
        self.handleSubmit_btn_password.clicked.connect(self.handleSubmit_password)


    def set_userinfo(self):
        user_info = UserInfo()
        username, nickname, avatar_path,register_time = user_info.load_user_info()
        self.pushButton_mian_username.setText(nickname)  # 显示昵称
        self.lineEdit_name.setText(nickname)
        self.lineEdit_phone.setText(username)
        self.lineEdit_createTime.setText(register_time)
        self.lineEdit_phone.setDisabled(True)
        self.lineEdit_createTime.setDisabled(True)
        if avatar_path:
            self.set_avatar(avatar_path)  # 假设你有一个方法来设置头像

    def eventFilter(self, source, event):
        if source == self.pushButton_mian_username:
            if event.type() == QEvent.Enter:  # 鼠标进入按钮
                self.show_person_form()  # 显示个人中心窗口
            elif event.type() == QEvent.Leave:  # 鼠标离开按钮
                # 判断鼠标是否在弹出窗口区域内
                if self.person_form and not self.person_form.rect().contains(
                        self.person_form.mapFromGlobal(QCursor.pos())):
                    self.close_person_form()  # 关闭个人中心窗口

        elif source == self.person_form:
            if event.type() == QEvent.Enter:  # 鼠标进入弹出窗口时
                return True  # 允许事件继续传播

            if event.type() == QEvent.Leave:  # 鼠标离开弹出窗口时
                if not self.pushButton_mian_username.rect().contains(
                        self.pushButton_mian_username.mapFromGlobal(QCursor.pos())):
                    self.close_person_form()

        return super().eventFilter(source, event)
    def show_person_form(self):
        if not self.person_form:
            self.person_form = PersonFormMain(self)
            self.person_form.logout_signal.connect(self.logout)
            self.person_form.userinfo_signal.connect(self.show_profile)

            button_rect = self.pushButton_mian_username.geometry()
            x = button_rect.x()
            y = button_rect.bottom()

            # 设置弹出窗口的位置,位置这个自己调一下
            self.person_form.setGeometry(x + 70, y + 21, self.person_form.width(), self.person_form.height())

            self.person_form.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题栏

            self.person_form.setWindowModality(Qt.ApplicationModal)  # 阻止父窗口交互

            # 弹出窗口事件过滤器
            self.person_form.installEventFilter(self)

            self.shadow_effect(self.person_form)


        if not self.person_form.isVisible():
            self.person_form.show()

    def close_person_form(self):
        if self.person_form and self.person_form.isVisible():
            self.person_form.close()
            self.person_form = None
    def shadow_effect(self, widget):
        shadow_effect = QGraphicsDropShadowEffect(widget)
        shadow_effect.setBlurRadius(15)  # 模糊半径
        shadow_effect.setColor(Qt.gray)  # 阴影颜色
        shadow_effect.setOffset(0, 0)

        # 将阴影应用到窗口
        widget.setGraphicsEffect(shadow_effect)

    def center_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        # 设置合适的初始宽度和高度
        new_width = min(900, screen.width())
        new_height = min(600, screen.height())
        self.resize(new_width, new_height)
        self.move((screen.width() - new_width) / 2, (screen.height() - new_height) / 2)
        # self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def set_avatars(self):
        labels = [self.label_userAvatar, self.label_avatar]
        for label in labels:
            set_circular_avatar(label)

    def set_avatar(self, avatar_filename):
        """设置头像并更新显示"""
        if avatar_filename:
            # 加载头像并设置到 QLabel
            avatar_path = os.path.join("user_avatars", avatar_filename)
            pixmap = QPixmap(avatar_path)
            if not pixmap.isNull():
                self.label_userAvatar.setPixmap(pixmap)
                self.label_avatar.setPixmap(pixmap)
                labels = [self.label_userAvatar, self.label_avatar]
                for label in labels:
                    set_circular_avatar(label)
        else:
            print("没有头像路径")

    def handleSubmit(self):
        """提交修改并更新数据库"""
        new_nickname = self.lineEdit_name.text().strip()  # 获取昵称

        user_info = UserInfo()
        username, nickname, avatar_path, register_time = user_info.load_user_info()  # 获取用户名和注册时间


        if not new_nickname:
            DialogOver(parent=self, text="昵称不能为空！", title="提交失败", flags="warning")
            return
        if not self.upload_avatar_path and nickname == new_nickname:
            DialogOver(parent=self, text="未修改任何信息！", title="提交失败", flags="warning")
            return
        if not self.upload_avatar_path:
            avatar_filename = avatar_path
        else:
            avatar_filename = save_avatar_file(self.upload_avatar_path)


        sql = "UPDATE user SET nick_name= '%s', avatar='%s' WHERE username='%s'" % (new_nickname, avatar_filename,username)
        result = insertDB(sql)
        if result:
            user_info.save_user_info(username, new_nickname, avatar_filename, register_time)
            self.set_userinfo()  # 更新界面
            DialogOver(parent=self, text="修改已保存！", title="提交成功", flags="success")
        else:
            DialogOver(parent=self, text="保存失败，请稍后再试！", title="提交失败", flags="danger")

    def handleSubmit_password(self):
        old_password = self.lineEdit_old_password.text().strip()
        new_password = self.lineEdit_new_password.text().strip()
        check_password = self.lineEdit_check_password.text().strip()


        ret_psd = re.match("^(?![A-Za-z]+$)(?![A-Z0-9]+$)(?![a-z0-9]+$)(?![a-z\W]+$)(?![A-Z\W]+$)(?![0-9\W]+$)[a-zA-Z0-9\W]{6,16}$",new_password)

        if not ret_psd:
            DialogOver(parent=self, text="密码不符合要求，必须包含字母、数字、特殊字符", title="错误", flags="warning")
            return

        if str(new_password) != str(check_password):
            DialogOver(parent=self, text="两次输入密码不一致", title="错误", flags="warning")
            return

        user_info = UserInfo()
        username, _, _, _ = user_info.load_user_info()  # 获取账号

        sql_get_password = f"SELECT password FROM user WHERE username='{username}'"
        db_result = selectDB(sql_get_password)

        # 对比旧密码
        current_password = db_result[0]["password"]
        if old_password != current_password:
            DialogOver(parent=self, text="原密码不正确", title="错误", flags="warning")
            return


        sql_update_password = f"UPDATE user SET password='{new_password}' WHERE username='{username}'"
        result = insertDB(sql_update_password)

        if result:
            self.lineEdit_old_password.setText("")
            self.lineEdit_new_password.setText("")
            self.lineEdit_check_password.setText("")
            DialogOver(parent=self, text="密码修改成功，下次登录生效！", title="成功", flags="success")
        else:
            DialogOver(parent=self, text="密码修改失败，请稍后再试！", title="错误", flags="danger")



    def handleClose(self):
        self.set_userinfo()
    def logout(self):
        user_info_instance = UserInfo()
        user_info_instance.clear_user_info()
        self.hide()
        if not hasattr(SI, 'loginWin') or SI.loginWin is None:
            from Login import Win_Login
            SI.loginWin = Win_Login()
        SI.loginWin.show()

    def upload_avatar(self, event):
        image_path = upload_avatar(self.label_avatar, circular=True)
        if image_path:
            self.upload_avatar_path = image_path  # 上传路径

    def update_button_styles(self):
        # 更新按钮的背景颜色
        if self.index_btn.isChecked():
            self.index_btn.setStyleSheet("background:#e6e6e6; ")
        else:
            self.index_btn.setStyleSheet("")

        if self.main_btn.isChecked():
            self.main_btn.setStyleSheet("background:#e6e6e6;")
        else:
            self.main_btn.setStyleSheet("")

        if self.userinfo_btn.isChecked():
            self.userinfo_btn.setStyleSheet("background:#e6e6e6;")
        else:
            self.userinfo_btn.setStyleSheet("")

    def show_home(self):
        self.stackedWidget.setCurrentIndex(0)
        self.index_btn.setChecked(True)
        self.main_btn.setChecked(False)
        self.userinfo_btn.setChecked(False)
        self.update_button_styles()

    def show_detect(self):
        self.stackedWidget.setCurrentIndex(1)
        self.index_btn.setChecked(False)
        self.main_btn.setChecked(True)
        self.userinfo_btn.setChecked(False)
        self.update_button_styles()

    def show_profile(self):
        self.stackedWidget.setCurrentIndex(2)
        self.index_btn.setChecked(False)
        self.main_btn.setChecked(False)
        self.userinfo_btn.setChecked(True)
        self.update_button_styles()

    #主窗口显示原图与检测结果
    @staticmethod
    def show_image(img, label, flag):

        if flag == "path":
            img_src = cv2.imdecode(np.fromfile(img, dtype=np.uint8), -1)
        else:
            img_src = img

        # Resize the image
        img_src_ = cv2.resize(img_src, (640, 480))

        # 将 OpenCV 图像转换为 QImage 对象，并将其显示在 QLabel 组件中
        frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
        img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1], QImage.Format_RGB888)

        label.setPixmap(QPixmap.fromImage(img))
        label.setScaledContents(True)  # 自适应界面大小

    # 控制开始|暂停
    def run_or_continue(self):
        if self.yolo_predict.source == '' or self.yolo_predict.source is None:
            DialogOver(parent=self, text="请重新上传文件", title="运行失败", flags="danger")
            self.pushButton_start_stop.setChecked(False)
            return

        self.yolo_predict.stop_dtc = False
        # 开始
        if self.pushButton_start_stop.isChecked():

            # 图片预测
            file_extension = self.yolo_predict.source[-3:].lower()
            if file_extension == 'png' or file_extension == 'jpg':
                self.img_predict()
                return

            # 视频预测
            self.pushButton_start_stop.setChecked(True)

            if '0' in self.yolo_predict.source or '1' in self.yolo_predict.source or 'rtsp' in self.yolo_predict.source:
                self.progressBar.setFormat('实时视频流检测中...')
            if 'avi' in self.yolo_predict.source or 'mp4' in self.yolo_predict.source:
                self.progressBar.setFormat('当前检测进度:%p%')
            self.yolo_predict.continue_dtc = True
            if self.yolo_predict.source.isdigit():
                self.pushButton_start_stop.setChecked(True)
                self.progressBar.setFormat('实时视频流检测中...')
                self.yolo_predict.continue_dtc = True
   
            # 开始检测
            if not self.yolo_thread.isRunning():
                self.yolo_thread.start()
                self.main2yolo_begin_sgl.emit()
        # 暂停
        else:
            self.yolo_predict.continue_dtc = False
            self.pushButton_start_stop.setChecked(False)
            DialogOver(parent=self, text="暂停中...", title="运行暂停", flags="warning")

    # select local file
    def open_src_file(self):
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()

        # 这段代码是 PySide6 中使用 QFileDialog 对话框进行文件选择的示例。
        # 如果你单击了窗口中的某个按钮，会打开一个文件对话框，允许用户选择一个视频或图像文件。
        # QFileDialog.getOpenFileName() 是一个静态方法，返回一个元组。
        # 这个元组包含用户选择的文件的完整路径和一个空字符串。
        # 使用的是解包（unpacking）语法，将返回的元组拆分为两个变量 name 和 _。
        # name 变量包含用户选择的文件的完整路径，
        # 而 _ 变量包含一个空字符串。由于我们不使用空字符串，
        # 因此可以将其赋给一个无用且未使用的变量 _，以避免不必要的警告。
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold,
                                              "Pic File(*.mp4 *.mkv *.avi *.flv *.jpg *.png)")
        self.stop()
        if name:
            self.yolo_predict.source = name
            print('Loaded file：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)
            self.stop()
            if ".avi" in name or ".mp4" in name:
                # 显示第一帧
                self.cap = cv2.VideoCapture(name)
                ret, frame = self.cap.read()
                if ret:
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    self.show_image(rgbImage, self.label_input, 'img')

                else:
                    self.cap.release()
            else:
                self.show_image(name, self.label_input, 'path')

    def chose_cam(self):
        # try:
        # 关闭YOLO线程
        self.stop()
        # 获取本地摄像头数量
        _, cams = Camera().get_cam_num()
        popMenu = QMenu()
        popMenu.setFixedWidth(self.pushButton_sht.width())
        popMenu.setStyleSheet('''
                                            QMenu {
                                            font-size: 10px;
                                            font-family: "Microsoft YaHei UI";
                                            font-weight: light;
                                            color:white;
                                            padding-left: 5px;
                                            padding-right: 5px;
                                            padding-top: 4px;
                                            padding-bottom: 4px;
                                            border-style: solid;
                                            border-width: 0px;
                                            border-color: rgba(255, 212, 255, 255);
                                            border-radius: 3px;
                                            background-color: rgba(16,155,226,50);
                                            }
                                            ''')

        for cam in cams:
            exec("action_%s = QAction('%s 号摄像头')" % (cam, cam))
            exec("popMenu.addAction(action_%s)" % cam)
        pos = QCursor.pos()
        action = popMenu.exec(pos)

        # 设置摄像头来源
        if action:
            str_temp = ''
            selected_stream_source = str_temp.join(filter(str.isdigit, action.text()))  # 获取摄像头号，去除非数字字符
            self.yolo_predict.source = selected_stream_source

        # # 启动YOLO线程进行检测
        # if not self.yolo_thread.isRunning():
        #     self.yolo_thread.start()
        #     self.main2yolo_begin_sgl.emit()

    def load_config(self):
        config_file = 'config/setting.json'
        if not os.path.exists(config_file):
            iou = 0.7
            conf = 0.25
            rate = 10
            save_res = 0
            save_txt = 0
            new_config = {"iou": iou,
                          "conf": conf,
                          "rate": rate,
                          "save_res": save_res,
                          "save_txt": save_txt
                          }
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            if len(config) != 5:
                iou = 0.26
                conf = 0.33
                rate = 10
                save_res = 0
                save_txt = 0
            else:
                iou = config['iou']
                conf = config['conf']
                rate = config['rate']
                save_res = config['save_res']
                save_txt = config['save_txt']

        self.yolo_predict.save_res = (False if save_res == 0 else True)

        self.yolo_predict.save_txt = (False if save_txt == 0 else True)
        self.pushButton_start_stop.setChecked(False)


    def show_status(self, msg):
        if msg == '检测完成':
            self.pushButton_start_stop.setChecked(False)
            # 终止yolo线程
            if self.yolo_thread.isRunning():
                self.yolo_thread.quit()

        elif msg == '检测终止':
            self.pushButton_start_stop.setChecked(False)
            # 终止yolo线程
            if self.yolo_thread.isRunning():
                self.yolo_thread.quit()
            self.label_input.clear()
            self.label_out.clear()


    def stop(self):
        try:
            # if hasattr(self, 'cap') and self.cap.isOpened():
            #     self.cap.release()
            self.yolo_predict.release_capture()  # 这里是为了终止使用摄像头检测函数的线程，改了yolo源码
            # 结束线程
            self.yolo_thread.quit()

        except:
            pass

        self.yolo_predict.stop_dtc = True
        self.pushButton_start_stop.setChecked(False)  # 恢复按钮状态
        self.label_input.clear()  # 清空视频显示
        self.label_out.clear()  # 清空视频显示
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.progressBar.setValue(0)

    # 预测图片
    def img_predict(self):

        if check_url(self.yolo_predict.source):
            return

        self.pushButton_start_stop.setChecked(False)
        # 读取照片
        image = cv2.imread(self.yolo_predict.source)
        org_img = image.copy()
        # 加载模型
        model = self.yolo_predict.load_yolo_model()

        # 获取数据源
        iter_model = iter(model.track(source=image, show=False))
        result = next(iter_model)

        # 检查是否有目标
        if result.boxes.id is None:
            self.show_image(image, self.label_input, 'img')
            self.show_image(image, self.label_out, 'img')
            self.yolo_predict.source = ''
            return

        # 如果有目标
        try:
            id = result.boxes.id.tolist()
            self.id = [int(j) for j in id]

            coordinates = result.boxes.xyxy.tolist()
            self.coordinates = [list(map(int, e)) for e in coordinates]

            cls_list = result.boxes.cls.tolist()
            self.names_list = [int(i) for i in cls_list]

            self.names = model.names

            self.conf_list = result.boxes.conf.tolist()
            self.conf_list = ['%.2f %%' % (each * 100) for each in self.conf_list]
            self.tabel_show(self.id, self.coordinates, self.names_list, self.conf_list, self.names,
                            path=self.yolo_predict.source)

        except AttributeError:
            return

        # 画标签
        img_box = result.plot()
        # 显示图片
        self.show_image(org_img, self.label_input, 'img')
        self.show_image(img_box, self.label_out, 'img')
        self.yolo_predict.source = ''
        return

    def tabel_show(self, id, coordinates, names_list, confs, names, path=None):
        path = path
        self.tableWidget.setRowCount(0)
        for id, coordinate, cls_name, conf in zip(id, coordinates, names_list, confs):
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)

            # 设置每列的内容
            item_id = QTableWidgetItem(str(id))  # 目标id
            item_id.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_path = QTableWidgetItem(str(path))  # 路径
            item_cls = QTableWidgetItem(str(names[int(cls_name)]))    # 类别名字
            item_cls.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_conf = QTableWidgetItem(str(conf))  # 置信度
            item_conf.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_location = QTableWidgetItem(str(coordinate))  # 目标框位置

            # 将数据插入到对应行中
            self.tableWidget.setItem(row_count, 0, item_id)
            self.tableWidget.setItem(row_count, 1, item_path)
            self.tableWidget.setItem(row_count, 2, item_cls)
            self.tableWidget.setItem(row_count, 3, item_conf)
            self.tableWidget.setItem(row_count, 4, item_location)

        # 滚动到表格的底部，显示最新的目标
        self.tableWidget.scrollToBottom()


    def to_close(self):
        self.close()

    # 最小化窗口
    def to_minmal(self):
        self.showMinimized()

    # 放大缩小窗口
    def max_or_restore(self):
        if self.max_btn.isChecked():
            self.showMaximized()
        else:
            self.showNormal()

    #鼠标控制 groupBox实现窗口自由移动
    def mousePressEvent(self, event):
        # self.m_Position = event.pos()
        self.m_Position = event.position().toPoint()
        if event.button() == Qt.LeftButton:
            if 0 < self.m_Position.x() < self.frame_6.pos().x() + self.frame_6.width() and \
                    0 < self.m_Position.y() < self.frame_6.pos().y() + self.frame_6.height():
                self.m_flag = True
                

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            new_pos = event.globalPosition().toPoint()
            self.move(new_pos - self.m_Position)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False


if __name__ == "__main__":
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    app = QApplication(sys.argv)
    Home = Client()
    Home.show()
    sys.exit(app.exec())
