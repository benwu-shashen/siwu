import os

from Auto_wed_current.Auto_base.filename import filename


class web_combobox_file():
    def __init__(self):
        self.filename_original = filename().filename_func(r'\Auto_file\原始导入excel模板')
        self.filename_replace = filename().filename_func(r'\Auto_file\替换导入excel模板')

    def option_value(self, comboBox_template, comboBox_file, web_combobox):
        line_locals = 0
        for line in web_combobox.control_dict:
            if web_combobox.control_dict[line]['box_template'] == comboBox_template:
                line_locals = line
                break

        comboBox_file.clear()
        text = comboBox_template.currentText()
        if text == '原始模板':
            for (root, dirs, file) in os.walk(self.filename_original):  # 原始导入模板列表展示
                files_original = file
                comboBox_file.addItems(files_original)
                comboBox_file.currentText()
                comboBox_file.setToolTip(comboBox_file.currentText()) # 鼠标悬浮，展示文本

        elif text == '替换模板':
            for (root, dirs, file) in os.walk(self.filename_replace):  # 原始导入模板列表展示
                files_replace = file
                comboBox_file.addItems(files_replace)
                comboBox_file.currentText()
                comboBox_file.setToolTip(comboBox_file.currentText()) # 鼠标悬浮，展示文本

        comboBox_file.setCurrentIndex(-1)
        web_combobox.isBox_file_dict[line_locals - 1] = True

