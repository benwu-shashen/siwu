import csv

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

from Auto_wed_current.Auto_Post.GUI_Post_ComboBox.post_combobox import post_combobox
from Auto_wed_current.Auto_Post.GUI_Post_Download_template.post_download_template import post_download_template
from Auto_wed_current.Auto_Post.GUI_Post_PushButton.post_button import post_button_IsEnabled
from Auto_wed_current.Auto_Post.GUI_Post_Template.post_template import post_template
from Auto_wed_current.Auto_Post.GUI_Post_Thread.post_thread import execute_thread
from Auto_wed_current.Auto_Post.__init__ import post_property_data
from Auto_wed_current.Auto_Post.GUI_Post_Untitled.untitled_post import Ui_Form_Post
from Auto_wed_current.Auto_base.filename import filename


class post_window(QtWidgets.QMainWindow, Ui_Form_Post):
    def __init__(self):
        super(post_window, self).__init__()
        self.setupUi(self)

        self.control_property()

        self.post_tableWidget_setting()
        self.dt = post_download_template()  # 模板下载
        self.et = execute_thread()
        self.bt = post_button_IsEnabled()
        self.tp = post_template() # 编辑模板
        self.cb = post_combobox()  # 初始化行数，默认添加一行，初始化选项数据
        self.filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')

        self.perform_connect()

    def perform_connect(self):
        self.pushButton_download_template.clicked.connect(self.dt.download_file) # 下载模板
        self.pushButton_post_start.clicked.connect(self.et.start)  # 执行接口测试
        self.pushButton_edit_template.clicked.connect(self.edit_template)  # 编辑模板
        self.pushButton_post_preview.clicked.connect(self.post_tableWidget_preview)  # 预览数据
        self.et.set_Enabled_bf.connect(self.bt.set_Enabled_bf)
        self.et.set_Enabled_af.connect(self.bt.set_Enabled_af)

    def control_property(self):  # 所有控件属性
        post_property_data.pushButton_post_close = self.close
        post_property_data.frame_box = self.frame_box

        post_property_data.pushButton_post_start = self.pushButton_post_start # 测试
        post_property_data.pushButton_download_template = self.pushButton_download_template # 下载模板
        post_property_data.pushButton_edit_template = self.pushButton_edit_template  # 编辑模板
        post_property_data.tableWidget_preview = self.tableWidget_preview # 表格
        post_property_data.pushButton_post_preview = self.pushButton_post_preview # 预览

    def post_tableWidget_setting(self):
        self.tableWidget_preview.setHorizontalHeaderLabels([
    "测试编号", "测试名称", "请求类型", "请求url",
    "请求参数", "响应码", "响应参数", "结果", "说明"
        ])

    def edit_template(self):
        self.tp.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.tp.show()

    def post_tableWidget_preview(self): # 填充数据
        self.tableWidget_preview.setRowCount(0)  # 清空所有行
        path = filename().filename_func(r'\Auto_file\接口CSV模板\接口模板.csv')
        with open(path, 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # 跳过第一行
            for row in csv_reader:
                row_position = self.tableWidget_preview.rowCount()
                self.tableWidget_preview.insertRow(row_position)

                for col, item in enumerate(row):
                    self.tableWidget_preview.setItem(row_position, col, QTableWidgetItem(item))


    def closeEvent(self, event):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Question)  # 设置图标
        messageBox.setWindowTitle('关闭GUI')  # 设置标题
        messageBox.setText('是否关闭接口程序')  # 设置内容
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)  # 设置按钮
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonN = messageBox.button(QMessageBox.StandardButton.No)
        buttonY.setText('确定')
        buttonN.setText('取消')

        messageBox.exec()

        if messageBox.clickedButton() == buttonY:
            event.accept()

        elif messageBox.clickedButton() == buttonN:
            event.ignore()