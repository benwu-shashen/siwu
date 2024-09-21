import os
import shutil

from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data
from Auto_wed_current.Auto_base.filename import filename


class data_staging(att_property_data):
    def __init__(self,
        append_attachment_list,
        attachment_dict,
        del_attachment_list,
    ):
        super().__init__()
        self.append_attachment_list = append_attachment_list
        self.attachment_dict = attachment_dict
        self.del_attachment_list = del_attachment_list

        self.attachment_filename_list = []
        self.attachment_files_path = [] # 原始模板原文件绝对路径列表
        self.attachment_filename_dict = {} # 文件名 ： 绝对路径

        self.attachment_dir = filename().filename_func(r'\Auto_file\上传附件')
        self.filename_dir(self.attachment_dir)
        self.filename_list(self.attachment_files_path)
        self.filename_dict()

    def filename_dir(self, dir):
        for (root, dirs, file) in os.walk(dir): # 获取原始导入模板的所有文件
            self.original_filename_list = file
            for full_path in file:
                self.attachment_files_path.append(root + os.sep + full_path)

    def filename_list(self, text): # 获取文件名列表
        for filename in text:
            num = int(len(filename) - 1)

            for str in range(len(filename), -1, -1):
                if filename[str - 1] == '/':
                    filename = filename[num + 1: len(filename)]
                    self.attachment_filename_list.append(filename)
                    break

                elif filename[str - 1] != '/':
                    num -= 1

    def filename_dict(self): # 获取文件名和文件名相对路径字典
        self.attachment_filename_dict = dict(zip(self.original_filename_list, self.attachment_files_path))

    def file_update(self):
        if self.del_attachment_list != []: # 原始模板删除函数
            for data in self.del_attachment_list:
                os.remove(self.attachment_filename_dict[data])

        elif self.del_attachment_list == []:
            pass

        if self.append_attachment_list != []:
            for data in self.append_attachment_list: # 原始模板文件复制函数
                shutil.copy(self.attachment_dict[data], self.attachment_dir)

        elif self.append_attachment_list == []:
            pass
