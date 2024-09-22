import os

from PyQt6 import QtWidgets

from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_base.filename import filename

class template_show(tem_property_data):
    def __init__(self):
        super().__init__()
        self.filename_show()

    def filename_show(self):
        files_original = []

        self.listWidget_original.clear()

        filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')

        for (root, dirs, file) in os.walk(filename_original):  # 原始导入模板列表展示
            files_original = file

        for dict in files_original:
            self.item = QtWidgets.QListWidgetItem(self.listWidget_original)  # 创建列表项
            self.item.setText(dict)  # 设置项文本
            self.item.setToolTip(dict)
