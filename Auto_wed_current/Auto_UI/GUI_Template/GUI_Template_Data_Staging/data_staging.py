import os
import shutil

from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
from Auto_wed_current.Auto_base.filename import filename

class data_staging(tem_property_data):
    def __init__(self,
        append_original_list,
        append_replace_list,
        original_dict,
        replace_dict,
        del_original_list,
        del_replace_list
    ):
        super().__init__()
        self.append_original_list = append_original_list
        self.append_replace_list = append_replace_list
        self.original_dict = original_dict
        self.replace_dict = replace_dict
        self.del_original_list = del_original_list
        self.del_replace_list = del_replace_list

        self.original_filename_list = []
        self.replace_filename_list = []
        self.original_files_path = [] # 原始模板原文件绝对路径列表
        self.replace_files_path = [] # 替换模板原文件绝对路径列表
        self.original_filename_dict = {} # 文件名 ： 绝对路径
        self.replace_filename_dict = {} # 文件名 ： 绝对路径

        self.original_dir = filename().filename_func(r'\Auto_file\原始导入excel模板')
        self.replace_dir = filename().filename_func(r'\Auto_file\替换导入excel模板')

        self.filename_dir(self.original_dir, '原始模板')
        self.filename_dir(self.replace_dir, '替换模板')

        self.filename_list(self.original_files_path, '原始模板')
        self.filename_list(self.replace_files_path, '替换模板')

        self.filename_dict('原始模板')
        self.filename_dict('替换模板')

    def filename_dir(self, dir, condition):
        if condition == '原始模板':
            for (root, dirs, file) in os.walk(dir): # 获取原始导入模板的所有文件
                self.original_filename_list = file
                for full_path in file:
                    self.original_files_path.append(root + os.sep + full_path)

        elif condition == '替换模板':
            for (root, dirs, file) in os.walk(dir):  # 获取原始导入模板的所有文件
                self.replace_filename_list = file
                for full_path in file:
                    self.replace_files_path.append(root + os.sep + full_path)

    def filename_list(self, text, condition): # 获取文件名列表
        for filename in text:
            num = int(len(filename) - 1)

            for str in range(len(filename), -1, -1):
                if filename[str - 1] == '/':
                    filename = filename[num + 1: len(filename)]
                    if condition == '原始模板':
                        self.original_filename_list.append(filename)

                    elif condition == '替换模板':
                        self.replace_filename_list.append(filename)
                    break

                elif filename[str - 1] != '/':
                    num -= 1

    def filename_dict(self, condition): # 获取文件名和文件名相对路径字典
        if condition == '原始模板':
            self.original_filename_dict = dict(zip(self.original_filename_list, self.original_files_path))

        elif condition == '替换模板':
            self.replace_filename_dict = dict(zip(self.replace_filename_list, self.replace_files_path))

    def file_update(self):
        if self.del_original_list != []: # 原始模板删除函数
            for data in self.del_original_list:
                os.remove(self.original_filename_dict[data])

        elif self.del_original_list == []:
            pass

        if self.del_replace_list != []: # 替换模板删除函数
            for data in self.del_original_list:
                os.remove(self.replace_filename_dict[data])

        elif self.del_replace_list == []:
            pass

        if self.append_original_list != []:
            for data in self.append_original_list: # 原始模板文件复制函数
                shutil.copy(self.original_dict[data], self.original_dir)

        elif self.append_original_list == []:
            pass

        if self.append_replace_list != []:
            for data in self.append_replace_list:  # 替换模板文件复制函数
                shutil.copy(self.replace_dict[data], self.replace_dir)

        elif self.append_replace_list == []:
            pass
