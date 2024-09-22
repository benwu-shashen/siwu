import csv
import os

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

from Auto_wed_current.Auto_Post.GUI_Post_Download_template.post_download_template import post_download_template
from Auto_wed_current.Auto_Post.GUI_Post_PushButton.post_button import post_button_IsEnabled
from Auto_wed_current.Auto_Post.GUI_Post_Template.post_template import post_template
from Auto_wed_current.Auto_Post.GUI_Post_Thread.post_thread import execute_thread
from Auto_wed_current.Auto_Post.__init__ import post_property_data
from Auto_wed_current.Auto_base.filename import filename


class post_perform_func(post_property_data):
    def __init__(self):
        super().__init__()

        self.post_tableWidget_setting()
        self.dt = post_download_template()  # 模板下载
        self.et = execute_thread()
        self.bt = post_button_IsEnabled()
        self.filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')

        self.post_perform_connect()

        self.test = self.test  # 一个bug，需要这样写才会触发信号

    def post_perform_connect(self):
        self.pushButton_post_start.clicked.connect(self.post_start) # 执行接口测试
        self.pushButton_download_template.clicked.connect(self.dt.download_file)  # 下载模板，取至web_qt_gui
        self.pushButton_post_preview.clicked.connect(self.post_tableWidget_preview)  # 预览数据
        self.pushButton_edit_template.clicked.connect(self.edit_template) # 编辑模板

        self.et.set_Enabled_bf.connect(self.bt.set_Enabled_bf)
        self.et.set_Enabled_af.connect(self.bt.set_Enabled_af)

    def edit_template(self):
        self.tp = post_template()  # 编辑模板
        self.tp.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.tp.closed.connect(self.test_01)  # 连接自定义关闭信号
        self.tp.show()

    def post_tableWidget_setting(self):
        self.tableWidget_preview.setHorizontalHeaderLabels([
    "测试编号", "测试名称", "请求类型", "请求url",
    "请求参数", "响应码", "响应参数", "结果", "说明"
])

    def test_01(self):
        for filename in os.listdir(self.filename_original):
            if filename.endswith('.xls'):
                # 构造完整的文件路径
                file_path = os.path.join(self.filename_original, filename)

                # 读取 .xls 文件
                df = pd.read_excel(file_path)

                # 构造新的 .csv 文件名
                csv_filename = filename.replace('.xls', '.csv')
                csv_file_path = os.path.join(self.filename_original, csv_filename)

                # 保存为 .csv 文件
                df.to_csv(csv_file_path, index=False, encoding='utf-8')
                os.remove(file_path)

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

    def post_start(self):
        self.et.start()

    def test(self): # 不能删
        pass