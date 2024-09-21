import os

import xlrd
from PyQt6.QtWidgets import QComboBox, QListWidgetItem, QListWidget, QCheckBox

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_base.filename import filename

class web_combobox_sheet(QComboBox):
    """
    读取模板目录
    """
    def __init__(self):
        super().__init__()
        self.filename_original = filename().filename_func(r'\Auto_file\原始导入excel模板')
        self.filename_replace = filename().filename_func(r'\Auto_file\替换导入excel模板')

    def option_value(self, comboBox_template, comboBox_file, comboBox_sheet, comboBox_wait, control_locals_QlineEdit, web_combobox):
        """

        :param comboBox_template: template组件
        :param comboBox_file: comboBox_file组件
        :param comboBox_sheet: comboBox_sheet组件
        :param QSpinBox:
        :param line:
        :param web_combobox:
        :return:
        """
        comboBox_sheet.clear()
        template = comboBox_template.currentText()

        if web_combobox.isBox_file_dict_bool(comboBox_template):
            if template == '原始模板':
                file = comboBox_file.currentText()

                if file == '':
                    pass

                elif file != '':
                    full_path = self.filename_original + os.sep + file
                    try:
                        work_book = xlrd.open_workbook(full_path)
                        sheets = work_book.sheet_names()

                    except Exception:
                        web_error().box_warning('该文件后缀名已被更改，请上传后缀名为.xls文件')

                    else:
                        self.combocheckbox(sheets, comboBox_template, comboBox_file, comboBox_sheet, comboBox_wait, control_locals_QlineEdit, web_combobox) # 执行一下函数

            elif template == '替换模板':
                file = comboBox_file.currentText()

                if file == '':
                    pass

                elif file != '':
                    full_path = self.filename_replace + os.sep + file
                    try:
                        work_book = xlrd.open_workbook(full_path)
                        sheets = work_book.sheet_names()

                    except Exception:
                        web_error().box_warning('该文件后缀名已被更改，请上传后缀名为.xls文件')

                    else:
                        self.combocheckbox(sheets, comboBox_template, comboBox_file, comboBox_sheet, comboBox_wait, control_locals_QlineEdit, web_combobox)

    def combocheckbox(self, sheets, comboBox_template, comboBox_file, comboBox_sheet, comboBox_wait, control_locals_QlineEdit, web_combobox):
        """
        生成组合框
        :param items:
        :param comboBox_template:
        :param comboBox_file:
        :param comboBox_sheet:
        :param QSpinBox:
        :param line:
        :return:
        """
        control_locals_QlineEdit.items.clear()
        control_locals_QlineEdit.temporary_data.clear()
        control_locals_QlineEdit.box_list.clear()
        for data in sheets:
            control_locals_QlineEdit.items.append(data + ' ' * 50) # 设置多选空格

        q = QListWidget()

        for i in range(len(control_locals_QlineEdit.items)):
            control_locals_QlineEdit.box_list.append(QCheckBox()) # 多选
            control_locals_QlineEdit.box_list[i].setText(control_locals_QlineEdit.items[i]) # 设置文本
            q.setItemWidget(QListWidgetItem(q), control_locals_QlineEdit.box_list[i])
            control_locals_QlineEdit.box_list[i].stateChanged.connect(lambda : self.show_selected(comboBox_template, comboBox_file, comboBox_sheet, comboBox_wait, control_locals_QlineEdit, web_combobox)) # 多选状态变更

        control_locals_QlineEdit.text.setReadOnly(True) # 设置显示为只读
        comboBox_sheet.setLineEdit(control_locals_QlineEdit.text) # 设置显示为单行显示
        comboBox_sheet.setModel(q.model()) # 设置模型为列表
        comboBox_sheet.setView(q) # 设置表单

    def get_selected(self, control_locals_QlineEdit):
        for i in range(0, len(control_locals_QlineEdit.items)):
            if control_locals_QlineEdit.box_list[i].isChecked() == True: # 判断多选选中
                get_text = control_locals_QlineEdit.box_list[i].text()
                if get_text not in control_locals_QlineEdit.temporary_data:
                    control_locals_QlineEdit.temporary_data.append(get_text)

            elif control_locals_QlineEdit.box_list[i].isChecked() == False:
                get_text = control_locals_QlineEdit.box_list[i].text()
                if get_text in control_locals_QlineEdit.temporary_data:
                    control_locals_QlineEdit.temporary_data.remove(get_text)

    def show_selected(self, comboBox_template, comboBox_file, comboBox_sheet, conboBox_wait, control_locals_QlineEdit, web_combobox):
        if web_combobox.isBox_file_dict_bool(comboBox_template):
            control_locals_QlineEdit.text.clear()
            self.get_selected(control_locals_QlineEdit)
            blank_data = []
            for data in control_locals_QlineEdit.temporary_data:
                data = data.rstrip()
                blank_data.append(data)
            ret = ','.join(blank_data)
            control_locals_QlineEdit.text.setText(ret)
            control_locals_QlineEdit.text.setToolTip(control_locals_QlineEdit.text.text())  # 鼠标悬浮，展示文本
            web_combobox.cw.csv_data_append(comboBox_template, comboBox_file, comboBox_sheet, conboBox_wait, web_combobox) # 取至web_csv_write


