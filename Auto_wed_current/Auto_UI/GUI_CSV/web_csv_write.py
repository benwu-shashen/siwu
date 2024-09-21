import csv

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_base.filename import filename

class web_csv_write:
    """
    读取csv数据
    """
    def __init__(self):
        self.combobox_list = {}
        self.we = web_error()

    def csv_data_append(self, comboBox_template, comboBox_file, comboBox_sheet, box_wait, web_combobox):
        template = comboBox_template.currentText()
        file = comboBox_file.currentText()
        sheet = comboBox_sheet.currentText()
        wait = box_wait.value()

        box_list = []
        box_list.append(template)
        box_list.append(file)
        box_list.append(sheet)
        box_list.append(wait)

        self.combobox_list[web_combobox.reture_Box_line_dict(comboBox_template) + 1] = box_list # 存储数据

    def csv_data_delete(self, line):
        del self.combobox_list[line]
        combobox_list_locals = {}
        combobox_list_num = 1
        for i in self.combobox_list:
            combobox_list_locals[combobox_list_num] = self.combobox_list[i]
            combobox_list_num += 1
        del self.combobox_list
        self.combobox_list = combobox_list_locals

    def csv_data_write(self):
        """
        文件数据校验
        :return: 返回校验数据
        """
        csv_all_data = []
        csv_header = ['[模板]', '[文件名]', '[工作表名]', '[强制等待]']
        csv_all_data.append(csv_header)

        for i in self.combobox_list:
            csv_file = []
            for j in self.combobox_list[i]:
                if j != '':
                    csv_file.append(j)
                else:
                    position = self.combobox_list[i].index('')
                    self.we.box_warning('请选择第{}行{}'.format(i, csv_header[position]))
                    return False, csv_all_data

            csv_all_data.append(csv_file)

        path = filename().filename_func(r'\Auto_file\配置文件\test_data.csv')
        with open(path, 'w+', newline='', encoding='utf-8') as f:
            csv_write = csv.writer(f)
            for data in csv_all_data:
                csv_write.writerow(data)

        return True, csv_all_data
