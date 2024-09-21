import os
from time import sleep

import xlrd
from PyQt6.QtCore import QThread, QWaitCondition, QMutex, pyqtSignal
from PyQt6.QtWidgets import QFileDialog, QLineEdit
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
import csv
from Auto_wed_current.Auto_base.filename import filename

class thread_import(QThread, tem_property_data): # 执行开始线程
    import_verify = pyqtSignal(str)
    import_append = pyqtSignal()
    def __init__(self):
        super(QThread, self).__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.sheet_dict_all = {}

    def filedialog(self): # 创建文件对话框
        dir = QFileDialog()
        dir.setDirectory('C:/')  # 设置初始路径为桌面
        dir.setNameFilter('文件(*.csv)')  # 只显示xls文件格式

        if dir.exec_():  # 判断是否选择了文件
            filename = dir.selectedFiles()

            data_import = []
            with open(filename[0]) as csvfile:
                csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
                for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
                    data_import.append(row)

            if data_import[0] != ['模板', '文件名', '工作表名', '等待时间']:
                self.import_verify.emit('导入模板格式不正确，请第一行按照【模板,文件名,工作表名,等待时间】填写')

            self.text_import(data_import)

        else:
            pass

    def text_import(self, list):
        list.remove(list[0]) # list为导入模板的数据

        func_num = 0
        for num in list:
            if num[0] != '':
                func_num += 1

        for num in range(func_num - 1):
            self.import_append.emit()

        self.msleep(500) # 休眠0.5秒，新增完

        property_num = 1
        for data in list:
            box_template = data[0]
            box_file = data[1]
            box_sheet = data[2]
            box_wait = data[3]

            template_op = ['原始模板', '替换模板']
            if box_template not in template_op:
                print('报错template{}'.format(property_num))

            elif box_template in template_op:
                self.msleep(50)
                self.control_dict['box_template' + str(property_num)].setCurrentIndex(template_op.index(box_template))

                file_op = self.file_option(box_template)
                if box_file not in file_op:
                    print('报错file{}'.format(property_num))

                elif box_file in file_op:
                    self.msleep(50)
                    self.control_dict['box_file' + str(property_num)].setCurrentIndex(file_op.index(box_file))

                    # sheet_op = self.sheet_option(box_template, box_file)
                    # list_sheet = box_sheet.split(',')
                    #
                    # for sheet in list_sheet:
                    #     if sheet not in sheet_op:
                    #         print('报错sheet{}'.format(property_num))
                    #
                    #     elif sheet in sheet_op:
                    #         self.msleep(100)
                    #         pass
                    #         # print(sheet)
                    #         # print(sheet_op)
                    #         # print(self.ws.box_list)
                    #         # self.ws.box_list[sheet_op.index(sheet)].setChecked(True)

            if box_wait != '':
                self.msleep(50)
                self.control_dict['box_wait' + str(property_num)].setValue(int(box_wait))

            elif box_wait == '':
                pass

            property_num += 1

    def file_option(self, template):
        option_all = []
        if template == '原始模板':
            option_num = self.listWidget_original.count()
            for i in range(option_num):
                option_all.append(self.listWidget_original.item(i).text())

        elif template == '替换模板':
            option_num = self.listWidget_replace.count()
            for i in range(option_num):
                option_all.append(self.listWidget_replace.item(i).text())

        return option_all

    def sheet_option(self, template, file_name):
        if template == '原始模板':
            path = filename().filename(r'\Auto_file\原始导入excel模板\{}'.format(file_name))
            data = xlrd.open_workbook(path)
            files_original = data.sheet_names()

            return files_original

        elif template == '替换模板':
            path = filename().filename(r'\Auto_file\替换导入excel模板\{}'.format(file_name))
            data = xlrd.open_workbook(path)
            files_replace = data.sheet_names()

            return files_replace

    def run(self):
        self.mutex.lock()
        self.filedialog()
        self.mutex.unlock()

# path = filename().filename(r'\Auto_file\原始导入excel模板')
# for (root, dirs, file) in os.walk(path):  # 原始导入模板列表展示
#     files_original = file
# print(files_original)

