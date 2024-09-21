import os

from PyQt6 import QtWidgets

from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Thread.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
from Auto_wed_current.Auto_base.filename import filename

class template_show(tem_property_data):
    def __init__(self):
        super().__init__()
        self.filename_show()

    def filename_show(self):
        files_original = []
        files_replace = []

        self.listWidget_original.clear()
        self.listWidget_replace.clear()

        filename_original = filename().filename_func(r'\Auto_file\原始导入excel模板')
        filename_replace = filename().filename_func(r'\Auto_file\替换导入excel模板')

        for (root, dirs, file) in os.walk(filename_original):  # 原始导入模板列表展示
            files_original = file

        for dict in files_original:
            self.item = QtWidgets.QListWidgetItem(self.listWidget_original)  # 创建列表项
            self.item.setText(dict)  # 设置项文本
            self.item.setToolTip(dict)

        for (root, dirs, file) in os.walk(filename_replace):  # 替换导入模板列表展示
            files_replace = file

        for dict in files_replace:
            self.item = QtWidgets.QListWidgetItem(self.listWidget_replace)  # 创建列表项
            self.item.setText(dict)  # 设置项文本
            self.item.setToolTip(dict)

        thread_data_staging.initial_original_list = files_original # 初始模板列表数据
        thread_data_staging.initial_replace_list = files_replace # 初始模板列表数据

        thread_data_staging.delete_original_list = [] # 要被删除的模板列表
        thread_data_staging.delete_replace_list = []  # 要被删除的模板列表
