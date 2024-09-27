import os
import shutil

import pandas as pd
from PyQt6.QtWidgets import QFileDialog

from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_base.filename import filename


class append_file(tem_property_data):
    def __init__(self):
        super().__init__()
        self.we = web_error()
        self.filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')

    def QMessageBox_error(self):
        self.we.box_warning('选择的文件重名，请重新选择')

    def original_file(self):
        self.filedialog(self.listWidget_original)

    def filedialog(self, listWidget=True): # 创建文件对话框
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置多选
        dir.setNameFilter('文件(*.xls)') # 只显示xls文件格式

        if dir.exec() == QFileDialog.DialogCode.Accepted:  # 判断是否选择了文件
            self.text = dir.selectedFiles()

            filename_list = [] # 文件名列表

            for filename in self.text:
                num = int(len(filename) - 1)

                for str in range(len(filename), -1, -1):
                    if filename[str - 1] == '/':
                        filename = filename[num + 1: len(filename)]
                        filename_list.append(filename)
                        break

                    elif filename[str - 1] != '/':
                        num -= 1

            listWidget_data = []
            count = listWidget.count() # 获取条目数

            filename_list_changed = []
            for filename in filename_list:
                filename_list_changed.append(filename.replace('.xls', '.csv'))
            if filename in filename_list_changed:
                self.QMessageBox_error()
                return

            for num in range(count): # 遍历listwidget中的内容
                listWidget_data.append(listWidget.item(num).text())

            listWidget.addItems(filename_list_changed)

            for data in self.text:  # 替换模板文件复制函数
                shutil.copy(data, self.filename_original)

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

            self.we.box_information("导入完成")


