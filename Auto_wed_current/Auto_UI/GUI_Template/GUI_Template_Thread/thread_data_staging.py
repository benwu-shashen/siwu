from PyQt6.QtCore import QThread, QWaitCondition, QMutex

from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Data_Staging.data_staging import data_staging
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data

class thread_data_staging(QThread, tem_property_data): # 执行开始线程
    def __init__(self, parent=None):
        super(QThread, self).__init__()
        # self.cond = QWaitCondition()
        # self.mutex = QMutex()

    # self.append_original_list取至web_template，初始为[]，用来存新增的虚拟数据地址
    # self.append_replace_list取至web_template，初始为[]，用来存新增的虚拟数据地址

    # self.original_dict取至web_template，初始为{}
    # self.replace_dict取至web_template，初始为{}

    # self.initial_original_list取至template_show，初始原始模板列表
    # self.initial_replace_list取至template_show，初始替换模板列表
    # self.delete_original_list取至template_show，要被删除的模板列表
    # self.delete_replace_list取至template_show 要被删除的模板列表
    # filename_list获取新增的模板列表
    def append_data(self, filename_list, condition, text = None):
        filename_dict_staging = dict(zip(filename_list, text))
        if condition == '原始模板':
            for data in filename_list:
                if data not in self.append_original_list: # 是否在新增模板里面
                    self.append_original_list.append(data)

                elif data in self.append_original_list:
                    del filename_dict_staging[data]
                    filename_list.remove(data)

            self.original_dict.update(filename_dict_staging)

        elif condition == '替换模板':
            for data in filename_list:
                if data not in self.append_replace_list:
                    self.append_replace_list.append(data)

                elif data in self.append_replace_list:
                    del filename_dict_staging[data]
                    filename_list.remove(data)

            self.replace_dict.update(filename_dict_staging)

        elif condition == None or condition == '':
            pass

        # print(self.append_original_list, '新增模板') # 新增模板
        # print(self.initial_original_list, '原始模板') # 原始模板
        # print(self.original_dict, '原始模板') # 文件名 : 绝对路劲
        # print(self.delete_original_list, '原始模板') # 删除模板
        # print(self.append_replace_list, '替换模板')
        # print(self.initial_replace_list, '替换模板')
        # print(self.replace_dict, '替换模板')
        # print(self.delete_replace_list, '替换模板')
        # print('----------------------------------')

    def delete_data(self, filename_list, condition):
        if condition == '原始模板':
            for data in filename_list:
                if data in self.initial_original_list:
                    self.delete_original_list.append(data)

                elif data not in self.initial_original_list:
                    pass

                if data in self.append_original_list:
                    self.append_original_list.remove(data)
                    del self.original_dict[data]

                elif data not in self.append_original_list:
                    pass

        elif condition == '替换模板':
            for data in filename_list:
                if data in self.initial_replace_list:
                    self.delete_replace_list.append(data)

                elif data not in self.initial_replace_list:
                    pass

                if data in self.append_replace_list:
                    self.append_replace_list.remove(data)
                    del self.replace_dict[data]

                elif data not in self.append_replace_list:
                    pass

        # print(self.append_original_list, '新增模板')  # 新增模板
        # print(self.initial_original_list, '原始模板')  # 原始模板
        # print(self.original_dict, '原始模板')  # 文件名 : 绝对路劲
        # print(self.delete_original_list, '原始模板')  # 删除模板
        # print(self.append_replace_list, '替换模板')
        # print(self.initial_replace_list, '替换模板')
        # print(self.replace_dict, '替换模板')
        # print(self.delete_replace_list, '替换模板')
        # print('----------------------------------')

    # self.append_original_list 新增模板
    # self.original_dict 新增模板地址，字典方式，是模板：绝对路径
    # self.delete_original_list 删除模板
    def run(self):
        # self.mutex.lock()
        self.ds = data_staging(
            self.append_original_list,
            self.append_replace_list,
            self.original_dict,
            self.replace_dict,
            self.delete_original_list,
            self.delete_replace_list
        )
        self.ds.file_update()
        # self.mutex.unlock()