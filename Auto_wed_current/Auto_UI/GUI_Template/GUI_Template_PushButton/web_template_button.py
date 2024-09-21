from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data

class web_template_button(tem_property_data):
    def __init__(self):
        super().__init__()

    def template_original_bf(self): # 选择原始模板列表文本之前
        self.pushButton_original_delete.setEnabled(False)

    def template_original_af(self): # 选择原始模板列表文本之后
        self.pushButton_original_delete.setEnabled(True)

    def template_replace_bf(self): # 选择替换模板列表文本之前
        self.pushButton_replace_delete.setEnabled(False)

    def template_replace_af(self): # 选择替换模板列表文本之后
        self.pushButton_replace_delete.setEnabled(True)

