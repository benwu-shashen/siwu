import os

from Auto_wed_current.Auto_base.filename import filename

class post_combobox_file():
    def __init__(self):
        self.filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')

    def option_value(self, comboBox_file):
        comboBox_file.clear()
        for (root, dirs, file) in os.walk(self.filename_original):  # 原始导入模板列表展示
            files_original = file
            comboBox_file.addItems(files_original)
            comboBox_file.currentText()
            comboBox_file.setToolTip(comboBox_file.currentText()) # 鼠标悬浮，展示文本

        comboBox_file.setCurrentIndex(-1)

    def preview_button_isbool(self, comboBox_file, comboBox_preview):
        if comboBox_file.currentIndex() == -1:
            comboBox_preview.setEnabled(False)
        else:
            comboBox_preview.setEnabled(True)


