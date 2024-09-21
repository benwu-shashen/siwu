
class web_combobox_template():
    """
    设置模板控件信息
    """
    def option_value(self, comboBox_template):
        list_data = ['原始模板', '替换模板']
        comboBox_template.addItems(list_data)
        comboBox_template.setCurrentIndex(-1)
